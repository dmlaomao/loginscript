# -*- coding: utf-8 -*-

'a login script'

__author__ = 'dmlaomao'

import sys
import urllib2
import urllib
import cookielib
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
            return data
            print 'You have successfully logined'
        except Exception,e:
            print str(e)
            print 'login failed'

argv = sys.argv
print campuslogin(argv[1],argv[2])
