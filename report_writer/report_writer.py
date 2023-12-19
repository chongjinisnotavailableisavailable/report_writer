import os
from variable_test import reports_format
from template_generator import gen_template, template_finder
from object_insert import insert_objects

#writes the report, default path folder is being ensured by create_folder() in main; 
#to update and add in ability to change path
def report_writer_main(files_to_merge = template_finder(reports_format), folder_to_save_in = os.path.join(os.path.expanduser('~'), 'Desktop','report')):

    #generates a template w.r.t the required format
    gen_template(files_to_merge, folder_to_save_in)

    
    
    """
    insert_headers()
    insert_tables()
    insert_paragraphs()
    replace_keywords()
    insert_pictures
    insert_signor()
    format_report()
    """


if __name__ == "__report_writer__":   
    report_writer_main()