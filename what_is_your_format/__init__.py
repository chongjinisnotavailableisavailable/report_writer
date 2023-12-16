from variable_test import reports_format 

#the desired format for the report; not to be mistaken with the function in MSWord format
    #code that imports the relevant required blocks of text from a set of templates stored in a database remote/local
    #ideally it has to be modularised, indexed/number tagged
    #probably use a dictionary for key;value? mapping????

def format_check():
    _report_formats = {"generic":"generic_report_format","corporate":"...","simplified":"...","detailed": "..."}

    selected_format = _report_formats.get(reports_format)

    return selected_format


print(f"Selected format is {reports_format}")

