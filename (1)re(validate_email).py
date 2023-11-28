import re
def extract_emails(text):
    # Define a regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all email addresses in the text
    emails = re.findall(email_pattern, text)

    return emails

def validate_email(email):
    # Define a regular expression pattern for validating email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.match to check if the email matches the pattern
    return re.match(email_pattern, email) is not None

# Example usage
text_to_search = "Contact us at john.doe@example.com or support@company.com for assistance."

# Extracting emails from the text
extracted_emails = extract_emails(text_to_search)
print("Extracted Emails:", extracted_emails)

# Validating each extracted email
for email in extracted_emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")



































