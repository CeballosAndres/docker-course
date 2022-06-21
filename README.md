# Curso introductorio a Docker

## 00 Hola mundo

**Objetivo:** Familiarizarse con los comandos básicos y comprobar el correcto funcionamiento del entorno.

---

- Corriendo el hola mundo
  `docker run hello-world`
- Corriendo ubuntu en modo interactivo
  `docker run -it ubuntu bash`
- Corriendo web app y publicando puerto
  `docker run -d -p 80:80 docker/getting-started` 
  - `cat /etc/os-release`
