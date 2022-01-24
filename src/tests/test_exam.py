import pytest
import a_client as client

title_get_data = [
    {{}, 400},
    {{'title': 'test'}, 400},
    {{'title': 'test', 'year': '2019'}, 201},
    {{'title': 'test', 'year': '2019'}, 400},
]
@pytest.mark.parametrize('title', title_get_data)
def test_title_get(client):
    response = client.get('/title')
    assert response.status_code == 200
    assert b'Welcome!' in response.data

def test_title_post(client):
    response = client.post('/title')
    assert response.status_code == 200

def test_title_put(client):
    response = client.put('/title')
    assert response.status_code == 200

def test_title_delete(client):
    response = client.delete('/title')
    assert response.status_code == 200

subject_data = []
@pytest.mark.parametrize('subject', subject_data)
def test_subject():
    assert True 

search_data = []
@pytest.mark.parametrize('search', search_data)
def test_search():
    assert True

images_data = []
@pytest.mark.parametrize('image', images_data)
def test_images():
    assert True 

question_data=[]
@pytest.mark.parametrize('question', question_data)
def test_questions():
    assert True

answer_data = []
@pytest.mark.parametrize('answer', answer_data)
def test_answers():
    assert True

