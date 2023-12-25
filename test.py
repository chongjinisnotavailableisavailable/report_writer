import os

def delete_pycache(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "__pycache__":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Replace 'your_folder_path' with the path to the folder containing '__pycache__' files
folder_path = os.getcwd()
print(folder_path)

delete_pycache(folder_path)