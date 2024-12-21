import os

def file_check(folder):
        try:
            files=os.listdir(folder)
            return files, None
        except PermissionError:
            return None, "Permission Denied"
        except FileNotFoundError:
            return None, "File Not Found"
        
def file_display():
    folders = input("Enter the name of folders in which you want to look for files:").split()
    for folder in folders:
        files, Error = file_check(folder)
        if files:
            print(f"/nHere are the files that you wanted to look for {folder}")
            for file in files:
                print(file)
        else:
             print(Error, files, folders)

file_display()