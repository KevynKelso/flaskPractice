import unittest
from app import plus
from unittest.mock import patch

class BasicTests(unittest.TestCase):


    def test_app_output_is_correct(self):
            plus()
            self.assertEqual(plus, sum(num1,num2))


    def test_app_input_is_number(self):
            self.assertEqual(num1, int)
            self.assertEqual(num2, int)


    def test_plus_success(self):
        with patch('app.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            plus_response = plus()

            assert mock_post.called
            self.assertEqual(plus_response.status_code, 200)
