# Curso introductorio a Docker

## 02 Con docker en CLI

**Objetivo:** Ejecución de la script desde un contenedor Docker, y observar las ventajas que otorga.

---

- Ejecutar desde CLI un simple script de python
  `docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python hello_from_docker.py`

## Fuentes de referencia

-  https://hub.docker.com/_/python
