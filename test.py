import requests, base64, json, re
import hashlib


img_url = 'https://obd-memorial.ru/html/getimageinfo?id=70782617&_=1582546278185'

info_url = 'https://obd-memorial.ru/html/info.htm?id=70782617'
#####################################
def make_str_cookie(cookies):
    str_cook = ''
    for key, value in cookies.items():
        str_cook += '{0}={1};'.format(key,value)
    return str_cook

res1 = requests.get(info_url,allow_redirects = True)
print(res1.status_code)
print(res1.cookies)
print('*****************')

cookies = {}
cookies['3fbe47cd30daea60fc16041479413da2']=res1.cookies['3fbe47cd30daea60fc16041479413da2']
cookies['JSESSIONID']=res1.cookies['JSESSIONID']
headers={}
headers['Cookie'] = make_str_cookie(cookies)
res2 = requests.get(info_url,headers=headers,cookies=cookies,allow_redirects = True)
print(res2.status_code)
print(res2.cookies)
print('*****************')


res3 = requests.get(img_url,headers=headers,cookies=cookies,allow_redirects = True)
print(res3.status_code)
#print(res3.text)
data = json.loads(res3.text)
print(str(data[0].id))
src = re.findall(r'src=\"(\S+)\"', str(data[0]))
print (src)
ids = re.findall(r'id=\"(\d+)\"', str(data[0]))
print(len(ids))

h = hashlib.md5(b"password")
p = h.hexdigest()
print(p)
#req="http://obd-memorial.ru/memorial/fullimage?id="+$id_page+"&id1="+( Get-StringHash $id_page)+"&path="+$path_pic

exit(1)

'''
cookies = {}
cookies['3fbe47cd30daea60fc16041479413da2']=res2.cookies['3fbe47cd30daea60fc16041479413da2']
cookies['JSESSIONID']='8C691120DCB05507637ABE7BCC8657F1'
headers={}
headers['Cookie'] = make_str_cookie(cookies)

res3 = requests.get(url, cookies,allow_redirects = True)
print(res3.status_code)
'''
