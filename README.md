# Curso introductorio a Docker

## 04 Agregando base de datos MySQL

**Objetivo:** Levantar un contenedor con una instancia de base de datos y lograr que los datos sean persistentes en un volumen.

---

### Pasos de la práctica

- Levantar contenedor con base de datos MySQL desde CLI
  `ID=$(docker run -e MYSQL_ROOT_PASSWORD=123456789 -d -P arm64v8/mysql:oracle)`

- Obtener el puerto 3306 de MySQL
  `docker port $ID 3306`

  - también se puede ver con
    `docker ps`

- Conectarse, crear base de datos y tabla en base de datos, con script create_table.sql

- Eliminar contenedor de MySQL creado `docker rm -f $ID`

- Levantar un contenedor con definición de base de datos durante la construcción del contenedor, con puerto definido y con almacenamiento persistente
  `docker run -e MYSQL_ROOT_PASSWORD=123456789 -e MYSQL_DATABASE=course -v ~/apps/mysql:/var/lib/mysql -d -p 3307:3306 arm64v8/mysql:oracle`

- Conectarse, crear base de datos y tabla en base de datos, con script create_table.sql
- **De la práctica anterior.**
  - `docker build -t my-flask-app:alpine-v1 .` *poner el punto* 
  - `docker run -it --rm --name my-running-app -e FLASK_ENV=development -v "$PWD":/usr/src/app -p 8000:5000 my-flask-app:alpine-v1`
### Fuentes de referencia

- https://hub.docker.com/_/mysql
