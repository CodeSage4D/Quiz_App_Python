from flask import render_template, request
from ..models import db, Question
from . import app

# Your route definitions here...
@app.route('/')
def index():
    # Retrieve all questions from the database
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@main.route('/submit', methods=['POST'])
def submit():
    # Retrieve all questions from the database
    questions = Question.query.all()

    # Initialize the score and total number of questions
    score = 0
    total_questions = len(questions)

    # Loop through the questions
    for question in questions:
        # Retrieve the user's selected answer for the current question
        selected_answer = request.form.get(f'answer_{question.id}')

        # Compare the selected answer with the correct answer
        if selected_answer == str(question.correct_option):
            score += 1

    # Calculate the percentage of correct answers
    percentage = (score / total_questions) * 100

    # You can decide how to display the results here
    # For example, you can create a results template or display the results directly

    # Here, I'm passing the score and total_questions as arguments to the template
    # You can modify this based on your template structure
    return render_template('results.html', score=score, total_questions=total_questions, percentage=percentage)
