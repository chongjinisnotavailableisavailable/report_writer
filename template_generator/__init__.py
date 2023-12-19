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
from docx.shared import Inches
import os

# a function to determine what kind of merging shall occur to generate a desired template
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

# A function to bold the document   
# when transplanting variables to merged doc, it should automatically revert it back to normal txt without bold
def bold(document):
    for paragraph in document.paragraphs:
                for run in paragraph.runs:
                    run.bold=True

#inserting objects like tables, logos, pictures
def insert_objects(document):
    for section in document.sections:
        header = section.header
        # for the header portion in the generated template, with the paragraph method, add a run, to add in a picture called logo.jpeg      
        for paragraph in header.paragraphs:
            paragraph.add_run().add_picture('Logo.jpg')

#adds in the TnC/whatever image add the end of the doc.
def TnC(document):
     last_page = document.add_paragraph()
     #on the last page, add_run to insert an image
     #note: the current image size (not file memory size), by default takes up one whole page, and hence a page break is not needed
     run = last_page.add_run()
     image = 'TnC.jpg'
     # this portion forces the image to be of a certain size to take up 1 page, to eliminate the need for a page break
     width_inch = 6.27
     height_inch = 8.76
     run.add_picture(image, width = Inches(width_inch), height = Inches(height_inch))
                 
# a function to generate a template base on given input
# default font Times New Roman
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
    
    bold(generated_template)

    insert_objects(generated_template)

    TnC(generated_template)

    output_file_path = os.path.join(output_folder, 'output__with_logo_and_TnC.docx')

    generated_template.save(output_file_path)

    return output_file_path


if __name__ == "__main__":   
    gen_template()