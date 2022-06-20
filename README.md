# Curso introductorio a Docker

## 02 Con docker en CLI

Ejecutar desde CLI un simple script de python
`docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python hello_from_docker.py`

https://hub.docker.com/_/python
