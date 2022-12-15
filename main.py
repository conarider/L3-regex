import re
import requests

url = 'https://lavrynenko.com/spisok-poddelnyx-email-adresov-generator/'

html_text = requests.get(url).text

reg_email = r"(?<![-._+])(\b[^<>: ][a-zA-Z0-9._-]+[^_.-]@[a-zA-Z]+\.[a-zA-Z]+\b)(?![-_+])"

result = re.findall(reg_email, html_text)

with open("emails.html", 'w') as f:
  f.write(html_text)

with open("emails.txt", 'w') as f:
  for res in result:
    f.write(res + "\n")
