import urllib.request
import re
import datetime
import os

from PIL import ImageTk
from urllib.request import urlopen

# On importe le fichier var.py dans lequel vous renseignez vos informations personelles (numéro de telephone, sid, token)

import var

# On importe la librairie qui va nous permettre d'envoyer un SMS à notre numéro de telephone
from twilio.rest import Client

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

def get_image():
    page = urlopen("https://www.krosmoz.com/fr/almanax")

    itemImageTag = re.findall('<div class=\"more-infos-content\">(.+?)<img([\w\W]+?)/>', str(page.read()))[0][1]
    itemImageSrc = re.findall('src=\"(.*?)\"', itemImageTag)[0]

    return itemImageSrc

# Envoi du SMS

sid = var.sid
token = var.token

client = Client(sid,token)

message = client.messages.create(
    to=var.phone_number_perso,
    from_=var.phone_number_twilio,
    body="\n \n" + get_ressource() + "\n" + get_bonus(),
    media_url=get_image(),
    status_callback="https://www.toptal.com/developers/postbin/...")