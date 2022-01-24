# EXAM API


## What is it?

A REST api for CRUD of exam + Scoring

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
python populate_db.py
```

Testing

```python manage.py test```

# Running the app

```export FLASK_APP=app.py```

Start the server

```flask run```

# Endpoints

## /title
POST 
```
{
    "title":"KCSE",
    "year":2019

}
```
PUT title?id=2
```
{
  "title":"KCPE",
   "year":2019  
}
```
```
GET title?id=2 | /title
```
```
DELETE title?id=2 
```
## /search

```
{
    "year" : 2019
}
```
## /image

POST
```
{
    "url": "www.picture.com",
    "caption": "wonderful picture",
    "question_id": 2

}
```
PUT
```
{
    "url": "www.picture.com",
    "caption": "wonderful picture",
    "question_id": 3
}
```
```
GET image?id=2 | /image
```
```
DELETE image?id=2
```
## /question
POST
```
{
    "ques": "what is a female sheep called",
    "question_score": 20

}
```
PUT question?id=2 
```
{
    "ques": "what is a female sheep called",
    "question_score": 20

}
```
```
GET question?id=2 |/ question
```
```
DELETE question?id=2
```
## /answer
POST
```
{
    "answer": "ew",
    "question_id": 2

}
```
PUT answer?id=3
```
{
    "answer": "eww"
}
```
```
GET answer?id=3 | /answer
```
```
DELETE answer?id=2
```
## /subquestion
```
POST
{
    "sub_ques": "what specie is an elephant",
    "ques_id": 1,
    "score": 1,
    "ans": "All elephants are mammals belonging to the elephantidae family"
}
```
```
PUT sub_question?id=2
{
    "sub_ques": "what specie is an elephant",
    "ques_id": 1,
    "score": 1,
    "ans": "All elephants are mammals belonging to the elephantidae family"
}
```
```
GET sub_question?id=2 | sub_question
```
```
DELETE sub_question?id=2
```
## /cms

```
{
    "student_answer": "something excellent",
    "question_id": 20
}
```
## /tms

```
{
    "student_choice":"A",
    "question_id" : 1
}
```


# Marking Scheme

Primary School: 

Choice Question Marking Scheme

Choice selected by pupil is compared the the correct answer linked the the question in the db, and if correct, score ir provided else, score is 0

Secondary School:

Text Marking Scheme

Because student cannot write exactly what the marking scheme provides, a matching algorithm is used to do a string match.

It uses [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to calculate the differences between sequences in a simple-to-use package

### Example:

"fuzzy was a bear", "fuzzy fuzzy was a bear"
Score: 84


