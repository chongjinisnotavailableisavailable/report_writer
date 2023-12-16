"""
templates should merge required blocks of text automatically; append in acsending order
list of common pages:
    Main desc
    rationale
    conclusion page
    evidence appendix
    pictures
    disclaimers & citing & etc

"""
from variable_test import reports_format
from docx import Document

#change this to be more flex


relevant_contents = ["1_Introduction.docx", "2_Description.docx"]

def merge_relevant(files = relevant_contents, output_file = 'merged.docx'):
    
    generated_template = Document()

    for file_path in files:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            p = generated_template.add_paragraph()
            p.add_run(paragraph.text).bold=True

    generated_template.save(output_file)      
    
if __name__ == "__main__":   
    merge_relevant(relevant_contents, 'merged.docx')


#from here; to automate relevents contents based on list
#when transplanting variables to merged doc, it should automatically revert it back to normal txt without bold

