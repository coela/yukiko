#-*- coding:utf-8 -*-

import re
import urllib
import BeautifulSoup

def handle(msg, event):
    if event == u"RECEIVED":
        if re.search(u'ガンダム', msg.Body):
            msg.Chat.SendMessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.Body):
            msg.Chat.SendMessage(
                BeautifulSoup.BeautifulSoup(
                    urllib.urlopen(msg.Body)
                    ).title.string
                )
        elif re.match(u'\#V-MAX', msg.Body):
            msg.Chat.SendMessage(u"レディ")
