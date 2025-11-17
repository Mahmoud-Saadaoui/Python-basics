import re

# Searching for Patterns
text = "My email is test@example.com"
pattern = r"\S+@\S+"
match = re.search(pattern, text)
print(match.group())    # test@example.com

# Finding All Matches
text = "Tags: #python #coding #dev"
pattern = r"#\w+"
tags = re.findall(pattern, text)
print(tags)  # ['#python', '#coding', '#dev']

# Replacing Text
text = "Call me at 555-123-9876"
clean = re.sub(r"\d", "*", text)
print(clean)  # Call me at ***-***-****

# Validating Input
email = "hello@mail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# Using Groups
text = "Name: John Doe, Age: 28"
pattern = r"Name:\s(.+),\sAge:\s(\d+)"
match = re.search(pattern, text)
print(match.group(1))  # John Doe
print(match.group(2))  # 28


