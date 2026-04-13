import pypdf

def generate_study_guide(file_path):
    chapters = [
        (1, "Linear Regression", 8),
        (2, "Classification and Logistic Regression", 20),
        (3, "Generalized Linear Models", 29),
        (4, "Generative Learning Algorithms", 34),
        (5, "Kernel Methods", 48),
        (6, "Support Vector Machines", 59),
        (7, "Deep Learning", 80),
        (8, "Generalization", 113),
        (9, "Regularization and Model Selection", 135),
        (10, "Clustering and K-means", 145),
        (11, "EM Algorithms", 148),
        (12, "Principal Components Analysis", 165),
        (13, "Independent Components Analysis", 171),
        (14, "Self-supervised Learning", 177),
        (15, "Reinforcement Learning", 189),
        (16, "LQR, DDP and LQG", 206),
        (17, "Policy Gradient", 220)
    ]
    
    study_guide_content = "# CS229 Detailed Study Guide\n\n"
    
    with open(file_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        total_pages = len(reader.pages)
        
        for i, (num, name, start_page) in enumerate(chapters):
            end_page = start_page + 4 # Extract 5 pages for more detail
            if i + 1 < len(chapters):
                end_page = min(end_page, chapters[i+1][2])
            
            text = ""
            for p in range(start_page - 1, min(end_page - 1, total_pages)):
                text += reader.pages[p].extract_text() + "\n"
            
            # Simple heuristic to extract potential "Key Concepts" (capitalized terms or first lines)
            # and format them into the guide.
            study_guide_content += f"## Chapter {num}: {name}\n"
            study_guide_content += "### Core Concepts\n"
            
            # Extract first paragraph or key intro lines
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            intro = " ".join(lines[:10])
            study_guide_content += f"- **Overview:** {intro[:300]}...\n"
            
            # Look for formulas or specific keywords (heuristic)
            study_guide_content += "### Key Technical Points\n"
            if "gradient descent" in text.lower():
                study_guide_content += "- **Gradient Descent:** Optimization algorithm for minimizing the cost function.\n"
            if "likelihood" in text.lower():
                study_guide_content += "- **Maximum Likelihood Estimation:** Method for estimating model parameters.\n"
            if "kernel" in text.lower():
                study_guide_content += "- **The Kernel Trick:** Efficient computation in high-dimensional feature spaces.\n"
            if "backpropagation" in text.lower():
                study_guide_content += "- **Backpropagation:** Algorithm for calculating gradients in neural networks.\n"
            if "MDP" in text.upper():
                study_guide_content += "- **Markov Decision Process (MDP):** Formal framework for modeling decision making in RL.\n"
            
            study_guide_content += "\n---\n\n"
            
    return study_guide_content

if __name__ == "__main__":
    file_path = "CS229/main_notes.pdf"
    guide = generate_study_guide(file_path)
    with open("CS229_Study_Guide.md", "w") as f:
        f.write(guide)
    print("Study guide saved to CS229_Study_Guide.md")
