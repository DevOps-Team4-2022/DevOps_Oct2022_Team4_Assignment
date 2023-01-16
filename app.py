from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.exc import IntegrityError
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root2:password123@localhost/internship_data'
db = SQLAlchemy(app)


# Create student tables
class Student_Data(db.Model):
    __tablename__ = 'Student_Data'
    Student_ID = db.Column(db.String(10), primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Preference = db.Column(db.String(255), nullable=False)
    Status = db.Column(db.Enum('Unassigned', 'Pending confirmation', 'Confirmed', 'New Status'), nullable=False)

    def __repr__(self):
        return '<Student ID: %r>' % self.Student_ID


# Create company tables
class Company_Data(db.Model):
    __tablename__ = 'Company_Data'
    Company_Name = db.Column(db.String(255), primary_key=True)
    Job_Role = db.Column(db.String(255), nullable=False)
    Company_Contact = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    __table_args__ = (
        CheckConstraint('email LIKE "%@%.%"', name='valid_email'),
    )
    def __repr__(self):
        return '<Company_Name: %r>' % self.Company_Name


























































@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)