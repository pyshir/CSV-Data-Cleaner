from pathlib import Path
import os, csv, json
from datetime import datetime


abs_path = os.path.abspath('CSV_Data_Cleaner')

def invalid_writer(customer_id, name, email, phone, city):    
    file_path = Path(abs_path) / 'output' / 'invalid_customers.csv'
    is_empty = not file_path.exists() or Path(file_path).stat().st_size == 0
    fieldnames = ['customer_id', 'name', 'email', 'phone', 'city']
    file_dict = {
        fieldnames[0] : customer_id,
        fieldnames[1] : name,
        fieldnames[2] : email,
        fieldnames[3] : phone,
        fieldnames[4] : city
    }
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f,
            fieldnames = fieldnames
        )
        if is_empty:
            writer.writeheader()
            writer.writerow(file_dict)
        else:
            writer.writerow(file_dict)

def dup_checker(cutomer_id):
    file_path = Path(abs_path) / 'output' / 'clean_customers.csv'
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i in reader:
            if cutomer_id == i['customer_id']:
                return True

        return False

def dup_writer(customer_id, name, email, phone, city, status):
    file_path = Path(abs_path) / 'output' / 'duplicate_records.csv'
    is_empty = not file_path.exists() or Path(file_path).stat().st_size == 0
    fieldnames = ['customer_id', 'name', 'email', 'phone', 'city', 'status']
    file_dict = {
        fieldnames[0] : customer_id,
        fieldnames[1] : name,
        fieldnames[2] : email,
        fieldnames[3] : phone,
        fieldnames[4] : city,
        fieldnames[5] : status
    }
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )
        if is_empty:
            writer.writeheader()
            writer.writerow(file_dict)
        else:
            writer.writerow(file_dict)

def clean_writer(customer_id, name, email, phone, city, status):
    file_path = Path(abs_path) / 'output' / 'clean_customers.csv'
    is_empty = not file_path.exists() or Path(file_path).stat().st_size == 0
    fieldnames = ['customer_id', 'name', 'email', 'phone', 'city', 'status']
    file_dict = {
        fieldnames[0] : customer_id,
        fieldnames[1] : name,
        fieldnames[2] : email,
        fieldnames[3] : phone,
        fieldnames[4] : city,
        fieldnames[5] : status
    }
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )
        if is_empty:
            writer.writeheader()
            writer.writerow(file_dict)
        else:
            writer.writerow(file_dict)

def json_writer(report_list):
    result = json.dumps(
        report_list,
        indent= 4,
        ensure_ascii=False
    )
    return result

def log_gen(activity, status):
    file_path = Path(abs_path) / 'output' / 'cleaning_log.txt'
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = f'{time}    {activity}    {status}\n'
    with open(file_path, 'a') as f:
        f.write(data)



