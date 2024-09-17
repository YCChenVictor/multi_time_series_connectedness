import os

def get_file_names(path):
    all_entries = os.listdir(path)
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(path, entry))]
    return files
    
