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
root =tk.Tk()
def clickskill():
    for widget in root.winfo_children():
        widget.destroy()
    entry=tk.Entry(root, width=10)
    entry.pack()
    userinput=entry.get()
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/skills/{userinput.lower()}")
    root.title(response["index"])
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}")
    
def clickclass():
    entry=tk.Entry(root, width=10)
    entry.pack()
    userinput=entry.get()
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{userinput.lower()}")
    print
def clickrace():
    entry=tk.Entry(root, width=10)
    entry.pack()
    userinput=entry.get()
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/races/{userinput.lower()}")

root.geometry("670x500")
root.title("D&D 5e")
label1=tk.Label(root, text="D&D 5e info search: Search a skill, class, or race", font=("Times New Roman", 16))
label1.pack(side="top")

name=tk.Label(root, text="")


button=tk.Button(root, text="Skills", command=clickskill)
button.config()
button.pack(side="left")
button=tk.Button(root, text="Class", command=clickclass)
button.config()
button.pack()
button=tk.Button(root, text="Race", command=clickrace)
button.config()
button.pack(side="right")
root.mainloop()
