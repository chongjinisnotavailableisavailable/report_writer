from folder_creater import create_folder
from what_is_your_format import format_check
from report_writer import report_writer_main



def main():
    create_folder() #ensures folder is there; default desktop/report; prompts path in future using kwargs?
    format_check() #looks at what format of the report (i.e. generic, detailed, etc) is required and imports the relevant modules ; is this even relevant anymore
    report_writer_main() #writes the report
    
"""
report_writer()
    insert_headers()
    insert_tables()
    insert_paragraphs()
    replace_keywords()
    insert_pictures
    insert_signor()
    format_report()
"""
if __name__ == "__main__":   
    main()