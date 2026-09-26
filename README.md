# MovieGadgetAPI

REST API for managing movie gadgets, built with Django REST Framework.

## Technologies

* Python
* Django
* Django REST Framework
* SQLite
* Pillow

## Features

* Create movie gadgets
* Retrieve all gadgets
* Retrieve a single gadget
* Update gadgets
* Partially update gadgets
* Delete gadgets
* Upload gadget images

## API Endpoints

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | `/api/gadgets/`      | Get all gadgets           |
| POST   | `/api/gadgets/`      | Create a gadget           |
| GET    | `/api/gadgets/<id>/` | Get a gadget              |
| PUT    | `/api/gadgets/<id>/` | Update a gadget           |
| PATCH  | `/api/gadgets/<id>/` | Partially update a gadget |
| DELETE | `/api/gadgets/<id>/` | Delete a gadget           |

## Running the project

```bash
python manage.py runserver
```

The API is available at:

```text
http://127.0.0.1:8000/api/gadgets/
```
