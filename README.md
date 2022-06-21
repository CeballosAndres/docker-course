# Curso introductorio a Docker

## 00 Hola mundo

**Objetivo:** Familiarizarse con los comandos básicos y comprobar el correcto funcionamiento del entorno.

---

### Pasos de la práctica

- Corriendo el hola mundo
  `docker run hello-world`
- Corriendo ubuntu en modo interactivo
  `docker run -it ubuntu bash`
  - `cat /etc/os-release`
- Corriendo web app y publicando puerto
  `docker run -d -p 80:80 docker/getting-started` 

### Comandos explorados

- Ejecutar (descarga también) contenedores
  - `docker run`
- Listar contenedores
  - `docker ps`
  - `docker ps --all` ver también los que no están en ejecución
- Detener contenedor
  - `docker stop`
- Eliminar contenedor 
  - `docker rm ID`
  - `docker rm -f ID` forzar la eliminación
