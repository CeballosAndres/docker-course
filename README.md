# Curso introductorio a Docker

## 04 Agregando base de datos MySQL

- Ejecutando base de datos desde CLI
`ID=$(docker run -e MYSQL_ROOT_PASSWORD=123456789 -d -P arm64v8/mysql:oracle)`

- Obtener el puerto 3306 de MySQL
`docker port $ID 3306`
también se puede ver con
`docker ps`

- Es posible definir una base de datos durante la construcción del contenedor
`docker run -e MYSQL_ROOT_PASSWORD=123456789 -e MYSQL_DATABASE=curso_users -d -p 3306:3306 mysql`

### Fuentes de información
- https://hub.docker.com/_/mysql

