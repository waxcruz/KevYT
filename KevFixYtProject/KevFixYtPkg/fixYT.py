'''
Created on Jan 21, 2024

@author: billw
'''
import os
import sys
import shutil

def get_files_in_folder(sourceFolderPath: str, destinationFolderPath: str):
      
    try:
        # List all files in the source folder
        files = os.listdir(sourceFolderPath)
        
        # Iterate through the files and copy to destination folder using YT key as file name
        for file_name in files:
            sourceFilePath = os.path.join(sourceFolderPath, file_name)          
            # Check if it's a file (not a directory)
            if os.path.isfile(sourceFilePath):
                parts = file_name.split(".")
                ytFileType = parts[-1]
                ytKey = parts[-2][-11:]
                ytFileName = ytKey + "." + ytFileType
                destinationFilePath = os.path.join(destinationFolderPath, ytFileName)        
                shutil.copy2(sourceFilePath, destinationFilePath)
                
    except OSError as e:
        print(f"Error reading folder: {e}")
    




# Specify the  folders path
if 3 == len(sys.argv):
    sourceFolderPath = sys.argv[1]
    destinationFolderPath = sys.argv[2]
    # Call the function to create YT Key file names
    get_files_in_folder(sourceFolderPath, destinationFolderPath)
    print(f"YT Key Files Created")
else:
    cmdLine = " ".join(sys.argv)
    print(f"Error in command, {cmdLine}")
    print("Valid command is fixYT sourceFolderPath destinationFilePath")

