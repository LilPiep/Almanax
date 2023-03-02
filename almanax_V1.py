# Dans un premier temps, on importe les modules nécessaires
# On importe urllib.request pour récupérer le contenu de la page

import urllib.request
import re
import datetime
import os

# On définit la fonction qui va récupérer le contenu de la page https://www.krosmoz.com/fr/almanax
# Ce qui nous interesse est de recupérer le contenu de la balise <p class="fleft"> et de l'afficher
# Il s'agit en gros de la ressource à donner pour compléter la quête

def better_reading(content):
    # Avant de retourner le resultat, on doit faire en sorte de ne pas avoir de problème avec les caractères spéciaux
    # En affichage console on peut rencontrer des problèmes comme "\xc3\xa9" qui correspond à "é" ou "\xc3\xa0" qui correspond à "à", on veut donc remplacer ces caractères par leur équivalent
    content[0] = content[0].replace("\\xc3\\xa9", "é")
    content[0] = content[0].replace("\\xc3\\xa0", "à")
    content[0] = content[0].replace("\\xc3\\xa8", "è")
    content[0] = content[0].replace("\\xc3\\xa7", "ç")
    content[0] = content[0].replace("\\xc3\\xa2", "â")
    # On a aussi unn petit problème avec le l apostrophe, on veut donc la remplacer par son équivalent
    content[0] = content[0].replace("\\'", "'")
    # On veux dégager aussi le "\n" au début de la ligne
    content[0] = content[0].replace("\\n", "")

def get_ressource():
    # On récupère le contenu de la page
    page = urllib.request.urlopen("https://www.krosmoz.com/fr/almanax")
    # On récupère le contenu de la balise <p class="fleft">
    content = re.findall('<p class="fleft">(.+?)</p>', str(page.read()))
    better_reading(content)
    # On retourne le résultat
    return content[0]

def get_bonus():
    # On récupère le contenu de la page
    page = urllib.request.urlopen("https://www.krosmoz.com/fr/almanax")
    # On récupère le contenu de la balise <div class="more">
    content = re.findall('<div class="more">(.+?)</div>', str(page.read()))
    # On doit faire le tri dans tout ça, pas exemple, enlever les balises <b>
    content[0] = content[0].replace("<b>", "")
    content[0] = content[0].replace("</b>", "")
    # On décide de ne pas afficher tout ce qui suit le premier "."
    content[0] = content[0].split(".")[0]
    better_reading(content)
    # On retourne le résultat
    return content[0]

print(get_ressource() + "\n" + get_bonus()) # On affiche le résultat