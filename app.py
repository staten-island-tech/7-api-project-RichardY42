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
#.pack_forget()

import tkinter as tk
import requests

root =tk.Tk()

#searchbutton=tk.Button(root, text="Search", command=clicksearch)
def choseskill():
    skillbutton.pack_forget()
    classbutton.pack_forget()
    racebutton.pack_forget()
    name.pack_forget()
    desc.pack_forget()
    abltyscr.pack_forget()
    entry=tk.Entry(root, width=50)
    entry.pack(pady=20)
    def searchskill():
        name.pack(side="top")
        desc.pack(pady=1)
        abltyscr.pack(pady=1)
        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/skills/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        data = response.json()
        
        #return data
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        desc.config(text=f"Description: {data['desc']}")
        abltyscr.config(text=f"Ability Score: {data['ability_score']['index']}")
        print(data['ability_score'])
    
    searchskill=tk.Button(root, text="Search", command=searchskill)
    searchskill.pack(pady=1)



def choseclass():
    skillbutton.pack_forget()
    classbutton.pack_forget()
    racebutton.pack_forget()
    name.pack_forget()
    desc.pack_forget()
    abltyscr.pack_forget()
    entry=tk.Entry(root, width=50)
    entry.pack(pady=20)
    def searchclass():
        name.pack(side="top")
        desc.pack(pady=1)
        abltyscr.pack(pady=1)
        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/classes/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        data = response.json()
        
        #return data
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        desc.config(text=f"Description: {data['desc']}")
        abltyscr.config(text=f"Ability Score: {data['ability_score']}")
        print(data['ability_score'])
    
    searchskill=tk.Button(root, text="Search", command=searchclass)
    searchskill.pack(pady=1)




def choserace():
    skillbutton.pack_forget()
    classbutton.pack_forget()
    racebutton.pack_forget()
    name.pack_forget()
    desc.pack_forget()
    abltyscr.pack_forget()
    entry=tk.Entry(root, width=50)
    entry.pack(pady=20)
    def searchrace():
        name.pack(side="top")
        desc.pack(pady=1)
        abltyscr.pack(pady=1)
        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/races/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        data = response.json()
        
        #return data
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        desc.config(text=f"Description: {data['desc']}")
        abltyscr.config(text=f"Ability Score: {data['ability_score']}")
        print(data['ability_score'])
    
    searchskill=tk.Button(root, text="Search", command=searchrace)
    searchskill.pack(pady=1)
        


root.geometry("800x700")
root.title("D&D 5e")
label1=tk.Label(root, text="D&D 5e info search: Search a Skill, Class, or Race", font=("Times New Roman", 25)).pack()
skillbutton=tk.Button(root, text="Skills",font=("Times New Roman", 30), command=choseskill)
skillbutton.pack()
classbutton=tk.Button(root, text="Classes",font=("Times New Roman", 30), command=choseclass)
classbutton.pack(pady=5)
racebutton=tk.Button(root, text="Races",font=("Times New Roman", 30), command=choserace)
racebutton.pack(pady=5)
name=tk.Label(root, text="",font=("Times New Roman", 16))
name.pack(pady=0)
desc=tk.Label(root, wraplength=650, text="",  font=("Times New Roman", 13))
desc.pack(pady=10)
abltyscr=tk.Label(root, wraplength=150, text="",  font=("Times New Roman", 13))
abltyscr.pack(pady=10)


""" def clickclass():
    userinput=entry.get()
    url=f"https://www.dnd5eapi.co/api/2014/classes/{userinput.lower()}"
    response = requests.get(url)
    
    #return data
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}")

def clickrace():
    userinput=entry.get()
    url=f"https://www.dnd5eapi.co/api/2014/races/{userinput.lower()}"
    response = requests.get(url)
    
    #return data
    name.config(text=f"name: {response["name"]}")
    desc.config(text=f"description: {response["desc"]}")
    abltyscr.config(text=f"ability score: {response["ability_score"]}") """




#______________________________________________________________________________________
""" 

#skillbutton.config()

classbutton=tk.Button(root, text="Class", command=clickclass).pack(row=1, column=7)

#classbutton.config()

racebutton=tk.Button(root, text="Race", command=clickrace).pack(row=1, column=10)

#racebutton.config() """

root.mainloop()





