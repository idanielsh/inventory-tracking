# inventory-tracking / Shopify Solution Challenge - Summer 2022

## Usage

The API is currently hosted using heroku on https://shopify-inventory-tracking.herokuapp.com/

The interactive API documentation can be accessed at https://shopify-inventory-tracking.herokuapp.com/docs . This documentation is also available when deployed locally at http://0.0.0.0:8000/docs.


## Requirements

- Docker
- Git

## Installation

Clone the git repo to the desired folder:
```bash
git clone https://github.com/idanielsh/inventory-tracking
cd inventory-tracking 
```

## Setup 

```bash
cat .env.example > .env
```

Using a text editor, fill in the missing `DATABASE_URL` inside the newly created `.env` with a connection string to a database with a schema stored on `db_util/schema.ddl`

To build and run the docker container:

```bash
sudo docker build -t inventory-tracking .

sudo docker run -it --rm --env-file .env -p 8000:8000 inventory-tracking
```

This will launch the API on http://0.0.0.0:8000/

## Technical Details

This API was built using [FastAPI](https://fastapi.tiangolo.com/). I decided to use FastAPI due to its simple and intuitive design, familiarity from use in past projects, and the [auto generated documentation](https://shopify-inventory-tracking.herokuapp.com/docs). 

I chose to use PostgreSQL as the database, hosted on [Heroku Postgres](https://www.heroku.com/postgres)

