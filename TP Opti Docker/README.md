# Fichier de suivi du TP Optimisation Docker 

Le travail a été réalisé sur Codespaces.

## ETAPE 1 : Analyse initiale du fichier

Problèmes                                                            
- FROM node:latest => image lourde
- COPY node_modules => il ne faut pas les copier
- RUN npm install après le COPY node_modules => soit on copie (ce qui est mal), soit on les installe. Pas les deux.
- RUN apt-get` => a priori c'est un OS complet pour un petit serveur Node, c’est trop.
- ENV NODE_ENV=development => En prod il faut production ?
- USER root => faille de sécurité   
- pas de .dockerignore => donc on embarque plein de fichiers inutiles
- npm run build => inutile 
- EXPOSE 3000 4000 5000 => que 3000, pas besoin des autres

Temps de build : 46.0s (avec "docker build -t node-app:baseline .")
Taille : 1.2GB (avec "docker image ls node-app")

## ETAPE 2 : Supprimer les mauvaises pratiques et image plus légère

Passage à node:20-alpine et suppression du "COPY node_modules ./node_modules" et "RUN apt-get update && apt-get install -y build-essential ..."

Temps de build : 6.2s (avec "docker build -t node-app:baseline .")
Taille : 146MB (avec "docker image ls node-app")

## ETAPE 3 : ajout d'un .dockerignore

Temps de build : 4.3s (avec "docker build -t node-app:baseline .")
Taille : 148MB (avec "docker image ls node-app")
=> plus lourd car on a ajouté un fichier

## ETAPE 4 : Changement dockerfile pour "mode production" + clean npm
=> copier les fichier intelligement

Changements :
- Mode prod : ENV NODE_ENV=production
- installation plus propre et plus rapide des packages avec npm ci, sans "devDependencies"
- Passage en EXPOSE 3000 seulement
- COPY package*.json ./ => Copie uniquement les fichiers nécessaires pour installer les dépendances

Temps de build : 3.8s (avec "docker build -t node-app:baseline .")
Taille : 147MB (avec "docker image ls node-app")

## ETAPE 5 : Utilisation du multistage

Rendu plus propre ou pro.

Temps de build : 1.7s (avec "docker build -t node-app:baseline .")
Taille : 144MB (avec "docker image ls node-app")

Suppression de USER root pour la sécurité.