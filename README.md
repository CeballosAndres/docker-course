# Curso introductorio a Docker

## 04 Agregando base de datos MySQL

**Objetivo:** Generar un archivo docker-compose que levante un entorno de desarrollo con la app Flask y la base de datos.

---

- Levantar contenedores con docker compose
  `docker-compose up -d`
    - `--force-recreate`
    - `--remove-orphans`

- Ver logs de contenedores del docker compose
  `docker-compose logs`

- Detener y eliminar contenedores del docker compose
  `docker-compose down`

## Fuentes de referencia

- https://docs.docker.com/compose/compose-file/compose-file-v3/