import pypdf

def recreate_guide(file_path, output_path):
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
    
    md_content = "# CS229: Machine Learning Full Course Guide\n\n"
    md_content += "This guide contains both a high-level summary and a detailed study guide for each chapter.\n\n"
    
    with open(file_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        total_pages = len(reader.pages)
        
        for i, (num, name, start_page) in enumerate(chapters):
            # Read a larger chunk for better synthesis
            chunk_size = 6
            end_page = start_page + chunk_size
            if i + 1 < len(chapters):
                end_page = min(end_page, chapters[i+1][2])
            
            text = ""
            for p in range(start_page - 1, min(end_page - 1, total_pages)):
                text += reader.pages[p].extract_text() + "\n"
            
            md_content += f"## Chapter {num}: {name}\n\n"
            
            # Summary Section
            md_content += "### Chapter Summary\n"
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            summary_text = " ".join(lines[:15]) # More lines for summary
            md_content += f"{summary_text[:500]}...\n\n"
            
            # Study Guide Section
            md_content += "### Study Guide & Key Points\n"
            
            # Look for specific headers or keywords in the text
            if "gradient" in text.lower():
                md_content += "- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\\theta)$.\n"
            if "likelihood" in text.lower():
                md_content += "- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.\n"
            if "logistic" in text.lower() or "sigmoid" in text.lower():
                md_content += "- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.\n"
            if "kernel" in text.lower():
                md_content += "- **Kernels:** Using the 'Kernel Trick' to map features into high-dimensional spaces efficiently via inner products.\n"
            if "neural" in text.lower() or "backprop" in text.lower():
                md_content += "- **Neural Networks:** Multi-layer architectures using non-linear activation functions and backpropagation for training.\n"
            if "bias" in text.lower() and "variance" in text.lower():
                md_content += "- **Bias-Variance Tradeoff:** Understanding the balance between underfitting and overfitting.\n"
            if "unsupervised" in text.lower() or "clustering" in text.lower():
                md_content += "- **Unsupervised Learning:** Discovering patterns in unlabeled data (e.g., K-means, PCA).\n"
            if "markov" in text.lower() or "policy" in text.lower():
                md_content += "- **Reinforcement Learning:** Modeling agents in environments using MDPs, value functions, and policy gradients.\n"

            md_content += "\n---\n\n"
            
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(md_content)
    print(f"Recreated guide saved to {output_path}")

if __name__ == "__main__":
    recreate_guide("CS229/main_notes.pdf", "CS229_Recreated_Guide.md")
