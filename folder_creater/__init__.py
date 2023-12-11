try:
    from variable_test import folder_name
except ModuleNotFoundError:
    pass
import os

def create_folder():
    # Create the folder 'report' if it doesn't exist on the user's desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    report_folder = os.path.join(desktop_path, folder_name)
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    return(report_folder)

print(f"created folder, {folder_name}")