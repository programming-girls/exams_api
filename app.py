from manage import app, db

#blueprints
from src.views.text_marking_scheme import text_marking_scheme
from src.views.choice_marking_scheme import choice_marking_scheme
from src.views.exam import exam

#register blueprints
app.register_blueprint(text_marking_scheme)
app.register_blueprint(choice_marking_scheme)
app.register_blueprint(exam)


with app.app_context():
    from src.models.exam_model import Exam, Subject, Question, SubQuestion, Answer, Image
    db.create_all()


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)