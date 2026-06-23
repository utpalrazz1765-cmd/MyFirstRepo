import os

def get_text_file_metadat(file_path):
    if os.path.exists(file_path):
        file_metadata = {
            'file_name': os.path.basename(file_path),
            'file_size': os.path.getsize(file_path),
            'Creation_time': os.path.getctime(file_path),
            'modified_time': os.path.getmtime(file_path),
        }
        return file_metadata
    else:
        return None

file_path = text.txt
metadata = get_text_file_metadata(file_path)
if metadata:
    print("File Name : ", metadata[file_name])
    print("File Size : ", metadata[file_size])
    print(f"Creation Time : {metadata[Creation_time]}")
    print(f"Modified Time : {metadata[modified_time]}")
else:
    print("The file does not exist")
