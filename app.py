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
#.grid(row=0, column=0)



import requests
import tkinter as tk
root =tk.Tk()
def clicksearch():
    entry.get()

#searchbutton=tk.Button(root, text="Search", command=clicksearch)
def clickskill():
    
    userinput=entry.get()
    
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/skills/{userinput.lower()}")
    
    #return data
    root.title(response["index"])
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}")
    
def clickclass():
    userinput=entry.get()
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{userinput.lower()}")
    
    #return data
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}")

def clickrace():
    userinput=entry.get()
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/races/{userinput.lower()}")
    
    #return data
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}")
root.geometry("670x500")
root.title("D&D 5e")
label1=tk.Label(root, text="D&D 5e info search: Search a skill, class, or race", font=("Times New Roman", 16)).grid(row=0, column=7)


name=tk.Label(root, text="")
name.grid(row=5, column=20)
desc=tk.Label(root, text="")
desc.grid(row=10, column=20)
abltyscr=tk.Label(root, text="")
abltyscr.grid(row=15, column=20)

entry=tk.Entry(root, width=10, size=10)
entry.grid(row=5, column=7)

skillbutton=tk.Button(root, text="Skills", command=clickskill).grid(row=1, column=5)

#skillbutton.config()

classbutton=tk.Button(root, text="Class", command=clickclass).grid(row=1, column=7)

#classbutton.config()

racebutton=tk.Button(root, text="Race", command=clickrace).grid(row=1, column=10)

#racebutton.config()

root.mainloop()





