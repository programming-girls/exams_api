# EXAM API


## What is it?

A graphql api for CRUD of exam + Scoring

## Installation

Clone the repo

Navigate to the root folder

```cd exam-api ```

Create a virtualenv

```virtualenv venv```

Install the necessary packages

```pip install -r requirements.txt```

Perform migrations

```
python manage.py makemigrations
python manage.py migrate
```

Testing

```python manage.py test```

# Running the app

```export FLASK_APP=app.py```

Start the server

```flask run```

