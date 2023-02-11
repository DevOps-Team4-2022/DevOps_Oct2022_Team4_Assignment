import unittest
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from app import *


class TestMatchStudent(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_match_student(self):
        with app.app_context():
            # Create a test database
            studentResult = Student_Data.query.filter_by(Student_ID='9999999').first()
            if studentResult is None:
                student = Student_Data(Student_ID='9999999', Name='testStudent', Preference='testPreference',
                                       Status='Unassigned')
                db.session.add(student)
                db.session.commit()

            companyResult = Company_Data.query.filter_by(Company_Name='Test Inc').first()
            if companyResult is None:
                company = Company_Data(Company_ID='10000', Company_Name='Test Inc', Job_Role='TestDevelopment',
                                       Company_Contact='555-555-5555', Email='testinc@example.com')
                db.session.add(company)
                db.session.commit()

            # test if the student is matched with the company by changing status and company id
            studentResult = Student_Data.query.filter_by(Student_ID='9999999').first()
            companyResult = Company_Data.query.filter_by(Company_ID='10000').first()
            studentResult.Status = 'Pending confirmation'
            studentResult.Company_ID = companyResult.Company_ID
            db.session.commit()
            self.assertEqual(studentResult.Status, 'Pending confirmation')
            self.assertEqual(studentResult.Company_ID, 10000)


    def tearDown(self):
        with app.app_context():
            studentResult = Student_Data.query.filter_by(Student_ID='9999999').first()
            companyResult = Company_Data.query.filter_by(Company_ID='10000').first()
            if studentResult is not None:
                db.session.delete(studentResult)
                db.session.commit()

            if companyResult is not None:
                db.session.delete(companyResult)
                db.session.commit()
