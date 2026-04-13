import pypdf
import sys

def get_chapter_starts(file_path):
    # Manually defined based on TOC extraction
    chapters = [
        (1, "Linear regression", 8),
        (2, "Classification and logistic regression", 20),
        (3, "Generalized linear models", 29),
        (4, "Generative learning algorithms", 34),
        (5, "Kernel methods", 48),
        (6, "Support vector machines", 59),
        (7, "Deep learning", 80),
        (8, "Generalization", 113),
        (9, "Regularization and model selection", 135),
        (10, "Clustering and the k-means algorithm", 145),
        (11, "EM algorithms", 148),
        (12, "Principal components analysis", 165),
        (13, "Independent components analysis", 171),
        (14, "Self-supervised learning and foundation models", 177),
        (15, "Reinforcement learning", 189),
        (16, "LQR, DDP and LQG", 206),
        (17, "Policy Gradient (REINFORCE)", 220)
    ]
    
    with open(file_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        total_pages = len(reader.pages)
        
        extracted_data = {}
        for i, (num, name, start_page) in enumerate(chapters):
            # Extract first 2 pages of each chapter for summary
            end_page = start_page + 2
            # Also ensure we don't go past the next chapter's start
            if i + 1 < len(chapters):
                end_page = min(end_page, chapters[i+1][2])
            
            text = ""
            # pypdf uses 0-indexed pages, TOC used 1-indexed (likely)
            # Let's check page 8 in PDF (index 7)
            for p in range(start_page - 1, min(end_page - 1, total_pages)):
                text += reader.pages[p].extract_text() + "\n"
            extracted_data[name] = text
            
    return extracted_data

if __name__ == "__main__":
    file_path = "CS229/main_notes.pdf"
    data = get_chapter_starts(file_path)
    for name, text in data.items():
        print(f"=== CHAPTER: {name} ===")
        print(text[:1000]) # Print first 1000 chars of each for me to see
        print("-" * 40)
