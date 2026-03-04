import pymupdf4llm

def load_pdf(file_path : str):
    pages = pymupdf4llm.to_markdown(
        doc = file_path,
        page_chunks = True,
        show_progress = True
    )
    return pages

