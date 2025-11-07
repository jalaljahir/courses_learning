import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.util import ngrams
from collections import Counter

from rapidfuzz import fuzz  # Optional for fuzzy matching; install if needed


# Load DataFrame
df = pd.read_csv(r'data\data.csv')  # Replace with your file path
comments_col = 'comments'  # Your column name

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if pd.isna(text):
        return ''
    # Lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', str(text).lower())
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stop words and lemmatize
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and len(token) > 2]
    return ' '.join(lemmatized)

# Apply preprocessing
df['processed_comments'] = df[comments_col].apply(preprocess_text)
print(f"Preprocessed sample: {df['processed_comments'].iloc[0]}")

# Function to extract bigrams from processed text
def extract_bigrams(text):
    tokens = word_tokenize(text)
    return list(ngrams(tokens, 2))  # Bigrams

# Extract all bigrams
df['bigrams'] = df['processed_comments'].apply(extract_bigrams)

# Flatten and count bigram frequencies (optional, for basic stats)
all_bigrams = [bigram for bigrams_list in df['bigrams'] for bigram in bigrams_list]
bigram_freq = Counter(all_bigrams)
print("Top 5 frequent bigrams:", bigram_freq.most_common(5))

# TF-IDF for unigrams and bigrams
# For unigrams
vectorizer_uni = TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1,1))
tfidf_uni = vectorizer_uni.fit_transform(df['processed_comments'])
feature_names_uni = vectorizer_uni.get_feature_names_out()

# For bigrams
vectorizer_bi = TfidfVectorizer(max_features=500, stop_words='english', ngram_range=(2,2))
tfidf_bi = vectorizer_bi.fit_transform(df['processed_comments'])
feature_names_bi = vectorizer_bi.get_feature_names_out()

# Get top key terms/phrases (combine uni + bi, score > threshold)
def get_top_terms(tfidf_matrix, feature_names, top_n=50, threshold=0.1):
    scores = tfidf_matrix.mean(axis=0).A1
    top_indices = scores.argsort()[-top_n:][::-1]
    top_terms = [(feature_names[i], scores[i]) for i in top_indices if scores[i] > threshold]
    return top_terms

top_unigrams = get_top_terms(tfidf_uni, feature_names_uni)
top_bigrams = get_top_terms(tfidf_bi, feature_names_bi)

# Combine into a single list of key terms/phrases
key_terms = [term[0] for term in top_unigrams + top_bigrams]
print("Sample key terms/phrases:", key_terms[:10])

# Optional: Save to DataFrame for UI
df['key_phrases'] = df['processed_comments'].apply(lambda x: [phrase for phrase in key_terms if phrase in x])


def filter_by_term(df, term, column=comments_col, fuzzy_threshold=80):
    filtered = df[df[column].str.contains(term, case=False, na=False)]
    # Optional fuzzy: For more flexible matching
    # fuzzy_matches = df[df[column].apply(lambda x: fuzz.partial_ratio(str(x), term) >= fuzzy_threshold if pd.notna(x) else False)]
    return filtered

# Test
sample_term = key_terms[0]
filtered_df = filter_by_term(df, sample_term)
print(f"Rows matching '{sample_term}': {len(filtered_df)}")


# Start app

import streamlit as st
import pandas as pd
# Assume df, key_terms, filter_by_term are defined from previous steps
# (Load them here or in a shared script)

st.title("Comment Filter Dashboard")

# Sidebar for filters
st.sidebar.header("Filter by Key Terms/Phrases")
selected_terms = st.sidebar.multiselect(
    "Select from extracted key terms/phrases:",
    options=key_terms,
    default=key_terms[:3]  # Default to top 3
)
custom_term = st.sidebar.text_input("Or enter a custom term:")

# Apply filters
if selected_terms or custom_term:
    filtered_df = df.copy()
    for term in selected_terms:
        filtered_df = filter_by_term(filtered_df, term)
    if custom_term:
        filtered_df = filter_by_term(filtered_df, custom_term)
    
    # Display results
    st.write(f"Showing {len(filtered_df)} rows matching your filters.")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.write("Select terms to filter.")
    st.dataframe(df.head(10), use_container_width=True)  # Show sample

# Optional: Stats section
st.header("Analysis Stats")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Records", len(df))
with col2:
    st.metric("Unique Key Phrases Extracted", len(key_terms))