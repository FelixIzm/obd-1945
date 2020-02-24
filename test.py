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
#####################################
def getStringHash(id):
    h = hashlib.md5(str(id).encode()+b'db76xdlrtxcxcghn7yusxjcdxsbtq1hnicnaspohh5tzbtgqjixzc5nmhybeh')
    p = h.hexdigest()
    return str(p)
#####################################

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
print(data[0]['id'])
src = re.findall(r'src=\"(\S+)\"', str(data[0]))
if(src):
    print (src)
    ids = re.findall(r'id=\"(\d+)\"', str(data[0]))
    print(len(ids))
    req="https://cdn.obd-memorial.ru/html/images3?id="+str(data[0]['id'])+"&id1="+(getStringHash(data[0]['id']))+"&path="+src[0]
    print(req)
'''
Function Get-StringHash([String] $String,$HashName = "MD5") {
    $StringBuilder = New-Object System.Text.StringBuilder
    [System.Security.Cryptography.HashAlgorithm]::Create($HashName).ComputeHash([System.Text.Encoding]::UTF8.GetBytes($String+'db76xdlrtxcxcghn7yusxjcdxsbtq1hnicnaspohh5tzbtgqjixzc5nmhybeh'))|%{
        [Void]$StringBuilder.Append($_.ToString("x2"))
    }
    $StringBuilder.ToString()
}

'''

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
