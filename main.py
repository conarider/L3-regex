import re
import requests

url = 'https://lavrynenko.com/spisok-poddelnyx-email-adresov-generator/'
url2= 'https://myshows.me/login/'

html_text = requests.get(url).text
html_text2 = requests.get(url2).text

reg_email = r"(?<![-._+])(\b[^<>: ][a-zA-Z0-9._-]+[^_.-]@[a-zA-Z]+\.[a-zA-Z]+\b)(?![-_+])"
reg_link= r"(?<=\")((http|https)://\S+)(?=\")"

result = re.findall(reg_email, html_text)
result2 = re.findall(reg_link, html_text2)

with open("emails.html", 'w') as f:
  f.write(html_text)


print("emails:")
for res in result:
  print(res)

with open("emails.txt", 'w') as f:
  for res in result:
    f.write(res + "\n")



print("\nhyperlinks:")
for res in result2:
  print(res[0])

with open("links.txt", 'w') as f:
  for res in result2:
    f.write(res[0] + "\n")