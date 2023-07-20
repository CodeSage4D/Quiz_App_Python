from app import create_app, db
from app.models import Question

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # Add sample quiz questions to the database
        question1 = Question(
            question_text="What is the capital of France?",
            option_1="Berlin",
            option_2="London",
            option_3="Paris",
            option_4="Madrid",
            correct_option=3
        )

        question2 = Question(
            question_text="What is the largest mammal?",
            option_1="Elephant",
            option_2="Blue Whale",
            option_3="Giraffe",
            option_4="Hippopotamus",
            correct_option=2
        )

        # Add more questions as needed
        db.session.add(question1)
        db.session.add(question2)

        db.session.commit()
