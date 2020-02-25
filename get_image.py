import requests, json, re, os
import hashlib
import lxml.html as html
#from lxml.html import parse, fromstring

img_url = 'https://obd-memorial.ru/html/getimageinfo?id=70782617'
response = requests.post(img_url)
response_dict = json.loads(response.text)
print(len(response_dict))

