#-*- coding:utf-8 -*-

import re
import urllib2
import beautifulsoup

timeout = 10

def handle(msg, event):
    if event == u"received":
        if re.search(u'ガンダム', msg.body):
            msg.chat.sendmessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.body):
            opener = urllib2.build_opener()
            opener.addheaders = [('user-agent', 'mozilla/5.0')]
            msg.chat.sendmessage(
                beautifulsoup.beautifulsoup(
                    opener.open(msg.body,None,timeout)
                    ).title.string
                )
        elif re.match(u'\#v-max', msg.body):
            msg.chat.sendmessage(u"レディ")

