import re

def id_validate(customer_id):
    if str(customer_id).isdigit():
        return True
    else:
        return False

def email_validate(email):
    result = re.search(r'^([\w]+[\.\_\-\+]?)+\w\@\w+(\.\w+)+$', email)
    if result:
        return True
    else:
        return False

def pn_validate(phone):
    result = re.search(r'\d+', phone)
    if result:
        return True
    else:
        return False