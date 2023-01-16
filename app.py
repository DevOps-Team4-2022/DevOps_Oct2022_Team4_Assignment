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


@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded files
    student_data = request.files.get('internship_student_data')
    company_data = request.files.get('internship_company_data')

    # check if either one of the files are uploaded
    if student_data:
        try:
            if student_data.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                student_df = pd.read_excel(student_data)
                if set(student_df.columns) == set(['Student_ID', 'Name', 'Preference', 'Status']):
                    for index, row in student_df.iterrows():
                        student = Student_Data.query.filter_by(Student_ID=row['Student_ID']).first()
                        if not student:
                            student = Student_Data(Student_ID=row['Student_ID'], Name=row['Name'],
                                                   Preference=row['Preference'], Status=row['Status'])
                            db.session.add(student)
                            db.session.commit()
                        else:
                            continue
                    return redirect('/')
                else:
                    return 'The columns in the excel file does not match the columns in the table'
            else:
                return 'The file is not in excel format'
        except IntegrityError:
            print("record already exists")
            db.session.rollback()
            return redirect('/')

    elif company_data:
        try:
            if company_data.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                company_df = pd.read_excel(company_data)
                if set(company_df.columns) == set(['Company_Name', 'Job_Role', 'Company_Contact', 'Email']):
                    for index, row in company_df.iterrows():
                        company = Company_Data.query.filter_by(Company_Name=row['Company_Name']).first()
                        if not company:
                            company = Company_Data(Company_Name=row['Company_Name'], Job_Role=row['Job_Role'],
                                                   Company_Contact=row['Company_Contact'], Email=row['Email'])
                            db.session.add(company)
                            db.session.commit()
                            return redirect('/')
                    else:
                        return 'The columns in the excel file does not match the columns in the table'
                else:
                    return 'The file is not in excel format'
        except IntegrityError:
            print("record already exists")
            db.session.rollback()
            return redirect('/')
    else:
        return 'Please upload either student or company data'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)