import os
import shutil

# You can change this for your desired output folder
mainOutputFolder = "organize/"

# This is not really necessary since we discovered the files dynamically
# However, if you want to stop the "[!} {ext} is currently not supported" message
# You can add the file extensions here
files = {
    ".py": [],
    ".exe": [],
    ".pdf": [],
    ".cpp": [],
    ".h": [],
    ".json":[],
}

# This function will move the files to the specified folder
def moveFiles(ext, filename):
    """
    Move the files to the specified folder
    """
        
    # For every file in the list of files with the same extensionile
    for file in files[ext]:
        # Try to move the file to the specified folder
        try:
            shutil.move(file, f"{mainOutputFolder}{filename}/{file}")
            print(f"[/] Moved {file} to {filename}/{file}")

        # Otherwise, permission might be denied
        except:

            # If you are getting this error, you need to be sure that no other program is using the file.
            print(f"[!] Permission might be denied for \"{file}\"... Trying to Continue")

if __name__ == "__main__":

    # Get the current directory
    dirs = os.scandir()

    # For every file in the current directory# 
    for file in dirs:

        # Try to get the index of the last dot in the file name
        try:
            ext_idx = file.name.rindex('.')

        # If there is no dot, then we'll just assume it is a folder
        except:
            print(f"[!] Found a possible Folder: {file.name}")
            continue

        # Get the file extension
        ext = file.name[ext_idx:].lower()
        
        # Try to add the file to the list of files with the same extensiony 
        try:
            files[ext].append(file.name)
        
        # If the extension is not specified in the files dictionary, then we'll add it
        except:
            print(f"[!] {ext} is currently not supported")
            print(f"[!] Supporting \"{ext}\"")
            files[ext] = []
            files[ext].append(file.name)
    
    # Try to create the main output foldery 
    try:
        os.mkdir(f"{mainOutputFolder}")
        print(f"[/] Created {mainOutputFolder}")
    
    # If it fails, then we'll just use the current directory
    except:
        # If it continuously fails, there might be a permission issuee 
        mainOutputFolder = ""
        print(f"[!] Can't Create {mainOutputFolder}... Trying to continue using the current directory")

    # For every file extension in the files dictionary
    for key,value in files.items():

        # If there are files with the same extension# 
        if len(value) >= 1:
            
            # Create a folder with the name of the extension
            try:
                os.mkdir(f"{mainOutputFolder}{key[1:]}")
                print(f"[/] Created {key[1:]}")
            except:
                printf(f"[!] {key[1:]} already exists")
            
            # then move the files to the specified folder.
            moveFiles(key, key[1:])
        else:
            continue
