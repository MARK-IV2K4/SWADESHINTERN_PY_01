import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory into subfolders based on their file types.
    
    Parameters:
        directory (str): The path to the directory to organize.
    
    Returns:
        None
    """
    if not os.path.exists(directory):
        raise ValueError(f"The directory '{directory}' does not exist.")
    
    # Define file type categories and their extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".pptx", ".odt"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Video": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
        "Others": []  # For files that don't match any category
    }

    # Create category folders if they don't exist
    for category in file_categories:
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate through files in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
        
        # Determine the file's category based on its extension
        file_moved = False
        for category, extensions in file_categories.items():
            if item.lower().endswith(tuple(extensions)):
                shutil.move(item_path, os.path.join(directory, category, item))
                file_moved = True
                break
        
        # If no category matched, move to "Others"
        if not file_moved:
            shutil.move(item_path, os.path.join(directory, "Others", item))

    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    print("Welcome to the File Organizer!")
    directory = input("Enter the path to the directory you want to organize: ").strip()
    try:
        organize_files(directory)
    except Exception as e:
        print(f"Error: {e}")
