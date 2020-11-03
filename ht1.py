# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

window = tk.Tk()
 
window.title("Python Tkinter Text Box")
window.minsize(600,400)
 
def clickMe():
    imagesSize = name.get()
    imageSizeFromLoc = directoryLocation1.get()
    #imageSizeFromLoc = str(imageSizeFromLoc)
    imageType = tkvar.get()
    videosSize = nameTwo.get()
    videoSizeFromLoc = directoryLocation2.get()
    #videoSizeFromLoc = str(videoSizeFromLoc)
    videoType = tkvarTwo.get()
    documentsSize = nameThree.get()
    documentSizeFromLoc = directoryLocation3.get()
    #documentSizeFromLoc = str(documentSizeFromLoc)
    documentType = tkvarThree.get()
    a=b=c=0
    if(imageSizeFromLoc==''):
        if (imageType == 'MB'):
            a = int(imagesSize) * 1024
        elif (imageType == 'GB'):
            a = int(imagesSize) * 1024 * 1024
    else:
        a = get_directory_size(imageSizeFromLoc)
    
    if(videoSizeFromLoc==''):
        if (videoType == 'MB'):
            b = int(videosSize) * 1024
        elif (videoType == 'GB'):
            b = int(videosSize) * 1024 * 1024     
    else:
        b = get_directory_size(videoSizeFromLoc)
   
    if(documentSizeFromLoc==''):
        if (documentType == 'MB'):
            c = int(documentsSize) * 1024
        elif (documentType == 'GB'):
            c = int(documentsSize) * 1024 * 1024   
    else:
        c = get_directory_size(documentSizeFromLoc)
   
    
    
    objects = ('images', 'videos', 'documents')
    y_pos = np.arange(len(objects))
    performance = [a,b,c]
    
    myFig = plot(y_pos, performance, 0.5, objects)
    myFig.savefig(r'C:\Users\Sajjad\Desktop\plot.png')
    
    #top = tk.Toplevel()
    #diagrams = tk.PhotoImage(file=myFig)
    #logolbl= tk.Label(top, image = diagrams)
    #logolbl.grid()
    #tk.mainloop()
    
 
label = ttk.Label(window, text = "Enter storage size of images")
label.place(x = 0, y = 0)

tkvar = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvar.set('KB') # set the default option
popupMenu = tk.OptionMenu(window, tkvar, *choices) 
popupMenu.place(x=400, y=10)

 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.place(x = 0, y = 20)


labelDirectoryLocation1 = ttk.Label(window, text = "OR enter folder/directory location for images")
labelDirectoryLocation1.place(x = 150, y = 0)
directoryLocation1 = tk.Entry(window)
directoryLocation1.place(x=150, y=20)


labelTwo = ttk.Label(window, text = "Enter storage size of videos")
labelTwo.place(x = 0, y = 40)

tkvarTwo = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarTwo.set('KB') # set the default option
popupMenuTwo = tk.OptionMenu(window, tkvarTwo, *choices) 
popupMenuTwo.place(x=400, y=50) 
 
nameTwo = tk.StringVar()
nameEnteredTwo = ttk.Entry(window, width = 15, textvariable = nameTwo)
nameEnteredTwo.place(x = 0, y = 60)

labelDirectoryLocation2 = ttk.Label(window, text = "OR enter folder/directory location for videos")
labelDirectoryLocation2.place(x = 150, y = 40)
directoryLocation2 = tk.Entry(window)
directoryLocation2.place(x=150, y=60)
 

labelThree = ttk.Label(window, text = "Enter storage size of documents")
labelThree.place(x = 0, y = 80)

tkvarThree = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarThree.set('KB') # set the default option
popupMenuThree = tk.OptionMenu(window, tkvarThree, *choices) 
popupMenuThree.place(x=400, y=90) 
 
nameThree = tk.StringVar()
nameEnteredThree = ttk.Entry(window, width = 15, textvariable = nameThree)
nameEnteredThree.place(x = 0, y = 100)

labelDirectoryLocation3 = ttk.Label(window, text = "OR enter folder/directory location for docs")
labelDirectoryLocation3.place(x = 170, y = 80)
directoryLocation3 = tk.Entry(window)
directoryLocation3.place(x=150, y=100)


button = ttk.Button(window, text = "Display Graph", command = clickMe)
button.place(x= 13, y = 150)
 
window.mainloop()

def plot(y_pos, performance, alpha, objects):
    fig = plt.figure()
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Usage in KB')
    plt.title('Media Type')
    return fig
    



import os

def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
