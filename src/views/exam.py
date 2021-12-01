import hashlib
from manage import db
from flask import Blueprint, Response, request
from src.models.exam_model import Exam, Question, Answer, Image, SubQuestion  

exam = Blueprint('exam', __name__)

exam_keys = ['title', 'year']
image_keys = ['image_url', 'image_caption']
question_keys = ['question', 'ques_score', 'image_id']
answer_keys = ['ans','ques_id']
sub_question_keys = ['sub_question', 'sub_ques_score', 'sub_ques_ans_id']

@exam.route('/title', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Exam(id=None):
    if request.method == 'POST':
        '''
        this is hashed because you can have 2019 KCSE and 2019 KCPE, 2019 Mock
        but never duplicates, even if it is in lowercase
        '''
        if not request.json:
            return Response(status=400)
        title = request.json.get('title')
        if not title:
            return Response(status=400, response='Title is required')
        year = request.json.get('year')
        if not year:
            return Response(status=400, response='year is required')
        string= title.lower() + year
        hash_object = hashlib.md5(string.encode())

        res = Exam.query.filter_by(exam_hash=hash_object.hexdigest()).first()
        if res:
            return Response(status=400, response='Exam already exists')

        exam = Exam( title=title, year=year, exam_hash=hash_object.hexdigest())
        db.session.add(exam)
        db.session.commit()
        return Response(status=201, mimetype='application/json')
    

    if request.method == 'GET':
        if not id:
            res = Exam.query.all()
        res = Exam.query.get(id).first()
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.json:
            return Response('No data provided')
        res = Exam.query.get(id)
        for key in exam_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Exam title updated sucesfully')
        
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Exam.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Exam title deleted sucesfully')

@exam.route('/search', methods=['GET'])
def _Search():
    if not request.args:
        return Response('No data provided')
    res = Exam.query.filter_by(**request.args).all()
    return Response(res)
    

@exam.route('/image', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Images(id):
    if request.method == 'POST':
        url = request.form['image_url'] 
        caption = request.form['caption']
        image = Image(url=url, image_caption=caption)
        db.session.add(image)
        db.session.commit()
        return Response('Image created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Image.query.all()
        res = Image.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Image.query.get(id)
        for key in image_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Image updated sucesfully')

    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Image.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Image deleted sucesfully')

@exam.route('/question', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Questions(id):
    if request.method == 'POST':
        ques = request.form['question'] 
        question_score = request.form['question_score']
        image_id = request.form['image_id'] 
        ques = Question(ques=ques, ques_score=question_score,image=image_id)
        db.session.add(ques)
        db.session.commit()
        return Response('Question created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Question.query.all()
        res = Question.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Question.query.get(id)
        for key in question_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Question updated sucesfully')
    
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Question.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Question deleted sucesfully')



@exam.route('/questions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Answer(id):
    if request.method == 'POST':
        ans = request.form['answer'] 
        question_id = request.form['question_id'] 
        ans = Answer(ans=ans, question=question_id)
        db.session.add(ans)
        db.session.commit()
        return Response('Answer created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Answer.query.all()
        res = Answer.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Answer.query.get(id)
        for key in answer_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Answer updated sucesfully')
    
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Answer.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Answer deleted sucesfully')

@exam.route('/subquestion', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Subquestion(id):
    if request.method == 'POST':
        sub_ques = request.form['sub_question'] 
        ques_id = request.form['ques_id'] 
        score = request.form['score']
        ans = request.form['ans']
        sub_ques = SubQuestion(sub_ques=sub_ques, question=ques_id, subques_score=score, sub_ques_ans_id=ans)
        db.session.add(sub_ques)
        db.session.commit()
        return Response('Sub_Question created sucesfully')

    if request.method == 'GET':
        if not id:
            res = SubQuestion.query.all()
        res = SubQuestion.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = SubQuestion.query.get(id)
        for key in sub_question_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Sub_Question updated sucesfully')
    
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = SubQuestion.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Sub_Question deleted sucesfully')
    


