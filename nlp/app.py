import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image  # For plots

# Load data (adjust path; or run Steps 1-4 first)
# df = pd.read_pickle('processed_df.pkl')
# Load other vars: key_terms, top_words_per_topic, etc. (from globals or pickle)

st.title("Comprehensive Comment Analysis Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(df))
col2.metric("Unique Key Phrases", len(key_terms))
col3.metric("Optimal Topics", optimal_num_topics)
col4.metric("Default Coherence", results['c_v']['coh_score'] if 'c_v' in results else 'N/A')

# Plots
st.header("Evaluation Plots")
try:
    img = Image.open('metrics_comparison.png')
    st.image(img, caption="Coherence & Perplexity vs. Topics")
except:
    st.info("Run Step 3.6 to generate plots.")

# Topic Distribution Chart
st.header("Topic Distribution")
topic_counts = df['dominant_topic'].value_counts().sort_index().reset_index()
topic_counts['label'] = [topic_labels[i] for i in topic_counts['index']]
chart = alt.Chart(topic_counts).mark_bar().encode(
    x='label:N', y='dominant_topic:N', color='label:N', tooltip=['label', 'dominant_topic']
).properties(width=400, height=300)
st.altair_chart(chart, use_container_width=True)

# Top Words
with st.expander("View Top Words per Topic"):
    for i, words in enumerate(top_words_per_topic):
        st.write(f"**{topic_labels[i]}**: {', '.join(words)}")

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_terms = st.sidebar.multiselect("Key Terms/Phrases:", options=key_terms, default=key_terms[:3])
custom_term = st.sidebar.text_input("Custom Term:")
st.sidebar.subheader("By Topic")
selected_topic = st.sidebar.selectbox("Select Topic:", options=[None] + list(range(optimal_num_topics)), 
                                      format_func=lambda x: topic_labels[x] if x is not None else "All")
topic_threshold = st.sidebar.slider("Min Topic Probability:", 0.0, 1.0, 0.5)

# Apply Filters
filtered_df = combined_filter(df, selected_terms, selected_topic, custom_term, topic_threshold)
st.write(f"Showing {len(filtered_df)} rows.")

# Display Table
st.dataframe(filtered_df, use_container_width=True)

# Download
st.download_button("Download Filtered Data", filtered_df.to_csv(), "filtered_comments.csv")

if not selected_terms and selected_topic is None and not custom_term:
    st.info("Use filters to explore!")