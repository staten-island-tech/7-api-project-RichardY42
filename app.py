"""Directions: Select an API and build a project around that.
The project must show the user some data from the API in a manner that is easy to read.
You have a large degree of freedom of what the project is.
User should be able to request and view different types of data through the terminal.
Example, show users some stock data.
Then allow users to search for new stock data, sort stock data etc. 
We will also be leveraging Tkinter for this project
For leveraging Tkinter I will be allowing the use of an AI assistant but you must save your prompts.
All prompts must ONLY be related to tkinter and not the logic of the application.
You can copy and paste your prompts and the AI response into a google doc to be shared with me at the end of the project.
See my example below.
"""
#https://5e-bits.github.io/docs/


import requests
import tkinter as tk

def on_clickskill():
    entry=tk.Entry(root, width=15)
    entry.pack()
    def getskill():
        userinput=entry.get()
        response = requests.get(f"/api/2014/monsters/{userinput.lower()}") 

root =tk.Tk()
root.geometry("670x500")
root.title("D&D 5e")
label1=tk.Label(root, text="D&D 5e info search: Search a skill, class, or race")
label1.config(font=("Times New Roman", 16))
label1.pack(side="top")



button=tk.Button(root, text="Skills", command=)
button
button.pack()
root.mainloop()
