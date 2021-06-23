# Create a class method named 'validate', which should
# be called from the '__init__' method to validate parameter
# email, passed to the constructor.
# The logic inside the 'validate' method could be
# to check if the passed email parameter is a valid email string.
import re


class MyEmail:
    def __init__(self, email_name):
        self.email_name = email_name

    @property
    def validate(self):
        regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

        if re.search(regex, self.email_name):
            return self.email_name
        else:
            return None


my_email_1 = MyEmail('roman.povzyk@gmail.com')
my_email_2 = MyEmail('roman?povzyk@gmail.com')

print(my_email_1.validate)
print(my_email_2.validate)
