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
    imageType = tkvar.get()
    videosSize = nameTwo.get()
    videoType = tkvarTwo.get()
    documentsSize = nameThree.get()
    documentType = tkvarThree.get()
    a=b=c=0
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
popupMenu.place(x=300, y=0)

 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.place(x = 0, y = 20)
 
 
button = ttk.Button(window, text = "Display Graph", command = clickMe)
button.place(x= 13, y = 150)


labelTwo = ttk.Label(window, text = "Enter storage size of videos")
labelTwo.place(x = 0, y = 40)

tkvarTwo = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarTwo.set('KB') # set the default option
popupMenuTwo = tk.OptionMenu(window, tkvarTwo, *choices) 
popupMenuTwo.place(x=300, y=40) 
 
nameTwo = tk.StringVar()
nameEnteredTwo = ttk.Entry(window, width = 15, textvariable = nameTwo)
nameEnteredTwo.place(x = 0, y = 60)
 

labelThree = ttk.Label(window, text = "Enter storage size of documents")
labelThree.place(x = 0, y = 80)

tkvarThree = tk.StringVar(window)
choices = { 'KB', 'MB', 'GB'}
tkvarThree.set('KB') # set the default option
popupMenuThree = tk.OptionMenu(window, tkvarThree, *choices) 
popupMenuThree.place(x=300, y=80) 
 
nameThree = tk.StringVar()
nameEnteredThree = ttk.Entry(window, width = 15, textvariable = nameThree)
nameEnteredThree.place(x = 0, y = 100)

 
window.mainloop()

def plot(y_pos, performance, alpha, objects):
    fig = plt.figure()
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Usage in KB')
    plt.title('Media Type')
    return fig
    

