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
#pack order not state order

import tkinter as tk
import requests

root =tk.Tk()
root.geometry("800x700")
root.title("D&D 5e")

menuframe = tk.Frame(root)
searchframe = tk.Frame(root)


entry=tk.Entry(searchframe, width=50)
possval=tk.Label(searchframe, wraplength=450, text="")
search=tk.Button(searchframe,text="Search")
errorlabel=tk.Label(searchframe, wraplength=650, text="", font=("Times New Roman", 16))
name=tk.Label(searchframe, text="",font=("Times New Roman", 16))
hitdie=tk.Label(searchframe, text="",font=("Times New Roman", 16))
desc=tk.Label(searchframe, wraplength=550, text="",  font=("Times New Roman", 15))
abltyscr=tk.Label(searchframe, wraplength=150, text="",  font=("Times New Roman", 16))

entry.pack(pady=20)
possval.pack()
search.pack()
errorlabel.pack()
name.pack(pady=10)
desc.pack(pady=5)
abltyscr.pack(pady=5)


""" def goingback():
    searchframe.pack_forget()
    menuframe.pack(fill="both", expand=True)
    label1.pack()
    skillbutton.pack()
    classbutton.pack(pady=5)
    racebutton.pack(pady=5)
goback=tk.Button(searchframe, text="<- Go Back", command=goingback) """

def choseskill():
    menuframe.pack_forget()
    searchframe.pack(fill="both", expand=True)
    possvalues="Possible values:\n acrobatics, animal-handling, arcana, athletics, deception, history, insight, intimidation, investigation, medicine, nature, perception, performance, persuasion, religion, sleight-of-hand, stealth, survival"
    possval.config(text=possvalues)
    
    
    def findskill():
        
        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/skills/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            errorlabel.config(text="Error fetching data!")
            
        if response.status_code == 200:
            errorlabel.pack_forget() 
        data = response.json()
        
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        desc.config(text=f"Description: {data['desc']}")
        abltyscr.config(text=f"Ability Score: {data['ability_score']['index']}")
        print(data['ability_score'])
    
    search.config(command=findskill)
    
   # goback.pack(pady=50)

    

def choseclass():
    menuframe.pack_forget()
    searchframe.pack(fill="both", expand=True)
    possvalues="Possible values:\n barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard"
    possval.config(text=possvalues)

    def findclass():
        
        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/classes/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            errorlabel.config(text="Error fetching data!")
        if response.status_code == 200:
            errorlabel.pack_forget() 
        data = response.json()
        
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        hitdie.config(text=f"Hit Die: {data['hit_die']}")
        desc.config(text=f"Description: {data['proficiency_choices']}",  font=("Times New Roman", 10))
        
    
    search.config(command=findclass)
    
    



def choserace():
    menuframe.pack_forget()
    searchframe.pack(fill="both",expand=True)
    possvalues="Possible values:\n dragonborn, dwarf, elf, gnome, half-elf, half-orc, halfling, human, tiefling"
    possval.config(text=possvalues)

    def searchrace():

        userinput=entry.get().lower()
        url=f"https://www.dnd5eapi.co/api/2014/races/{userinput}"
        response = requests.get(url)
        if response.status_code != 200:
            errorlabel.config(text="Error fetching data!")
        if response.status_code == 200:
            errorlabel.pack_forget() 
        data = response.json()
    
        root.title(data["index"])
        name.config(text=f"Name: {data['name']}")
        desc.config(text=f"Description: {data['desc']}")
        abltyscr.config(text=f"Ability Score: {data['ability_score']}")
        print(data['ability_score'])
    
    search.config(command=searchrace)
    
    



root.geometry("800x700")
root.title("D&D 5e")
label1=tk.Label(menuframe, text="D&D 5e info search: Search a Skill, Class, or Race", font=("Times New Roman", 25))
label1.pack()

skillbutton=tk.Button(menuframe, text="Skills",font=("Times New Roman", 30), command=choseskill)
skillbutton.pack()
classbutton=tk.Button(menuframe, text="Classes",font=("Times New Roman", 30), command=choseclass)
classbutton.pack(pady=5)
racebutton=tk.Button(menuframe, text="Races",font=("Times New Roman", 30), command=choserace)
racebutton.pack(pady=5)


menuframe.pack(fill="both", expand=True)



root.mainloop()
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






