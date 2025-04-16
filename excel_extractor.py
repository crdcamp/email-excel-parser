import os
import pandas as pd
from config import excel_files

def extract_excel():
    if excel_files:
        for excel_file in excel_files:
            # Create full path to the excel file
            excel_path = os.path.join('excel_data', excel_file)
            
            # Read the Excel file
            df = pd.read_excel(excel_path)
            
            # Create a CSV filename (replace .xlsx with .csv)
            csv_filename = excel_file.replace('.xlsx', '.csv')
            csv_path = os.path.join('excel_data', csv_filename)
            
            # Save as CSV
            df.to_csv(csv_path, index=False)
            print(f"Converted {excel_file} to {csv_filename}")
            
            # Print the dataframe for debugging
            print(df)
    else:
        print("No Excel files found")