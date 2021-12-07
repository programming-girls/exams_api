import hashlib
from manage import db
from flask import Blueprint, Response, request, jsonify
from src.models.exam_model import Exam, Question, Answer, Image, SubQuestion  

exam = Blueprint('exam', __name__)

exam_keys = ['title', 'year']
image_keys = ['image_url', 'image_caption']
question_keys = ['question', 'ques_score', 'image_id']
answer_keys = ['ans','ques_id']
sub_question_keys = ['sub_question', 'sub_ques_score', 'sub_ques_ans_id']

def hash_exam_title(string):
    hash = hashlib.md5(string.encode())
    return hash.hexdigest()

@exam.route('/title', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Exam():
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

        hash_object = hash_exam_title(string)

        res = Exam.query.filter_by(exam_hash=hash_object).first()
        if res:
            return Response(status=400, response='Exam already exists')

        exam = Exam( title=title, year=year, exam_hash=hash_object)
        db.session.add(exam)
        db.session.commit()
        return Response(status=201, mimetype='application/json')
    

    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            res = Exam.query.all()
            for exam in res:
                return Response(status=200, mimetype='application/json', response=exam)

        res = Exam.query.filter_by(id=id).first()
        if not res:
            return Response(status=404, response='Exam not found')
        return Response(status=200, mimetype='application/json', response=res)

    if request.method == 'PUT':
        id = request.args.get('id')
        if not id:
            return Response('No id provided')
        if not request.json:
            return Response('No data provided')
        res = Exam.query.get(id)
        if not res:
            return Response('Exam not found', status=404)

        for key in exam_keys:
            if key in request.json:

                setattr(res, key, request.json[key])
        # todo: update exam_hash on update
        db.session.commit()
        return Response('Exam title updated sucesfully')
        
    if request.method == 'DELETE':
        id = request.args.get('id')
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
def _Images():
    if request.method == 'POST':
        url = request.form['image_url'] 
        caption = request.form['caption']
        image = Image(url=url, image_caption=caption)
        db.session.add(image)
        db.session.commit()
        return Response('Image created sucesfully')

    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            res = Image.query.all()
            for image in res:
                return Response(status=200, mimetype='application/json', response=image)
        res = Image.query.get(id)
        if not res:
            return Response(status=404, response='Image not found')
        return Response(res)

    if request.method == 'PUT':
        id = request.args.get('id')
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
        id = request.args.get('id')
        if not id:
            return Response('Please provide an id')
        res = Image.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Image deleted sucesfully')

@exam.route('/question', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Questions():
    if request.method == 'POST':
        data =request.json

        if not data:
            return Response(status=400, response='No data provided')

        ques = data['question'] 

        if not ques:
            return Response(status=400, response='Question is required')

        question_score = data['question_score']

        if not question_score:
            return Response(status=400, response='Question score is required')

        image_id = data['image_id'] 

        if not image_id:
            image_id = None

        ques = Question(ques=ques, ques_score=question_score,image=image_id)
        db.session.add(ques)
        db.session.commit()
        return Response('Question created sucesfully')

    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            res = Question.query.all()
            for question in res:
                return Response(status=200, mimetype='application/json', response=question)
        res = Question.query.get(id)
        if not res:
            return Response(status=404, response='Question not found')
        return Response(status=200, mimetype='application/json', response=res)

    if request.method == 'PUT':
        id = request.args.get('id')
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
        id = request.args.get('id')
        if not id:
            return Response('Please provide an id')
        res = Question.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Question deleted sucesfully')



@exam.route('/answer', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Answer():
    if request.method == 'POST':

        data =request.json

        if not data:
            return Response(status=400, response='No data provided')

        ans = data['answer'] 

        if not ans:
            return Response(status=400, response='Answer is required')
        question_id = data['question_id'] 

        if not question_id:
            return Response(status=400, response='Question id is required')

        ans = Answer(ans=ans, question=question_id)
        db.session.add(ans)
        db.session.commit()
        return Response('Answer created sucesfully')

    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            res = Answer.query.all()
            for answer in res:
                return Response(status=200, mimetype='application/json', response=answer)
        res = Answer.query.get(id)
        if not res:
            return Response(status=404, response='Answer not found')
        return Response(status=200, mimetype='application/json', response=res)

    if request.method == 'PUT':
        id = request.args.get('id')
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
        id = request.args.get('id')
        if not id:
            return Response('Please provide an id')
        res = Answer.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Answer deleted sucesfully')

@exam.route('/subquestion', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Subquestion(id=None):
    data = request.json
    if not data:
        return Response('No data provided', status=400)

    if request.method == 'POST':

        sub_ques = data['sub_question'] 
        ques_id = data['ques_id'] 
        score = data['score']
        ans = data['ans']

        if not sub_ques:
            return Response('No sub question provided')
        if not ques_id:
            return Response('No question id provided')
        if not score:
            return Response('No score provided')
        if not ans:
            return Response('No answer provided')

        sub_ques = SubQuestion(sub_ques=sub_ques, question=ques_id, subques_score=score, sub_ques_ans_id=ans)
        db.session.add(sub_ques)
        db.session.commit()
        return Response('Sub_Question created sucesfully')

    if request.method == 'GET':
        if not id:
            res = SubQuestion.query.all()
            for sub_question in res:
                return Response(status=200, mimetype='application/json', response=sub_question)
        res = SubQuestion.query.get(id)
        if not res:
            return Response(status=404, response='Sub_Question not found')
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
    


