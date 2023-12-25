# Set the folder name and file name for the Word document
folder_name = 'report'
file_name = 'example.docx'
reports_format = 'generic'
client_name = "Ninomae Ina'nis"
records = [
    ('3', '101', 'Spam', 'a'),
    ('7', '422', 'Eggs', 'b'),
    ('4', '631', 'Spam, spam, eggs, and spam','c')
]

variables_dict = {
    '{$reference}': 'new 1',
    '{$A}': 'new 2',
    '{$topic}': 'This is a title'
}

generic = ["1_Introduction.docx", "2_Description.docx", "13_Conclusion page.docx", "14_Disclaimer.docx", "15_Signature block.docx"]

#last three blocks need some special fomatting, requires breaking up

folder_containing_images = input("Enter Path ")