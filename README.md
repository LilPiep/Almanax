# Almanax

## Objectif

L'objectif de ce projet est de créer un petit programme qui permet de récupérer les informations de l'Almanax du jour.
Pour se faire, on va récuperer les informations sur le site officiel de dofus, et les traiter.

### Contexte :

Sur le jeu Dofus, un certain Théodoran Ax (drole de nom) propose une quête journalière. En effet, il faudra chaque jour lui faire une offrande pour recevoir des kamas et de l'xp. Cette quête est liée à un bonus. Le problème est donc que chaque jour on doit aller sur le site de l'Almanax pour savoir quelle est la quête et le bonus du jour. C'est un peu répétitif, c'est pourquoi on cherche avec ce projet à automatiser cette tâche.

## V1 : Afficher les infos en ligne de commande

Dans cette V1, on va simplement afficher les informations de l'Almanax du jour en ligne de commande.
Ainsi, on affiche la quête et le bonus du jour.

## V2 : Afficher les infos dans une fenêtre avec une petite interface graphique choupi

Dans cette V2, on va afficher les informations de l'Almanax du jour dans une fenêtre avec une petite interface graphique choupi. Tout est dans le titre.

## V3 : Envoi de SMS

Le but de la V3 est d'envoyer un SMS sur un téléphone avec les informations récoltées dans la V1. 
Cette version est un premier jet de la version finale de almanax.py qui enverra un SMS tous les jours à l'utilisateur sans avoir besoin d'executer le programme à chaque fois. 

## V3.1 : Envoi de SMS automatique

Dans cette V3.1, on va envoyer un SMS tous les jours à l'utilisateur sans avoir besoin d'executer le programme à chaque fois. En gros, on automatise la V3.

Il vous faudra un compte Twilio et remplir les informations de connexion dans le fichier var.py.

https://www.twilio.com/fr/

On vous recommande aussi d'utiliser un postbin pour tester l'envoi de SMS. Il vous suffit de remplacer la valeur de la variable status_callback par le lien de votre postbin.

https://www.toptal.com/developers/postbin/

On utilisera cron qui permet de lancer un programme à une heure précise.

Voici les commandes à taper dans le terminal pour lancer le programme tous les jours à 9h du matin :

- ~$ export EDITOR=nano (pour utiliser nano comme éditeur de texte)
- ~$ crontab -e (pour éditer le fichier de cron)
- On tape alors dans le fichier : 0 9 * * * python3 /votre_chemin_vers_almanax_V3.py
- ~$ crontab -l (pour vérifier que le fichier a bien été modifié)

Nb : Vous ne recevrez votre SMS que si votre ordinateur est allumé à l'heure choisie. Si vous le souhaitez, vous pouvez programmer cron pour executer le programme le matin lorsque vous allumez votre ordinateur. 

## Erreurs commises dans ce projet et notes diverses

### Erreurs

- Push ses informations de connexion à l'API de Twilio sur Github n'est pas une super idée. Cette erreur est évitable en utilisant un fichier var.py dans lequel l'utilisateur renseigne ses propres informations de connexion. Rien de grave toutefois car Twilio a bloqué l'accès à l'API via le token que j'avais push et m'en a fourni un nouveau. Cette erreur m'a donc conduit à supprimer mon repo sur Github et à en créer un nouveau. (J'ai perdu l'avancement du projet avec tous les commits ainsi que l'historique de collaboration avec un autre utilisateur mais c'est pas grave, c'est un projet de test)

### Notes diverses

- C'était la première fois que j'utilisais un système d'envoi de SMS, c'était assez sympa à faire.

- C'était la première fois qu'un utilisateur github me proposait de collaborer sur un projet. C'était assez sympa aussi. J'ai donc eu le premier fork d'un de mes projets ainsi que mon premier pull request.

- C'est aussi la première fois que je publie un repo public sur Github. 

- C'était la première fois que j'utilisais cron pour automatiser des executions de programmes. D'ailleurs, sentez-vous libre d'adapter la commande cron à vos propres besoins. Voici le lien d'un site qui va vous faciliter la vie : https://crontab.guru/