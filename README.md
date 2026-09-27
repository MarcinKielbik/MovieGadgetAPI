# MovieGadgetAPI

REST API for managing movie gadgets and related articles, built with Django REST Framework.

## Technologies

* Python
* Django
* Django REST Framework
* SQLite
* Pillow
* Postman

## Features

### Movie Gadgets

* Create movie gadgets
* Retrieve all gadgets
* Retrieve a single gadget
* Update gadgets
* Partially update gadgets
* Delete gadgets
* Upload gadget images

### Articles

* Create articles related to movie gadgets
* Retrieve a single article
* Delete articles
* Upload article images
* Automatically record the publication date
* Associate articles with specific movie gadgets

## API Endpoints

### Movie Gadgets

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | `/api/gadgets/`      | Get all gadgets           |
| POST   | `/api/gadgets/`      | Create a gadget           |
| GET    | `/api/gadgets/<id>/` | Get a gadget              |
| PUT    | `/api/gadgets/<id>/` | Update a gadget           |
| PATCH  | `/api/gadgets/<id>/` | Partially update a gadget |
| DELETE | `/api/gadgets/<id>/` | Delete a gadget           |

### Articles

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| POST   | `/api/articles/`      | Create an article |
| GET    | `/api/articles/<id>/` | Get an article    |
| DELETE | `/api/articles/<id>/` | Delete an article |

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The API is available at:

```text
http://127.0.0.1:8000/api/
```
