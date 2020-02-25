import requests, base64, json, re, os
import hashlib
import lxml.html as html
#from lxml.html import parse, fromstring

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
def get_info(id,heareds,cookies):
    info_url = 'https://obd-memorial.ru/html/info.htm?id=4138741'
    res3 = requests.get(info_url,headers=headers,cookies=cookies,allow_redirects = True)
    #print(res3.text)
    doc = html.fromstring(res3.text)
    #print(doc.find_class('card_parameter'))
    for div in doc.find_class('card_parameter'):
        #print()
        print ('%s: %s' % (div.getchildren()[0].text_content(), div.getchildren()[1].text_content()))
    return True

#####################################


res1 = requests.get(info_url,allow_redirects = True)
if(res1.status_code==307):
    print(res1.status_code)
    print('*****************')

    cookies = {}
    cookies['3fbe47cd30daea60fc16041479413da2']=res1.cookies['3fbe47cd30daea60fc16041479413da2']
    cookies['JSESSIONID']=res1.cookies['JSESSIONID']
    headers={}
    headers['Cookie'] = make_str_cookie(cookies)
    res2 = requests.get(info_url,headers=headers,cookies=cookies,allow_redirects = True)
    if(res2.status_code==200):
        print(res2.status_code)
        print('*****************')

        #get_info(345,headers,cookies)
        res3 = requests.get(img_url,headers=headers,cookies=cookies,allow_redirects = True)
        if(res3.status_code==200):
            print(res3.status_code)
            data = json.loads(res3.text)
            print(len(data))
            page = data[0]
            src = re.findall(r'src=\"(\S+)\"', str(page))
            img_url="https://cdn.obd-memorial.ru/html/images3?id="+str(page['id'])+"&id1="+(getStringHash(page['id']))+"&path="+src[0]
            print(page['id'])
            print(img_url)
            r = requests.get(img_url,headers=headers,cookies=cookies, allow_redirects=True)
            header = r.headers
            content_length = header.get('content-length', None)
            print(content_length)
            content_type = header.get('content-type')
            '''
            for page in data:
                #print(page['id'])
                src = re.findall(r'src=\"(\S+)\"', str(page))
                if(src):
                    print (src)
                    ids = re.findall(r'id=\"(\d+)\"', str(page))
                    print('%s : %s' % (page['id'],len(ids)))
                    img_url="https://cdn.obd-memorial.ru/html/images3?id="+str(page['id'])+"&id1="+(getStringHash(page['id']))+"&path="+src[0]
                    location = os.path.abspath("./scan/"+str(page['id'])+'.jpg')

                    r = requests.get(img_url,headers=headers,cookies=cookies, allow_redirects=True)
                    open(location, 'wb').write(r.content)

                    print(img_url)
            '''    
#https://cdn.obd-memorial.ru/html/images3?id=70782618&id1=e9b750f3f4568d8f049698151ca6772c&path=Z/011/058-A-0071744-0001/00000001.jpg
#https://cdn.obd-memorial.ru/html/images3?id=70782618&id1=e9b750f3f4568d8f049698151ca6772c&path=Z/011/058-A-0071744-0001/00000001.jpg