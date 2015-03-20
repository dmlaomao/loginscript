#-*- coding: utf-8 -*-
import urllib2,urllib
import re
import hashlib


username=''
userpwd=''
CALG='12345678'
PID='1'
url='http://10.3.8.211/'


def get_encrypted_pwd():
	tempChar=PID+userpwd+CALG
	md5_pwd=hashlib.md5(tempChar).hexdigest()
	encrypted_pwd=md5_pwd+CALG+PID
	return encrypted_pwd

param={'DDDDD':username,
        'upass':get_encrypted_pwd(),
        'R1':'0',
        'R2':'1',
        'para':'00',
        'OMKKey':'123456'
        }
    
data=urllib.urlencode(param)
try:
    ret=urllib2.urlopen(url,data)
except Exception as e:
	print('Unable to connect to 10.3.8.211')
	exit(1)
pat='mcode'
result=re.findall(pat,ret.read())
if result:
	print('Login successfully!')
else:
	print('Login Error!Account or Password is Wrong.')