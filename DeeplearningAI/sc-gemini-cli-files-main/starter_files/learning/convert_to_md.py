from docx import Document

def docx_to_markdown(docx_path, md_path):
    doc = Document(docx_path)
    md_content = []
    
    for paragraph in doc.paragraphs:
        # Check for headings based on style name or level
        if paragraph.style.name == 'Title':
            md_content.append(f"# {paragraph.text}\n")
        elif paragraph.style.name.startswith('Heading'):
            try:
                # Extract level from style name (e.g., 'Heading 1' -> level 1)
                level = int(paragraph.style.name.split()[-1])
                md_content.append(f"{'#' * level} {paragraph.text}\n")
            except (ValueError, IndexError):
                # Fallback if style name doesn't match expected pattern
                md_content.append(f"## {paragraph.text}\n")
        elif paragraph.text.strip():
            md_content.append(f"{paragraph.text}\n")
            
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_content))
    
    print(f"Converted {docx_path} to {md_path}")

if __name__ == "__main__":
    docx_to_markdown('CS229_Course_Summaries.docx', 'CS229_Course_Summaries.md')
