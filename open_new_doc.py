import os
from docx import Document

def main(report_folder=os.getcwd(), file_name="test.docx"):

    # Create the Word document path inside the 'report' folder
    file_path = os.path.join(report_folder, file_name)

    # Load the Word document or create a new one if it doesn't exist
    if not os.path.exists(file_path):
        doc = Document()
        doc.save(file_path)

    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        print(paragraph.text)

if __name__ == "__main__":
    main()

