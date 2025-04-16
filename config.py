import os

email_files = [f for f in os.listdir('email_data') if f.endswith('.msg')]
excel_files = [f for f in os.listdir('excel_data') if f.endswith('.xlsx')]