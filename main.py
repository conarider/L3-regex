import re
import requests

url = 'https://lavrynenko.com/spisok-poddelnyx-email-adresov-generator/'

html_text = requests.get(url).text

reg_email = r"(?<![-._+])(\b[^<>: ][a-zA-Z0-9._-]+[^_.-]@[a-zA-Z]+\.[a-zA-Z]+\b)(?![-_+])"

result = re.findall(reg_email, html_text)

print("emails:")
for res in result:
  print(res)
