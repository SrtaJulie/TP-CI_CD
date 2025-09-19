# Fichier de suivi du TP Optimisation Docker 

Le travail a été réalisé sur Codespaces.

## Analyse initiale du fichier

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
