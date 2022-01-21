import json
import requests
from datetime import date

print('Populating database...')

url = 'http://127.0.0.1:5000/title'
subject_url = 'http://127.0.0.1:5000/subject'

exams = ['KCSE', 'KCPE']

def generate_exam():
  start = 1985
  end = (date.today())

  print('Generating exams...')

  while start <= end.year:
    for each in exams:
        payload = {
          "title": each,
          "year": start
        }
        response = requests.post(url, json = payload)

        print(response.text)
    start += 1

# generate_exam()

subjects = ['ENGLISH', 'KISWAHILI', 'MATHEMATICS', 'BIOLOGY', 'PHYSICS', 'CHEMISTRY','HISTORY AND GOVERNMENT', 'GEOGRAPHY', 'CHRISTIAN RELIGIOUS EDUCATION', 'ISLAMIC RELIGIOUS EDUCATION', 'HINDU RELIGIOUS EDUCATION', 'HOME SCIENCE', 'ART AND DESIGN', 'AGRICULTURE', 'WOODWORK', 'METALWORK', 'BUILDING CONSTRUCTION', 'POWER MECHANICS', 'ELECTRICITY', 'DRAWING AND DESIGN', 'AVIATION TECHNOLOGY', 'COMPUTER STUDIES', 'FRENCH', 'GERMAN', 'ARABIC', 'KENYA SIGN LANGUAGE', 'MUSIC', 'BUSINESS STUDIES']
sub_topic = ['PAPER 1', 'PAPER 2', 'PAPER 3']

print('Generating subjects...')

def generate_subject():
      exam_ids = list()

      exams = requests.get(url) 

      for each in exams.json():
          exam_ids.append(each['id'])
                        
      for each_exam in exam_ids:
          for each_subject in subjects:
              for each_sub_topic in sub_topic:
                  payload = {
                    "subject_topic": each_subject,
                    "sub_topic": each_sub_topic,
                    "exam_id": each_exam
                  }
                  response = requests.post(subject_url, json = payload)
                  print(response.text)

      
generate_subject()

    
    