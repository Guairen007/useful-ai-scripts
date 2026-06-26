import re

input_file = "input.txt"
output_file = "emails.txt"

# Basic email matching pattern
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

emails = sorted(set(re.findall(email_pattern, text)))

with open(output_file, "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print(f"Extracted {len(emails)} unique emails.")