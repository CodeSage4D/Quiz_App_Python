# app/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'
db = SQLAlchemy(app)

# Add your route definitions and other code here...

if __name__ == "__main__":
    app.run(debug=True)
