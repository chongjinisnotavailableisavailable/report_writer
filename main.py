from folder_creater import create_folder
from variable_test import folder_name
from doc_opener import open_new_doc


def main():
    create_folder() #ensures folder is there
    open_new_doc(folder_name) #creates a document in folder
    
"""
    open_new_doc()
    format_checker()
    format_select()
    report_writer()
    save_and_close()

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