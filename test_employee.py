import unittest
from unittest.mock import patch

from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        self.emp_1 = Employee('victor', 'augusto', 200)
        self.emp_2 = Employee('kikita', 'costa', 300)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEquals(self.emp_1.email, 'victor.augusto@email.com')
        self.assertEquals(self.emp_2.email, 'kikita.costa@email.com')


    def test_full_name(self):
        self.assertEqual(self.emp_1.full_name, 'victor augusto')
        self.assertEqual(self.emp_2.full_name, 'kikita costa')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 210)
        self.assertEqual(self.emp_2.pay, 315)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/augusto/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/costa/June')
            self.assertEqual(schedule, 'Bad response')
            

if __name__ == '__main__': unittest.main()