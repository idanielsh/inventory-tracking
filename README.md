# inventory-tracking / Shopify Solution Challenge - Summer 2022

## Requirements

- Docker
- Git

## Installation

Clone the git repo to the desired folder:
```bash
git clone https://github.com/idanielsh/inventory-tracking
cd inventory-tracking 
```

### Setup 

```bash
cat .env.example > .env
```

Using a text editor, fill in the missing `DATABASE_URL` inside the newly created `.env` with a connection string to a database with a schema stored on `db_util/schema.ddl`

With sudo privileges:

```bash
docker build -t inventory-tracking .

docker run -it --rm --env-file .env -p 8000:8000 inventory-tracking
```

This will launch the API on http://0.0.0.0:8000/

## Usage

The API is currently hosted using heroku on https://shopify-inventory-tracking.herokuapp.com/

The interactive API documentation can be accessed at https://shopify-inventory-tracking.herokuapp.com/docs . This documentation is also available when deployed locally at http://0.0.0.0:8000/docs.

