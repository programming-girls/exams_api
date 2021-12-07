from manage import application, db

#blueprints
from src.views.text_marking_scheme import text_marking_scheme
from src.views.choice_marking_scheme import choice_marking_scheme
from src.views.exam import exam

#register blueprints
application.register_blueprint(text_marking_scheme)
application.register_blueprint(choice_marking_scheme)
application.register_blueprint(exam)


with application.app_context():
    from src.models.exam_model import Exam, Subject, Question, SubQuestion, Answer, Image
    db.create_all()


@application.route('/')
def hello():
    division_by_zero = 1 / 0
    return "Hello World!"


if __name__ == '__main__':
    application.run(debug=True)