import unittest
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from app import *



class TestPrepareEmail(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
    
    def test_prepare_email(self):
        print("Running test_prepare_email()...")
        with app.app_context():
            # simulate a POST request with form data
            student_id = 'S0194725G'
            student_name = 'Lau Kai Feng'
            form_data = {
                'student_id': student_id,
                'student_name': student_name
            }
            response = self.app.post('/prepare_email', data=form_data)
            
            # check if email file was created
            file_name = f"{student_id}_{student_name}_Resume.msg"
            file_path = os.path.join('email', file_name)
            self.assertTrue(os.path.exists(file_path))
            
            # check if success message was returned
            self.assertIn(b'Successfully Generated an Email', response.data)
    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()

