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
    label.configure(text= 'Hello ' + name.get())
    imagesSize = name.get()
    imageType = tkvar.get()
    videosSize = nameTwo.get()
    videoType = tkvarTwo.get()
    documentsSize = nameThree.get()
    documentType = tkvarThree.get()
    
    if (imageType == 'MB'):
        a = int(imagesSize) * 1024
    elif (imageType == 'GB'):
        a = int(imagesSize) * 1024 * 1024
        
    if (videoType == 'MB'):
        b = int(videosSize) * 1024
    elif (videoType == 'GB'):
        b = int(videosSize) * 1024 * 1024
        
    if (documentType == 'MB'):
        c = int(documentsSize) * 1024
    elif (documentType == 'GB'):
        c = int(documentsSize) * 1024 * 1024
        
    
    objects = ('images', 'videos', 'documents')
    y_pos = np.arange(len(objects))
    performance = [a,b,c]
    
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Usage in KB')
    plt.title('Media Type')
    
    plt.show()
    
 
label = ttk.Label(window, text = "Enter storage size of images")
label.place(x = 80, y = 0)

tkvar = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvar.set('KB') # set the default option
popupMenu = tk.OptionMenu(window, tkvar, *choices) 
popupMenu.place(x=300, y=0)

 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.place(x = 0, y = 20)
 
 
button = ttk.Button(window, text = "Click Me", command = clickMe)
button.place(x= 50, y = 200)


labelTwo = ttk.Label(window, text = "Enter storage size of videos")
labelTwo.place(x = 80, y = 40)

tkvarTwo = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarTwo.set('KB') # set the default option
popupMenuTwo = tk.OptionMenu(window, tkvarTwo, *choices) 
popupMenuTwo.place(x=300, y=40) 
 
nameTwo = tk.StringVar()
nameEnteredTwo = ttk.Entry(window, width = 15, textvariable = nameTwo)
nameEnteredTwo.place(x = 0, y = 60)
 

labelThree = ttk.Label(window, text = "Enter storage size of documents")
labelThree.place(x = 80, y = 80)

tkvarThree = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarThree.set('KB') # set the default option
popupMenuThree = tk.OptionMenu(window, tkvarThree, *choices) 
popupMenuThree.place(x=300, y=80) 
 
nameThree = tk.StringVar()
nameEnteredThree = ttk.Entry(window, width = 15, textvariable = nameThree)
nameEnteredThree.place(x = 0, y = 100)

 
window.mainloop()

def check(a, b, c):
    objects = ('images', 'videos', 'documents')
    y_pos = np.arange(len(objects))
    performance = [10,8,6]
    
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Usage')
    plt.title('Programming language usage')
    
    plt.show()
