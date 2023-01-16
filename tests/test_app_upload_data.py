# This test can only be run locally after the app is run via app.py


# import unittest
# import sys, os, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
# from unittest.mock import MagicMock, patch
# from app import *
# import io
#
# class TestUpload(unittest.TestCase):
#     def setUp(self):
#         self.app = app
#         self.client = self.app.test_client()
#         self.student_data = MagicMock()
#         self.student_data.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         self.student_data.read.return_value = b'Student_ID,Name,Preference,Status\nS1234567,John Smith,Software Development,Unassigned\n'
#         self.company_data = MagicMock()
#         self.company_data.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         self.company_data.read.return_value = b'Company_Name,Job_Role,Company_Contact,Email\nACME Inc,Software Developer,Jane Doe,jane.doe@acme.com\n'
#
#     def test_upload_student_data(self):
#         # create a mock file object
#         mock_file = io.BytesIO(b"some file content")
#         mock_file.name = "dummy_student_data.xlsx"
#         # pass mock_file as the value of the 'internship_student_data' file parameter
#         with self.app.test_client() as client:
#             response = client.post('/upload', data={'internship_student_data': (mock_file, 'dummy_student_data.xlsx')})
#             self.assertEqual(response.status_code, 302)
#             self.assertEqual(response.location, 'http://127.0.0.1:5000/')
#             # check if student data was added to the database
#             student = Student_Data.query.filter_by(Student_ID='S0194725').first()
#             self.assertIsNotNone(student)
#             self.assertEqual(student.Name, 'Lau Kai Feng')
#             self.assertEqual(student.Preference, 'Software Engineering, Development')
#             self.assertEqual(student.Status, 'Unassigned')
#
#     def test_upload_company_data(self):
#         # create a mock file object
#         mock_file = io.BytesIO(b"some file content")
#         mock_file.name = "dummy_company_data.xlsx"
#         # pass mock_file as the value of the 'internship_student_data' file parameter
#         with self.app.test_client() as client:
#             response = client.post('/upload', data={'internship_company_data': (mock_file, 'dummy_company_data.xlsx')})
#             self.assertEqual(response.status_code, 302)
#             self.assertEqual(response.location, 'http://127.0.0.1:5000/')
#             # check if student data was added to the database
#             company = Student_Data.query.filter_by(Company_Name='A inc.').first()
#             self.assertIsNotNone(company)
#             self.assertEqual(company.Job_Role, 'Software Engineer')
#             self.assertEqual(company.Company_Contacts, 'John Smith')
#             self.assertEqual(company.Email, 'john@abc.com')
#
#     def test_upload_invalid_data(self):
#         with self.app.test_request_context(method='POST', data={'internship_student_data': self.company_data}):
#             response = upload()
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.data, b'The columns in the excel file does not match the columns in the table')