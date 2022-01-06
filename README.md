# inventory-tracking

## Project for Shopify Challenge - Summer 2022

## Docker Instructions

- With sudo privileges:

- To build docker container: `docker build -t <image name> .` e.g. `docker build -t inventory-tracking .`

- To run docker container: `docker run -it --rm --env-file <env file> -p 8000:8000 <image name>` e.g. `docker run -it --rm --env-file .env -p 8000:8000 inventory-tracking`