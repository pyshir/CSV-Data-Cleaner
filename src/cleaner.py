import re

def id_cleaner(customer_id):
    try:
        customer_id = str(customer_id).strip()
        result = re.search(r'\d+', customer_id)
        return int(result.group())
    except:
        return None

def nm_cleaner(name):
    name = str(name).strip().title()
    if name:
        return name
    else:
        return False

def email_cleaner(email):
    return email.strip().lower()

def city_cleaner(city):
    city = city.strip().title()
    if city:
        return city
    else:
        return None