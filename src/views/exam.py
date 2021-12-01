from manage import db
from flask import Blueprint, Response, request
from src.models.exam_model import Exam, Questions, Answers, Images, SubQuestion  

exam = Blueprint('exam', __name__)

exam_keys = ['id', 'title', 'year', 'topic', 'sub_topic']
image_keys = ['id', 'image_url', 'image_caption']
question_keys = ['id', 'question', 'ques_score', 'image_id']
answer_keys = ['id', 'ans','ques_id']
sub_question_keys = ['id', 'sub_question', 'sub_ques_score', 'sub_ques_ans_id']

@exam.route('/title', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Exam(id=None):
    if request.method == 'POST':
        title = request.form['title'] 
        year = request.form['year'] 
        topic = request.form['topic'] 
        sub_topic = request.form['sub_topic'] 
        exam = Exam(title = title, yeat = year, topic = topic, sub_topic = sub_topic)
        db.session.add(exam)
        db.session.commit()
        return Response('Exam title created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Exam.query.all()
        res = Exam.query.get(id).first()
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
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
        image = Images(url=url, image_caption=caption)
        db.session.add(image)
        db.session.commit()
        return Response('Image created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Images.query.all()
        res = Images.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Images.query.get(id)
        for key in image_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Image updated sucesfully')

    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Images.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Image deleted sucesfully')

@exam.route('/question', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Questions(id):
    if request.method == 'POST':
        ques = request.form['question'] 
        question_score = request.form['question_score']
        image_id = request.form['image_id'] 
        ques = Questions(ques=ques, ques_score=question_score,image=image_id)
        db.session.add(ques)
        db.session.commit()
        return Response('Question created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Questions.query.all()
        res = Questions.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Questions.query.get(id)
        for key in question_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Question updated sucesfully')
    
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Questions.query.get(id)
        db.session.delete(res)
        db.session.commit()
        return Response('Question deleted sucesfully')



@exam.route('/questions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _Answer(id):
    if request.method == 'POST':
        ans = request.form['answer'] 
        question_id = request.form['question_id'] 
        ans = Answers(ans=ans, question=question_id)
        db.session.add(ans)
        db.session.commit()
        return Response('Answer created sucesfully')

    if request.method == 'GET':
        if not id:
            res = Answers.query.all()
        res = Answers.query.get(id)
        return Response(res)

    if request.method == 'PUT':
        if not id:
            return Response('No id provided')
        if not request.form:
            return Response('No data provided')
        res = Answers.query.get(id)
        for key in answer_keys:
            if key in request.form:
                setattr(res, key, request.form[key])
        db.session.commit()
        return Response('Answer updated sucesfully')
    
    if request.method == 'DELETE':
        if not id:
            return Response('Please provide an id')
        res = Answers.query.get(id)
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
    


