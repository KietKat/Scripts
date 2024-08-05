import os
import shutil

# Define the path to the downloads directory
downloads_dir = r'C:\Users\KietN\Downloads'  # Use raw string to avoid unicode escape issues

# Define a dictionary of file extensions and their corresponding folder names
file_type_folders = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
    'documents': ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlsx', 'csv'],
    'videos': ['mp4', 'avi', 'mkv', 'mov', 'wmv'],
    'music': ['mp3', 'wav', 'flac', 'aac'],
    'archives': ['zip', 'rar', 'tar', 'gz', '7z'],
    'scripts': ['py', 'js', 'sh', 'bat', 'rb'],
    'mathlab' : ['m'],
    'R' : ['r']
}

# Create the destination folders if they don't exist
for folder in file_type_folders.keys():
    folder_path = os.path.join(downloads_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def classify_file(file_path):
    """Classify a file into a folder based on its extension."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower().strip('.')
    for folder, extensions in file_type_folders.items():
        if ext in extensions:
            dest_folder = os.path.join(downloads_dir, folder)
            shutil.move(file_path, dest_folder)
            print(f"Moved {file_path} to {dest_folder}")
            break

def sort_existing_files():
    """Sort all existing files in the downloads directory."""
    for file_name in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, file_name)
        if os.path.isfile(file_path):
            classify_file(file_path)

if __name__ == '__main__':
    sort_existing_files()
