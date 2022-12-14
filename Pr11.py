import requests
from tkinter import *


window = Tk()

window.title("Ромадин Д.А., УБ-23")
window.geometry('1024x720')

github = Entry(window, width = 10)
github.grid(column = 0, row = 0)
github.insert(0, 'vscode')


def writes(filename, text):
    file = open(filename, 'w')
    file.write(text)

def prosmotr():
    try:
        json = requests.get(f'https://api.github.com/users/{github.get()}').json()
    except:
        json = requests.get(f'https://api.github.com/users/vscode').json()
    try:
        company = json["company"]
    except:
        company = "None"
    try:
        created_at = json["created_at"]
    except:
        created_at = "None"
    try:
        email = json["email"]
    except:
        email = "None"
    try:
        id = json["id"]
    except:
        id = "None"
    try:
        name = json["name"]
    except:
        name = "None"
    try:
        url = json["url"]
    except:
        url = "None"
    writes('Pr11-Answer.txt',f"'company': {company}\n'create_at': {created_at}\n'email': {email}\n'id': {id}\n'name': {name}\n'url': {url}")


app = Button(window, text = 'START',command = prosmotr)
app.grid(column = 1, row = 0)

window.mainloop()