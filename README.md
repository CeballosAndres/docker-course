# Curso introductorio a Docker

## 03 Con docker file

- Construir imagen con un tag
`docker build -t my-flask-app:v1 .`

- Correr contenedor en modo interactivo
`docker run -it --rm --name my-running-app -p 5000:5000 my-flask-app:v1`

- Correr montando volumen y con variable para debug mode
`docker run -it --rm --name my-running-app -e FLASK_ENV=development -v ~/dev/hmh/docker-course:/usr/src/app -p 5000:5000 my-flask-app:v1`

- Correr contenedor en modo detached
`docker run --name my-running-app -p 5000:5000 -d my-flask-app:v1`