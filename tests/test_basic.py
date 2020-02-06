# B/c coverage doesn't include these in sys.path
import sys
import unittest
import my_app
import json
from utils import plus
from unittest.mock import patch

sys.path.append('../../myflaskproject')
sys.path.append('../../myflaskproject/app')

class BasicTests(unittest.TestCase):

    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()


    def test_util_plus_output_is_correct(self):
        num1 = 3
        num2 = 2
        sum1 = plus(num1,num2)
        self.assertEqual(sum1, 5)


    def test_util_plus_decimal(self):
        num1 = 3.5
        num2 = 2
        sum1 = plus(num1,num2)
        self.assertEqual(sum1, 5.5)


    def test_app_get_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_app_post_data(self):
        response = self.app.post('/',data={'num1': '5','num2': '2'})
        self.assertEqual(response.status_code, 200)

