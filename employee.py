import requests

class Employee:

    raise_amb = 1.05

    def __init__(self, username, lastname, pay):
        self.username = username
        self.lastname =lastname
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.username, self.lastname)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.username, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amb)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{ self.lastname }/{ month }')

        return response.text if response.ok else 'Bad response'