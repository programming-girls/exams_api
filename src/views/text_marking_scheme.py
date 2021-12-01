from os import abort
from thefuzz import fuzz
from flask import Blueprint,request, jsonify
from src.models.exam_model import Question_Answer, Question


text_marking_scheme = Blueprint('text_marking_scheme', __name__)

class Text_marking_scheme:
    def __init__(self, student_answer: str, question_id: int) -> None:
        self.student_answer = student_answer
        self.question_id = question_id

    def get_correct_answer(self) -> str:
        ans = Question_Answer.query.filter_by(question_id=self.question_id).first()
        return ans.answer

    def question_score(self) -> int:
        score = Question.query.filter_by(question_id=self.question_id).first()
        return score.score
    

    def compare_answer(self) -> int:
        correct_answer = self.get_correct_answer()
        score = fuzz.partial_token_set_ratio(self.student_answer, correct_answer)
        return score

    def get_score(self) ->int:

        res = 0
        fuzz_score = self.compare_answer()
        question_score = self.question_score()
        if fuzz_score <= 50:
            res = 0
        else:
            res = int(fuzz_score * question_score) // 100

        return res

@text_marking_scheme.route('/tms', methods=['GET'])
def get_answer():
    data = request.get_json()

    if not data:
        return jsonify({"message": "add data to the body in json format"})

    
    sa = data['student_answer']
    qi = data['question_id']
    tms = Text_marking_scheme(sa, qi)

    return jsonify({"score": tms.get_score()})

if __name__ == '__main__':
    Text_marking_scheme()