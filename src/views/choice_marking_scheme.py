from flask import Blueprint,request, jsonify
from src.models.exam_model import Answer, Question, Question_Answer


choice_marking_scheme = Blueprint('choice_marking_scheme', __name__)

class Choice_marking_scheme:
    def __init__(self, student_choice: str, question_id: int) -> None:
        self.student_choice = student_choice
        self.question_id = question_id

    def get_answer_from_db(self) -> str:
        ans = Question_Answer.query.filter(question_id = self.question_id ).first()
        return ans

    def compare_choice(self) ->bool:

        correct_ans = self.get_answer_from_db()
        if self.student_choice == correct_ans:
            return True
        return False

@choice_marking_scheme.route('/cms', methods=['GET'])
def get_answer():
    data = request.get_json()

    if not data:
        return jsonify({"message": "add data to the body in json format"})

    sc = data['student_choice']

    if not sc:
        return jsonify({"message": "add student choice to the body in json format"})

    qi = data['question_id']

    if not qi:
        return jsonify({"message": "add question id to the body in json format"})
    
    
    cms = Choice_marking_scheme(sc, qi)

    return jsonify({"score": cms.compare_choice()})

if __name__ == '__main__':
    Choice_marking_scheme()