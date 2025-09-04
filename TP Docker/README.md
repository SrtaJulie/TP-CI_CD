# Fichier de suivi du TP sur Docker 

Le travail à été réalisé sur Codespaces.

## Exercice 1
Pas d'installation nécessaire grace à Codespaces.

## Exercice 3

Tâches faites :
1. Vérifier la version de Docker :
docker --version

2. Lister les images disponibles sur votre machine :
docker images

3. Télécharger une image depuis Docker Hub :
docker pull hello-world

4. Exécuter un conteneur à partir de l'image :
docker run hello-world

![alt text](assets/image.png)

5. Lister les conteneurs en cours d'exécution :
docker ps

6. Lister tous les conteneurs (actifs et stoppés) :
docker ps -a

![alt text](assets/image-1.png)

7. Supprimer un conteneur :
docker rm <ID_conteneur>

8. Supprimer une image :
docker rmi <ID_image>

## Exercice 4 : serveur web

1. Télécharger l'image officielle Nginx :
docker pull nginx

2. Lancer un conteneur Nginx en arrière-plan :
docker run -d -p 8080:80 --name mon_nginx nginx

3. Vérifier que le conteneur est actif :
docker ps

4. Accéder à la page dans votre navigateur pour voir la page par défaut de Nginx.

![alt text](assets/image-2.png)

5. Arrêter le conteneur :
docker stop mon_nginx

![alt text](assets/image-3.png)

## Exercie 5 : application Python Flask

Création d'un fichier app.py contenant une application Flask minimale.
- Flask = micro-framework web en Python
- @app.route("/") = définit la route / = la page d’accueil
- host="0.0.0.0" = l’app hors du container (à priori)
- port=5000 = le port 5000 ( convention Flask)

Écriture d'un Dockerfile pour construire l’image de l’application.
Construction de l’image et lancement du conteneur.
= docker build -t flask-julie .

Tests de l’application.

![alt text](asset/image-4.png)

## Exercie 6 : Utilisation de docker compose

Compléter le fichier app.py afin de lui ajouter une connexion a un bdd mongoDB

Écrire un fichier docker compose avec les deux conteneurs

Lancer le docker compose puis à minima vérifier que la connexion c’est bien effectuée sur la base de données
