from app.app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    option_1 = db.Column(db.String(100), nullable=False)
    option_2 = db.Column(db.String(100), nullable=False)
    option_3 = db.Column(db.String(100), nullable=False)
    option_4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"Question(id={self.id}, question_text='{self.question_text}', correct_option='{self.correct_option}')"
