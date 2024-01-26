import imageio

def print_video_metadata(file_path):
    try:
        # Use imageio to get metadata for the video file
        with imageio.get_reader(file_path) as reader:
            meta_data = reader.get_meta_data()
            print(f'Metadata for {file_path}:\n{meta_data}')
    except Exception as e:
        print(f'Error reading video metadata: {e}')

# Replace 'your_mov_file.mov' with the actual path to your MOV file
mov_file_path = '/Users/jadephay/CanonReNamer/ToDo/MVI_1119.MOV'

# Call the function to print metadata
print_video_metadata(mov_file_path)

import os
from datetime import datetime

file_path = '/Users/jadephay/CanonReNamer/ToDo/MVI_1119.MOV'

# Get file information using os.stat
file_stat = os.stat(file_path)

# Get creation time and convert to a human-readable format
creation_time = datetime.fromtimestamp(file_stat.st_birthtime)
print(f'File creation time: {creation_time}')

# Get modification time and convert to a human-readable format
modification_time = datetime.fromtimestamp(file_stat.st_mtime)
print(f'File modification time: {modification_time}')
