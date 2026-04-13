import pypdf
import sys

def get_pdf_text(file_path, start_page=0, end_page=10):
    try:
        with open(file_path, "rb") as f:
            reader = pypdf.PdfReader(f)
            total_pages = len(reader.pages)
            end_page = min(end_page, total_pages)
            text = ""
            for i in range(start_page, end_page):
                text += f"--- Page {i+1} ---\n"
                text += reader.pages[i].extract_text() + "\n"
            return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    file_path = "CS229/main_notes.pdf"
    print(get_pdf_text(file_path))
