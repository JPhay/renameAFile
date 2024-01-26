import os
from datetime import datetime

def get_creation_time(file_path):
    try:
        # Get file information using os.stat
        file_stat = os.stat(file_path)
        
        # Use st_birthtime for creation time (works on macOS)
        creation_time = datetime.fromtimestamp(file_stat.st_birthtime)
        return creation_time
    except Exception as e:
        print(f'Error getting creation time for {file_path}: {e}')
        return None

def is_media_file(file_path):
    # Check if the file has a common image or video extension
    media_extensions = {'.jpg', '.jpeg', '.mov'}
    return os.path.splitext(file_path)[1].lower() in media_extensions

def rename_and_move_media(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Check if the file is an image or video
            if is_media_file(file_path):
                # Get creation time
                creation_time = get_creation_time(file_path)
                
                if creation_time:
                    # Format date as yyyyMMdd_HH:mm:ss
                    new_name = creation_time.strftime('%Y%m%d_%H:%M:%S') + os.path.splitext(file_name)[1]
                    
                    # New path for the renamed file in the "Done" folder
                    new_path = os.path.join(output_folder, new_name)
                    
                    # Rename and move the file
                    os.rename(file_path, new_path)
                    print(f'Renamed and moved: {file_path} -> {new_path}')
            else:
                print(f'Skipped: {file_path} (Not a JPEG image or MOV video)')

if __name__ == "__main__":
    # Specify input and output folders
    input_folder = "ToDo"
    output_folder = "Done"

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Rename and move JPEG images and MOV videos
    rename_and_move_media(input_folder, output_folder)
