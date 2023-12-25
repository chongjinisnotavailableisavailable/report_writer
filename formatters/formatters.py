from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def justify_text(text_to_be_justiefied):
    text_to_be_justiefied.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY