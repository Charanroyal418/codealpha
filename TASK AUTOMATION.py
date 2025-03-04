import os
import shutil

# Define source and destination directories
source_dir = 'C:/Users/Kodipunjula charan/Documents'  # Replace with your actual source directory path
dest_dir = 'C:/Users/Kodipunjula charan/Organized'  # Replace with your actual destination directory path

# List of file types and their corresponding directories
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.txt'],
    'audio': ['.mp3', '.wav'],
    'videos': ['.mp4', '.mkv']
}


# Function to organize files
def organize_files():
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"The source directory {source_dir} does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over files in source directory
    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()

        # Move files to corresponding directories based on file type
        for category, extensions in file_types.items():
            if file_ext in extensions:
                dest_path = os.path.join(dest_dir, category)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                try:
                    shutil.move(os.path.join(source_dir, filename), os.path.join(dest_path, filename))
                    print(f"Moved {filename} to {dest_path}")
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
                break


if __name__ == "__main__":
    organize_files()
    print("Files have been organized.")
