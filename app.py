from manage import app, db
from flask import request, jsonify, abort

from src.exam.models.model import Exam, Subject, Question, SubQuestion, Answer, Image

#blueprints
from src.orc_engine.ocr_server import ocr_core, ocr
from src.exam.views.text_marking_scheme import text_marking_scheme
from src.exam.views.choice_marking_scheme import choice_marking_scheme



#register blueprints
app.register_blueprint(ocr)
app.register_blueprint(text_marking_scheme)
app.register_blueprint(choice_marking_scheme)


with app.app_context():
    from src.exam.models.model import Exam, Subject, Question, SubQuestion, Answer, Image
    db.create_all()


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)