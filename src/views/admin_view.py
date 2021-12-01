from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from manage import app, db


from src.models.exam_model import Exam, Subject, Question, SubQuestion, Answer, Image

ad = Blueprint('ad', __name__)

admin = Admin(app, name='Exam API', template_mode='bootstrap3')
admin.add_view(ModelView(Exam, db.session))
admin.add_view(ModelView(Subject, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(SubQuestion, db.session))
admin.add_view(ModelView(Answer, db.session))
admin.add_view(ModelView(Image, db.session))