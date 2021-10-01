# Old file sorter 

##Imports modules
import os
import shutil
import time
import os.path
from os import path
#States different file extensions for different types of file
audio_extensions = ['.m4a', '.opus', 'mp3', '.wav', '.pcm', 'aac', '.wma']
images_extensions = ['.jpg', '.png', '.ico', '.jpeg']
video_extensions = ['.mp4', '.webm', '.mkv']

def audio_check():
    #Looks through files in the current directory
    for file in os.listdir():
        #Looks through the list of audio file extensions
        for i in range (len(audio_extensions)):
            #If the file is not downloaded fully, do not move it, move onto the next file
            if '.part' in file:
                continue
            #If the file uses a audio file extension listed above, it gets moved to the audio folder 
            elif audio_extensions[i] in file:
                shutil.move(file, audio_dir)
                print('Moved',file,'to',audio_dir)
            #If not the program moves onto the next file in the list    
            else:
                continue
            #This works the same for the other two functions
def images_check():
    for file in os.listdir():
        for i in range (len(images_extensions)):
            if '.part' in file:
                continue
            elif images_extensions[i] in file:
                shutil.move(file, images_dir)
                print('Moved',file,'to',images_dir)
            else:
                continue
def video_check():
    for file in os.listdir():
        for i in range (len(video_extensions)):
            if '.part' in file:
                continue
            elif video_extensions[i] in file:
                shutil.move(file, videos_dir)
                print('Moved',file,'to',videos_dir)
            else:
                continue

while True:
    try:
        f = open('config.txt', 'r')
        global download_folder
        download_folder = f.readlines(0)
        f.close()
        print('File Sorter Is Running')
        break
    except:
        from tkinter import *
        from tkinter import filedialog    

        def select_folder():
            global download_folder
            download_folder = str(filedialog.askdirectory())

        def restart():
            root.destroy()
            for i in range (1,2):
                continue

        root = Tk()
        root.title('File Sorter')
        root.geometry('480x480')
        
        button1 = Button(text = 'Select Download Folder', width = 20, height = 5, command = select_folder)
        button1.pack()
        button2 = Button(text = 'Restart Program', width = 20, height = 5, command = restart)
        button2.pack()

        root.mainloop()
        
        f = open('config.txt', 'w+')
        f.write(download_folder)
        f.close()
        continue

#if audio folder doesn't exist:
    #mkdir 'audio_dir' 

audio_dir = download_folder[0]+ '/Audio'
images_dir = download_folder[0]+ '/Images'
videos_dir = download_folder[0]+ '/Videos'

audio_path_check = path.exists(audio_dir)
if audio_path_check == False:
    os.mkdir(audio_dir)
images_path_check = path.exists(images_dir)
if images_path_check == False:
    os.mkdir(images_dir)
videos_path_check = path.exists(videos_dir)
if videos_path_check == False:
    os.mkdir(videos_dir)        

##Runs all three functions once every second
while True:            
    audio_check()
    images_check()
    video_check()    
    time.sleep(1)
