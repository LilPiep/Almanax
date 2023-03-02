import re
# Pour la fenêtre
from tkinter import *
from urllib.request import urlopen

from PIL import ImageTk


def better_reading(content):
    content = content.replace("\\xc3\\xa9", "é")
    content = content.replace("\\xc3\\xa0", "à")
    content = content.replace("\\xc3\\xa8", "è")
    content = content.replace("\\xc3\\xa7", "ç")
    content = content.replace("\\xc3\\xa2", "â")
    content = content.replace("\\'", "'")
    content = content.replace("\\n", "")
    return content


def get_ressource():
    page = urlopen("https://www.krosmoz.com/fr/almanax")
    content = re.findall('<p class="fleft">(.+?)</p>', str(page.read()))[0]
    content = better_reading(content)
    return content


def get_bonus():
    page = urlopen("https://www.krosmoz.com/fr/almanax")
    content = re.findall('<div class="more">(.+?)</div>', str(page.read()))[0]
    content = content.replace("<b>", "")
    content = content.replace("</b>", "")
    content = content.split(".")[0]
    content = better_reading(content)
    return content


# On veut créer une nouvelle fonction qui récupère l'image de la ressource de l'almanax et la stocke dans une variable pour pouvoir l'afficher dans la fenêtre plus tard

"""
on récupère l'url de l'image qui est dans la balise <img ... /> dans itemImageSrc

on obtient les octets de l'image avec le read

on crée l'objet PhotoImage de Tkinter avec les données

"""
def get_image():
    page = urlopen("https://www.krosmoz.com/fr/almanax")

    itemImageTag = re.findall('<div class=\"more-infos-content\">(.+?)<img([\w\W]+?)/>', str(page.read()))[0][1]
    itemImageSrc = re.findall('src=\"(.*?)\"', itemImageTag)[0]

    image_byt = urlopen(itemImageSrc)
    raw_data = image_byt.read()
    image = ImageTk.PhotoImage(data=raw_data)
    return image


# Création de la fenêtre dans laquelle on affiche le resultat de la fonction get_ressource() et get_bonus()

window = Tk()
window.title("Almanax")
window.geometry("1400x200")
window.minsize(200, 200)
window.maxsize(1800, 1800)
window.config(background='#41B77F')

# Création d'un label pour afficher le résultat de la fonction get_ressource()

label_ressource = Label(window, text=get_ressource(), font=("Courrier", 20), bg='#41B77F', fg='white')
label_ressource.pack()

# Création d'un label pour afficher le résultat de la fonction get_bonus()

label_bonus = Label(window, text=get_bonus(), font=("Courrier", 20), bg='#41B77F', fg='white')
label_bonus.pack()

img = get_image()

label_img = Label(image=img)
label_img.image = img
label_img.pack()

# Affichage de l'image

window.mainloop()