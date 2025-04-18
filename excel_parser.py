import os
import pandas as pd
from excel_extractor import extract_excel
import anthropic
import io
from contextlib import redirect_stdout
from dotenv import load_dotenv

load_dotenv()

def parse_excel():
    # Capture the output of extract_excel function using StringIO
    f = io.StringIO()
    with redirect_stdout(f):
        extract_excel()
    
    # Get converted CSV files
    csv_files = [f for f in os.listdir('excel_data') if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found after extraction")
        return
    
    # Process each CSV file
    for csv_file in csv_files:
        csv_path = os.path.join('excel_data', csv_file)
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Convert dataframe to string for API input
        csv_content = df.to_csv(index=False)
        
        print(f"DEBUG - Processing {csv_file}")
        print("DEBUG - First 200 characters of CSV content:")
        print(csv_content[:200])
        
        # Initialize Anthropic client
        client = anthropic.Anthropic(
            api_key=os.environ['ANTHROPIC_API_KEY'],
        )
        
        # Define system prompt to match message_parser format
        system_prompt = """
        Extract the name, email address, phone number, and organization from this Excel data as a csv with headers.
        Format should be 'name,email,phone,organization'.
        If the name, email address, phone number, or organization is missing, leave the corresponding column in the csv blank.
        Your entire response should be only the CSV data with no additional text.
        """
        
        # Send to Claude API
        message = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1000,
            temperature=0,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Here is a CSV file named {csv_file}:\n\n{csv_content}"
                        }
                    ]
                }
            ]
        )
        
        print(f"DEBUG - Claude's analysis of {csv_file}:")
        print(message.content)
        
if __name__ == "__main__":
    parse_excel()