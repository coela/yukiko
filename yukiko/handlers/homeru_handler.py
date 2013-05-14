#-*- coding:utf-8 -*-

import re

HOMERU_TEXT = ["「さすが<NAME>っ！おれたちにできない事を平然とやってのけるッ　そこにシビれる！あこがれるゥ！」"]

def handle(msg, event):
    if event == u"RECEIVED":
       if re.match(u'\#HOMERO', msg.Body):
            print msg.Body.str

