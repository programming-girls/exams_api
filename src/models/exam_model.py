from manage import db

Exam_Subject=db.Table('exam_subject',
    db.Column('exam_id', db.Integer, db.ForeignKey('exam.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)

Subject_Question=db.Table('subject_question',
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
)

Question_SubQuestion = db.Table('question_subquestion',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('subquestion_id', db.Integer, db.ForeignKey('subquestion.id'))
)

Question_Answer=db.Table('question_answer',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'))
)

Question_Image=db.Table('question_image',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('image_id', db.Integer, db.ForeignKey('image.id'))
)

class Exam(db.Model):
    __tablename__ = 'exam'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    year = db.Column(db.String(), nullable=False)
    exam_hash = db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return "<Exam: {}, {}, {}, {}>".format(self.id, self.title, self.year, self.exam_hash)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'exam_hash': self.exam_hash
        }

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    subject_topic = db.Column(db.String(), nullable=False)
    sub_topic = db.Column(db.String(), nullable=True)
    exam = db.relationship('Exam', secondary=Exam_Subject, backref=db.backref('Subject', lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
        return "<Subject ID: {}>".format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'subject_topic': self.subject_topic,
            'sub_topic': self.sub_topic
        }

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(), nullable=False)
    ques_score = db.Column(db.Integer, nullable=False)
    subject = db.relationship('Subject', secondary=Subject_Question, backref=db.backref('Question', lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
            return "<Question ID: {}>".format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'ques': self.ques,
            'ques_score': self.ques_score
        }

class SubQuestion(db.Model):
    __tablename__ = 'subquestion'
    id = db.Column(db.Integer, primary_key=True)
    subques = db.Column(db.String(), nullable=False)
    subques_score = db.Column(db.Integer, nullable=False)
    sub_ques_ans_id = db.Column(db.Integer, db.ForeignKey("Answer.id"))
    question = db.relationship('Question', secondary=Question_SubQuestion, backref=db.backref('SubQuestion', lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
        return "<SubQuestion ID: {}>".format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'subques': self.subques,
            'subques_score': self.subques_score,
            'sub_ques_ans_id': self.sub_ques_ans_id
        }

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    ans = db.Column(db.String(), nullable=False)
    question = db.relationship('Question', secondary=Question_Answer, backref=db.backref('Answer', lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
        return "<Answer ID: {}>".format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'ans': self.ans
        }

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    images_url = db.Column(db.String(), nullable=False, unique=True)
    image_caption = db.Column(db.String(), nullable=True)
    question = db.relationship('Question', secondary=Question_Image, backref=db.backref('Image', lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
        return "<Image ID: {}>".format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'images_url': self.images_url,
            'image_caption': self.image_caption
        }

