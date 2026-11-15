from pathlib import Path
import os
import csv
import src




prj_path = Path.joinpath(Path.cwd() / 'CSV_Data_Cleaner')
in_path = Path.joinpath(prj_path / 'input')
out_path = Path.joinpath(prj_path / 'output')
total_records = 0
cleaned_records = 0
invalid_records = 0
duplicate_records = 0

with open(os.path.join(in_path, 'customers.csv'), 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        total_records += 1
        id_clean = src.id_cleaner(i['customer_id'])
        if src.id_validate(id_clean):
            customer_id = id_clean
        else:
            customer_id = None
        name_cln = src.nm_cleaner(i['name'])
        if name_cln:
            name = name_cln
        else:
            name = None
        email = src.email_cleaner(i['email'])
        email_validate = src.email_validate(email)
        if email_validate:
            email = email
        else:
            email = None
        phone = i['phone']
        phone_validate = src.pn_validate(phone)
        city_cln = src.city_cleaner(i['city'])
        if city_cln:
            city = city_cln
        else:
            city = None


        if not email or not name:
            invalid_records += 1
            src.invalid_writer(customer_id, name, email, phone, city)
            src.log_gen('Invalid Record Add', 'Success')
        else:
            if not city:
                status = 'City is missing'
            else:
                status = 'Valid'
            #duplicate check
            result = src.dup_checker(str(customer_id))
            if result:
                duplicate_records += 1
                src.dup_writer(customer_id, name, email, phone, city, status)
                src.log_gen('Duplicate Record Add', 'Success')
            else:
                cleaned_records += 1
                src.clean_writer(customer_id, name, email, phone, city, status)
                src.log_gen('Clean Record Add', 'Success')

rep_dict = {
    "total_records" : total_records,
    "cleaned_records" : cleaned_records,
    "invalid_records" : invalid_records,
    "duplicate_records" : duplicate_records
}

result = src.json_writer(rep_dict)
src.log_gen('JSON Report Generate', 'Success')

print(result)