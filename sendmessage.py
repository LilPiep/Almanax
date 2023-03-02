# Demo Twilio par Korben - 2021

# Credits : 

# https://korben.info/articles/envoyer-sms-python-twilio

# On charge la lib Twilio et notamment l'API Rest
from twilio.rest import Client

# On importe le fichier var.py dans lequel vous renseignez vos informations personelles (numéro de telephone, sid, token)

import var

# On stocke notre SID et notre jeton dans des variables
sid = var.sid
token = var.token

# Et on initialise notre objet client avec nos identifiants.
client = Client(sid,token)

# Puis on forge notre premier message
message = client.messages.create(
    
    # destinataire
    to=var.phone_number_perso,
    
    # expéditeur (votre n° Twilio)
    from_=var.phone_number_twilio,
    
    # votre message
    body="Petit test avec image !",
    media_url="https://services.korben.info/images/assets/default@2x.png",
    status_callback="https://www.toptal.com/developers/postbin/....") # Pour verifier l'envoi du SMS sur Postbin

# J'affiche l'ID du message envoyé
print(message.sid)