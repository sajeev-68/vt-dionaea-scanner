import os

def getnewfiles_as_list():
    current_file = "files.txt"
    directory_path = '/home/<ur_directory_here>/tpotce/data/dionaea/binaries' #change directory name to reflect your system
    now_binaries = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    with open(current_file, "r") as file:
        old_binaries = [line.strip() for line in file]

    unique_files = list(set(now_binaries) ^ set(old_binaries))
    

    if not unique_files:
        return False
    else:
        return unique_files


    
