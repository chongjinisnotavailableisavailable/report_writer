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
import os

def template_finder(required_format):
    
    def generic_template():
         required = ["1_Introduction.docx", "2_Description.docx"]
         return required
    def corporate_template():
        ...
        
    def simplified_template():
        ...
        
    def detailed_template():
        ...
    
    cases = {
        'generic': generic_template,
        'coporate': corporate_template,
        'simplified': simplified_template,
        'detailed': detailed_template
        
    }
    required = cases.get(required_format)

    if required:
        return required()


def bold(document):
    for paragraph in document.paragraphs:
                for run in paragraph.runs:
                    run.bold=True

def gen_template(files, output_folder = os.path.join(os.path.expanduser('~'), 'Desktop','report')):
    
    generated_template = Document()

    for file_path in files:
        doc = Document(file_path)
        font_styles = doc.styles.add_style(name = 'Times New Roman', style_type = 1)
        font = font_styles.font
        font.name = 'Times New Roman'
        for paragraph in doc.paragraphs:
            p = generated_template.add_paragraph()
            p.add_run(paragraph.text).font.name = 'Times New Roman'
        
    output_file_path = os.path.join(output_folder, 'merged.docx')

    bold(generated_template)

    generated_template.save(output_file_path)

  
    


#when transplanting variables to merged doc, it should automatically revert it back to normal txt without bold

