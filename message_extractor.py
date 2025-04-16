import os
from config import email_files
import extract_msg

def extract_message():
    if email_files:
        # Create the full path to the first message file
        email_message = email_files[0]
        file_path = os.path.join('email_data', email_message)
        
        # Create an instance of the Message class with the file path
        msg = extract_msg.Message(file_path)
        
        # Create a list of the message properties
        subject = msg.subject
        sender = msg.sender
        date = msg.date
        body = msg.body
        
        # Create a list of the properties with labels
        contents = [
            f"Subject: {subject}",
            f"From: {sender}",
            f"Date: {date}",
            f"Body: {body}"
        ]

        msg.close()
        return contents

    else:
        print("No .msg files found")