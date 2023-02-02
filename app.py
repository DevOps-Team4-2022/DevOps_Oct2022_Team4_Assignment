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
    company_id = db.Column(db.Integer, db.ForeignKey('Company_Data.Company_ID'), nullable=True)

    def __repr__(self):
        return '<Student ID: %r>' % self.Student_ID


# Create company tables
class Company_Data(db.Model):
    __tablename__ = 'Company_Data'
    Company_ID = db.Column(db.Integer, primary_key=True)
    Company_Name = db.Column(db.String(255), nullable=False)
    Job_Role = db.Column(db.String(255), nullable=False)
    Company_Contact = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    __table_args__ = (
        CheckConstraint('email LIKE "%@%.%"', name='valid_email'),
    )

    def __repr__(self):
        return '<Company_ID: %r>' % self.Company_ID


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
                if set(student_df.columns) == set(['Student_ID', 'Name', 'Preference', 'Status', 'Company_ID']):
                    for index, row in student_df.iterrows():
                        if 'Company_ID' in row and not pd.isna(row['Company_ID']):
                            company = Company_Data.query.filter_by(Company_ID=row['Company_ID']).first()
                            if not company:
                                return f"<script> alert('The Company ID is not valid'); window.history.back(); </script>"
                            else:
                                student = Student_Data.query.filter_by(Student_ID=row['Student_ID']).first()
                                if not student:
                                    student = Student_Data(Student_ID=row['Student_ID'], Name=row['Name'],
                                                           Preference=row['Preference'], Status=row['Status'],
                                                           company_id=row['Company_ID'])
                                    db.session.add(student)
                                    db.session.commit()
                                else:
                                    continue
                        else:
                            student = Student_Data.query.filter_by(Student_ID=row['Student_ID']).first()
                            if not student:
                                student = Student_Data(Student_ID=row['Student_ID'], Name=row['Name'],
                                                       Preference=row['Preference'], Status=row['Status'],
                                                       company_id=None)
                                db.session.add(student)
                                db.session.commit()
                            else:
                                continue
                    return redirect('/')
                else:
                    return f"<script> alert('The columns in the excel file does not match the columns in the table'); window.history.back(); </script>"
            else:
                return f"<script> alert('The file is not in excel format'); window.history.back(); </script>"
        except IntegrityError:
            print("record already exists")
            db.session.rollback()
            return redirect('/')

    elif company_data:
        try:
            if company_data.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                company_df = pd.read_excel(company_data)

                if set(company_df.columns) == set(
                        ['Company_Name', 'Job_Role', 'Company_Contact', 'Email']):
                    for index, row in company_df.iterrows():
                        company = Company_Data(Company_Name=row['Company_Name'],
                                               Job_Role=row['Job_Role'], Company_Contact=row['Company_Contact'],
                                               Email=row['Email'])
                        db.session.add(company)
                        db.session.commit()
                    return redirect('/')
                else:
                    return f"<script> alert('The columns in the excel file does not match the columns in the table'); window.history.back(); </script>"
            else:
                return f"<script> alert('The file is not in excel format'); window.history.back(); </script>"
        except IntegrityError:
            print("record already exists")
            db.session.rollback()
            return redirect('/')
    else:
        return f"<script> alert('Please upload either student or company data'); window.history.back(); </script>"

@app.route('/')
def index():
    return redirect("/upload_data", code=302)

@app.route('/upload_data')
def upload_data():
    return render_template('upload_data.html')

@app.route('/match_student')
def match_student():
    data = db.session.execute(db.select(Student_Data)).scalars()
    print(data)
    #tasks = Student.query
    #students = Student.query.all()
    return render_template('match_student.html', students=data)



if __name__ == "__main__":
    app.run(port=5221, debug=True)