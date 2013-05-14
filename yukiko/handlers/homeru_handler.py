#-*- coding:utf-8 -*-

import re
import random
HOMERU_TEXT = [u"「さすが<NAME>っ！おれたちにできない事を平然とやってのけるッ　そこにシビれる！あこがれるゥ！」",
        u"<NAME>さん、素敵です！",
        u"シブイねェ…まったくおたくシブイぜ",
        u"お前がガンダムだ！",
        u"ええぃ！連邦軍の<NAME>は化け物か！"
        ]

def handle(msg, event):
    if event == u"RECEIVED":
       if re.match(u'\#HOMERO', msg.Body):
            random.shuffle(HOMERU_TEXT)
            text = HOMERU_TEXT[0].replace('<NAME>',msg.FromDisplayName)
            msg.Chat.SendMessage(text)
