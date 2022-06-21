# Curso introductorio a Docker

## 04 Agregando base de datos MySQL

**Objetivo:** Levantar un contenedor con una instancia de base de datos y lograr que los datos sean persistentes en un volumen.

---

- Ejecutando base de datos desde CLI
  `ID=$(docker run -e MYSQL_ROOT_PASSWORD=123456789 -d -P arm64v8/mysql:oracle)`

- Obtener el puerto 3306 de MySQL
  `docker port $ID 3306`
  también se puede ver con
  `docker ps`

- Es posible definir una base de datos durante la construcción del contenedor
  `docker run -e MYSQL_ROOT_PASSWORD=123456789 -e MYSQL_DATABASE=course -d -p 3307:3306 arm64v8/mysql:oracle`

### Fuentes de referencia

- https://hub.docker.com/_/mysql
