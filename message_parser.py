import os
from message_extractor import extract_message
import anthropic
import io
from contextlib import redirect_stdout
from dotenv import load_dotenv

load_dotenv()

def parse_message():
    # Get the message content from the return value of extract_message
    message_content_list = extract_message()
    
    # Check if we got content
    if message_content_list:
        message_content = "\n".join(message_content_list)
        print("DEBUG - Extracted content:")
        print(message_content)
    else:
        message_content = "No message content extracted"
        print("DEBUG - No content extracted from extract_message()")
    
    client = anthropic.Anthropic(
        api_key=os.environ['ANTHROPIC_API_KEY'],
    )
    
    print("DEBUG - Sending the following content to Claude:")
    print(message_content)
    
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=0,
        system="Extract the name, email address, phone number, and organization from this message as a csv with headers. Format should be 'name,email,phone,organization'. If the name, email address, phone number, or organization is missing, leave the corresponding column in the csv blank. Your entire response should be only the CSV data with no additional text.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message_content
                    }
                ]
            }
        ]
    )
    
    print("DEBUG - Claude's response:")
    print(message.content)
    
    return message.content

# Call the function if this file is run directly
if __name__ == "__main__":
    parse_message()