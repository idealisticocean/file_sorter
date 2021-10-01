# Updated file sorter
# Imports modules
import os
import shutil
import time
import os.path
from os import path

# Gets the username of the user (to be used to find their music, pictures and videos directories 
username = os.getenv('username')

# Lists different directories for different types of file (each element corresponds to rows in the 2D array)
file_type_directories = ['C:/Users/'+username+'/Music', 'C:/Users/'+username+'/Pictures', 'C:/Users/'+username+'/Videos']

# 2D array holds the name of different file formats
extensions = [
    ['.m4a', '.opus', 'mp3', '.wav', '.pcm', '.aac', '.wma'],
    ['.jpg', '.png', '.ico', '.jpeg'],
    ['.mp4', '.webm', '.mkv']
]

def extension_check():
    # Variable holds the default download directory (windows)
    download_dir = os.listdir('C:\\Users\\'+username+'\\Downloads')    
    
    # Looks through files in the downloads directory
    for file in download_dir:
            # If the file is not downloaded fully, do not move it, move onto the next file
            if '.part' in file:
                continue            
            # If the file type matches a file type given in 'extensions' the file is moved to the appropirate directory
            for i in range(len(extensions)):
                for j in range(len(extensions)):
                    if extensions[i][j] in file:
                        shutil.move(('C:/Users/'+username+'/Downloads/'+file), file_type_directories[i])
                        # Prints a status message which will also be written to the log file
                        print('File',file,'has been moved to', file_type_directories[i])

# Runs the program at a regular interval (in this case every 10 seconds)
while True:
    extension_check()
    time.sleep(10)
