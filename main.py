import re
import requests

url = 'https://lavrynenko.com/spisok-poddelnyx-email-adresov-generator/'
#url'https://dudom.ru/kompjutery/adresa-jelektronnoj-pochty-spisok-primer/'

url2= 'https://myshows.me/login/'


html_text = requests.get(url).text
html_text2 = requests.get(url2).text


reg_email = r"(?<![-._+])(\b[^<>: ][a-zA-Z0-9._-]+[^_.-]@[a-zA-Z]+\.[a-zA-Z]+\b)(?![-_+])"
reg_link= r"(?<=\")((http|https)://\S+)(?=\")"

result = re.findall(reg_email, html_text)
result2 = re.findall(reg_link, html_text2)


print("emails:")
for res in result:
  print(res)

print("\nhyperlinks:")
for res in result2:
  print(res[0])
