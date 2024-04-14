
import random
import string
import logging as logger
from html.parser import HTMLParser


def generate_random_email_and_password(domain=None, email_prefix=None):
    
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'
    
    random_email_string_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase, k = random_email_string_length))
    
    email = email_prefix + '_' + random_string + '@' + domain
    
    logger.info(f"Generate random email: {email}")
    
    rand_password_length = 20
    rand_password = ''.join(random.choice(string.ascii_lowercase, k = rand_password_length))

    rand_info = {"email": email, "password": rand_password}

    return rand_info






# 
# def generate_random_email_and_password(domain=None, email_prefix=None):
# 
#     if not domain:
#         domain = 'supersqa.com'
#     if not email_prefix:
#         email_prefix = 'testuser'
# 
#     random_email_string_length = 10
#     random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
# 
#     email = email_prefix + '_' + random_string + '@' + domain
# 
#     logger.info(f"Generated random email: {email}")
# 
#     rand_psswd_length = 20
#     rand_password = ''.join(random.choices(string.ascii_letters, k=rand_psswd_length))
# 
#     random_info = {"email": email, "password": rand_password}
# 
#     return  random_info
# 
# def convert_html_to_text(input_html_string):
#     # define a class used to convert html to text
#     class HTMLFilter(HTMLParser):
#         text = ""
# 
#         def handle_data(self, data):
#             self.text += data
# 
#     f = HTMLFilter()
#     f.feed(input_html_string)
#     return f.text
