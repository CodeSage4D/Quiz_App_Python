from flask import render_template, request
from app.models import Question
from app import app

@app.route('/')
def index():
    # Retrieve all questions from the database
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve all questions from the database
    questions = Question.query.all()

    # Initialize the score
    score = 0

    # Loop through the questions
    for question in questions:
        # Retrieve the user's selected answer for the current question
        selected_answer = request.form.get(f'answer_{question.id}')

        # Compare the selected answer with the correct answer
        if selected_answer == str(question.correct_option):
            score += 1

    # Calculate the percentage of correct answers
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    # You can decide how to display the results here
    # For example, you can create a results template or display the results directly
    result_message = f"You scored {score}/{total_questions} ({percentage:.2f}%)"

    # Display the results to the user
    return render_template('results.html', result_message=result_message)
