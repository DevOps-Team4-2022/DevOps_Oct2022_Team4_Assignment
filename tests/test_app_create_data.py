import unittest
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import *


class TestCreateStudentData(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_columns(self):
        student_data = Student_Data.__table__
        columns = student_data.columns.keys()
        self.assertEqual(columns, ['Student_ID', 'Name', 'Preference', 'Status', 'company_id'])

    def test_primary_key(self):
        student_data = Student_Data.__table__
        pk = student_data.primary_key.columns.keys()
        self.assertEqual(pk, ['Student_ID'])

    def test_repr_method(self):
        student = Student_Data(Student_ID='S12345678', Name='John Smith', Preference='Software Development', Status='Unassigned')
        self.assertEqual(str(student), "<Student ID: 'S12345678'>")
        student.Status = 'Pending confirmation'
        # check again if student id is still S12345678
        # after student's status change from 'Unassigned' to 'Pending confirmation'
        self.assertEqual(str(student), "<Student ID: 'S12345678'>")

    def setUp(self):
        self.student = Student_Data(Student_ID='12345678', Name='Sum Ting Wong', Preference='System Development',
                                    Status='Pending confirmation')

    def test_student_id(self):
        self.assertEqual(self.student.Student_ID, '12345678')

    def test_name(self):
        self.assertEqual(self.student.Name, 'Sum Ting Wong')

    def test_preference(self):
        self.assertEqual(self.student.Preference, 'System Development')

    def test_status(self):
        self.assertEqual(self.student.Status, 'Pending confirmation')

    # test if data already exists in database if not add it, can only be tested locally atm
    # def test_add_student_data_if_not_exists(self):
    #     with app.app_context():
    #         result = Student_Data.query.filter_by(Student_ID='12345678').first()
    #         if result is None:
    #             student = Student_Data(Student_ID='12345678', Name='Sum Ting Wong', Preference='System Development',
    #                                    Status='Pending confirmation')
    #             db.session.add(student)
    #             db.session.commit()
    #             result = Student_Data.query.filter_by(Student_ID='12345678').first()
    #             self.assertEqual(result.Name, 'Sum Ting Wong')
    #             self.assertEqual(result.Preference, 'System Development')
    #             self.assertEqual(result.Status, 'Pending confirmation')
    #         else:
    #             self.assertEqual(result.Name, 'Sum Ting Wong')
    #             self.assertEqual(result.Preference, 'System Development')
    #             self.assertEqual(result.Status, 'Pending confirmation')


class TestCreateCompanyData(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_columns(self):
        company_data = Company_Data.__table__
        columns = company_data.columns.keys()
        self.assertEqual(columns, ['Company_ID','Company_Name', 'Job_Role', 'Company_Contact', 'Email'])

    def test_primary_key(self):
        company_data = Company_Data.__table__
        pk = company_data.primary_key.columns.keys()
        self.assertEqual(pk, ['Company_ID'])

    def test_repr_method(self):
        company = Company_Data(Company_ID=1, Company_Name='A inc.', Job_Role='Software Engineer', Company_Contact='John Smith', Email='john@abc.com')
        self.assertEqual(str(company), "<Company_ID: 1>")
        company.Email = 'john@abc.com'
        self.assertEqual(str(company), "<Company_ID: 1>")

    def setUp(self):
        self.company = Company_Data(Company_Name='B inc.', Job_Role='Software Engineer', Company_Contact='Sum Ting Wong', Email='sum@abc.com')

    def test_company_name(self):
        self.assertEqual(self.company.Company_Name, 'B inc.')

    def test_job_role(self):
        self.assertEqual(self.company.Job_Role, 'Software Engineer')

    def test_company_contact(self):
        self.assertEqual(self.company.Company_Contact, 'Sum Ting Wong')

    def test_email(self):
        self.assertEqual(self.company.Email, 'sum@abc.com')


if __name__ == '__main__':
    unittest.main()