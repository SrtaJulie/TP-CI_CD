
FROM python:3.10-slim 
# => choisir une image de base

# rep de travail
WORKDIR /app

# hop le fichier app.py dans le container
COPY app.py .

RUN pip install Flask

# alncer l’application
CMD ["python", "app.py"]
