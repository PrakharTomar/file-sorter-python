import os
import shutil

# Folder path where files are located
path = r"Enter your file path here"

# List all files in the directory
os.listdir(path)

# Define folder names for different file types
folder_names = ["Documents", "Images", "Audios", "Videos", "Archives",
                "Programming", "System", "Presentations", "Spreadsheets"]

# Create folders if they do not exist
for folder_name in folder_names:
    if not os.path.exists(path + "\\" + folder_name):
        os.makedirs(path + "\\" + folder_name)

# Get the list of files in the directory
file_name = os.listdir(path)

# Move files to their respective folders based on file extension
for file in file_name:
    if file.endswith(".docx"):
        shutil.move(path + "\\" + file, path + "\\Documents\\" + file)
    elif file.endswith(".pdf"):
        shutil.move(path + "\\" + file, path + "\\Documents\\" + file)
    elif file.endswith(".txt"):
        shutil.move(path + "\\" + file, path + "\\Documents\\" + file)
    elif file.endswith(".jpg"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".jpeg"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".png"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".gif"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".svg"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".bmp"):
        shutil.move(path + "\\" + file, path + "\\Images\\" + file)
    elif file.endswith(".mp3"):
        shutil.move(path + "\\" + file, path + "\\Audios\\" + file)
    elif file.endswith(".wav"):
        shutil.move(path + "\\" + file, path + "\\Audios\\" + file)
    elif file.endswith(".m4a"):
        shutil.move(path + "\\" + file, path + "\\Audios\\" + file)
    elif file.endswith(".mov"):
        shutil.move(path + "\\" + file, path + "\\Videos\\" + file)
    elif file.endswith(".mp4"):
        shutil.move(path + "\\" + file, path + "\\Videos\\" + file)
    elif file.endswith(".zip"):
        shutil.move(path + "\\" + file, path + "\\Archives\\" + file)
    elif file.endswith(".rar"):
        shutil.move(path + "\\" + file, path + "\\Archives\\" + file)
    elif file.endswith(".7z"):
        shutil.move(path + "\\" + file, path + "\\Archives\\" + file)
    elif file.endswith(".html"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".js"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".css"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".php"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".py"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".ipynb"):
        shutil.move(path + "\\" + file, path + "\\Programming\\" + file)
    elif file.endswith(".exe"):
        shutil.move(path + "\\" + file, path + "\\System\\" + file)
    elif file.endswith(".dll"):
        shutil.move(path + "\\" + file, path + "\\System\\" + file)
    elif file.endswith(".sys"):
        shutil.move(path + "\\" + file, path + "\\System\\" + file)
    elif file.endswith(".cfg"):
        shutil.move(path + "\\" + file, path + "\\System\\" + file)
    elif file.endswith(".xlsx"):
        shutil.move(path + "\\" + file, path + "\\Spreadsheets\\" + file)
    elif file.endswith(".csv"):
        shutil.move(path + "\\" + file, path + "\\Spreadsheets\\" + file)
    elif file.endswith(".pptx"):
        shutil.move(path + "\\" + file, path + "\\Presentations\\" + file)








