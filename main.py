from message_extractor import extract_message
from message_parser import parse_message
from excel_extractor import extract_excel
from excel_parser import parse_excel

def process_all_emails():
    extract_message()
    parse_message

def process_all_excel():
    extract_excel()
    parse_excel()

process_all_emails()