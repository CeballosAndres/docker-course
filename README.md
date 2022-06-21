# Curso introductorio a Docker

## 03 Con docker file

**Objetivo:** Crear una imagen Docker a partir de otra con uso del Dockerfile.

---

### Pasos práctica

- Revisar contenido del archivo Dockerfile
- Construir imagen con un tag
  `docker build -t my-flask-app:v1 .`
- Modificar imagen de Python y tomar la de alpine
  `docker build -t my-flask-app:alpine-v1 .`
- Comparar tamaños de imágenes creadas `docker images`

- Correr contenedor en modo interactivo
  `docker run -it --rm --name my-running-app -p 8000:5000 my-flask-app:v1`

- Correr montando volumen y con variable para debug mode
  `docker run -it --rm --name my-running-app -e FLASK_ENV=development -v "$PWD":/usr/src/app -p 8000:5000 my-flask-app:v1`

- Correr contenedor en modo detached
  `docker run --name my-running-app -p 8000:5000 -d my-flask-app:v1`
