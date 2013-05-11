#-*- coding:utf-8 -*-

import re
import urllib2
import BeautifulSoup

timeout = 10

def handle(msg, event):
    if event == u"RECEIVED":
        if re.search(u'ガンダム', msg.Body):
            msg.Chat.SendMessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.Body):
            opener = urllib2.build_opener()
            opener.addheaders = [('user-agent', 'mozilla/5.0')]
            msg.Chat.SendMessage(
                BeautifulSoup.BeautifulSoup(
                    opener.open(msg.Body,None,timeout)
                    ).title.string.replace('&#10;',"")
                )
        elif re.match(u'\#v-max', msg.Body):
            msg.Chat.SendMessage(u"レディ")

