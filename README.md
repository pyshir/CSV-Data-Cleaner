# CSV Data Cleaner

**Author:** pyShir  
**WhatsApp:** 8801309495010

---

## 📌 Project Overview

CSV Data Cleaner is a Python-based project designed to clean, validate, and organize customer data from CSV files.

It processes customer records, validates different fields, detects duplicate entries, separates invalid records, and generates a JSON summary report.

## ✨ Features

- **Customer ID Cleaning:** Cleans and validates customer IDs.
- **Name Cleaning:** Removes unwanted characters and cleans customer names.
- **Email Validation:** Cleans and validates email addresses.
- **Phone Validation:** Checks phone number validity.
- **City Cleaning:** Cleans city names and handles missing values.
- **Invalid Record Detection:** Separates records with missing or invalid required fields.
- **Duplicate Detection:** Identifies duplicate customer records.
- **Clean Data Export:** Saves valid and cleaned customer records.
- **JSON Report Generation:** Generates a summary report in JSON format.
- **Activity Logging:** Records each processing operation with its status.

## 📁 Project Structure

```text
CSV_Data_Cleaner/
│
├── input/
│   └── customers.csv
│
├── output/
│   ├── cleaned.csv
│   ├── invalid.csv
│   ├── duplicates.csv
│   ├── report.json
│   └── app.log
│
├── src/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── validator.py
│   └── reporter.py
│
└── main.py
```

## 📋 Input CSV Format

Your `customers.csv` file should contain the following columns:

```csv
customer_id,name,email,phone,city
101,John Doe,john@example.com,01712345678,Dhaka
102,Jane Smith,jane@example.com,01812345678,Chittagong
103,Bob,bob@example.com,01912345678,Khulna
```

## ⚙️ Requirements

- Python 3.9+
- CSV module (Built-in)
- JSON module (Built-in)
- pathlib (Built-in)
- os (Built-in)

No external packages are required for the basic project.

## 🚀 How to Run

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/CSV_Data_Cleaner.git
```

**2. Navigate to the project directory**

```bash
cd CSV_Data_Cleaner
```

**3. Add your customer CSV file**

Place your `customers.csv` file inside the `input/` directory.

**4. Run the project**

```bash
python main.py
```

## 📊 Processing Summary

After processing, the project generates a JSON report containing:

```json
{
    "total_records": 100,
    "cleaned_records": 80,
    "invalid_records": 10,
    "duplicate_records": 10
}
```

*Note: The numbers above are sample data.*

## 📂 Output Description

| Output File | Description |
|---|---|
| cleaned.csv | Stores cleaned and valid records |
| invalid.csv | Stores invalid customer records |
| duplicates.csv | Stores duplicate customer records |
| report.json | Contains processing statistics |
| app.log | Stores processing activity logs |

## 🔍 Record Classification

- **Valid:** Records containing valid required fields.
- **City is missing:** Records with valid required fields but missing city information.
- **Invalid:** Records with missing or invalid required fields.
- **Duplicate:** Records that already exist in the dataset.

## 🛠️ Technologies Used

- Python
- CSV
- JSON
- pathlib
- File Handling
- Modular Programming

## 👨‍💻 Author

**pyShir**

📱 WhatsApp: 8801309495010

---

⭐ If you find this project useful, don't forget to give it a star on GitHub!

