import os

def main(folder_name):
    # Create the folder 'report' if it doesn't exist on the user's desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    report_folder = os.path.join(desktop_path, folder_name)
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    return(report_folder)

if __name__ == "__main__":
    main(folder_name="test")