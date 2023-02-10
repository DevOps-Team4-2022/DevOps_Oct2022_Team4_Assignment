import unittest
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import *
from io import BytesIO
import shutil


class TestUploadStudentData(unittest.TestCase):
    def test_add_student_data_if_not_exists(self):
        with app.app_context():
            result = Student_Data.query.filter_by(Student_ID='12345678').first()
            if result is None:
                student = Student_Data(Student_ID='12345678', Name='Sum Ting Wong', Preference='System Development',
                                       Status='Pending confirmation')
                db.session.add(student)
                db.session.commit()
                result = Student_Data.query.filter_by(Student_ID='12345678').first()
                self.assertEqual(result.Name, 'Sum Ting Wong')
                self.assertEqual(result.Preference, 'System Development')
                self.assertEqual(result.Status, 'Pending confirmation')

    def tearDown(self):
        with app.app_context():
            result = Student_Data.query.filter_by(Student_ID='12345678').first()
            if result is not None:
                db.session.delete(result)
                db.session.commit()

class TestUploadCompanyData(unittest.TestCase):
    def test_add_company_data_if_not_exists(self):
        with app.app_context():
            result = Company_Data.query.filter_by(Company_Name='Acme Inc').first()
            if result is None:
                company = Company_Data(Company_Name='Acme Inc', Job_Role='System Development',
                                       Company_Contact='555-555-5555', Email='acmeinc@example.com')
                db.session.add(company)
                db.session.commit()
                result = Company_Data.query.filter_by(Company_Name='Acme Inc').first()
                self.assertEqual(result.Job_Role, 'System Development')
                self.assertEqual(result.Company_Contact, '555-555-5555')
                self.assertEqual(result.Email, 'acmeinc@example.com')

    def tearDown(self):
        with app.app_context():
            result = Company_Data.query.filter_by(Company_Name='Acme Inc').first()
            if result is not None:
                db.session.delete(result)
                db.session.commit()

class TestUploadFile(unittest.TestCase):
    def setUp(self):
        # Create a dummy file to simulate the uploaded file
        self.dummy_file = BytesIO(b"dummy file content")
        self.dummy_file.seek(0)
        self.dummy_file.filename = "dummy_file.txt"

        folder_path = 'test_folder/uploaded-data/dummy_data'
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

    def test_folder_created(self):
        folder_path = 'test_folder/uploaded-data/dummy_data'
        self.assertFalse(os.path.exists(folder_path))
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.assertTrue(os.path.exists(folder_path))

    def test_file_stored(self):
        folder_path = 'test_folder/uploaded-data/dummy_data'
        file_path = os.path.join(folder_path, self.dummy_file.filename)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(file_path, 'wb') as f:
            f.write(self.dummy_file.read())
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'rb') as f:
            stored_content = f.read()
        self.assertEqual(stored_content, b"dummy file content")

    def tearDown(self):
        folder_path = 'test_folder'
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)