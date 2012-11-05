# encoding: utf-8

import Skype4Py
import time
import re
import urllib
import BeautifulSoup

def handler(msg, event):
    if event == u"RECEIVED":
        if re.search(u'ガンダム', msg.Body):
            msg.Chat.SendMessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.Body):
            msg.Chat.SendMessage(BeautifulSoup.BeautifulSoup(urllib.urlopen(msg.Body)).title.string)
        elif re.match(u'\#V-MAX', msg.Body):
					msg.Chat.SendMessage(u"レディ");

def main():
    skype = Skype4Py.Skype(Transport="x11")
    skype.OnMessageStatus = handler
    skype.Attach()
    # イベントハンドラは別スレッドにて実行されるので、
    # 本スレッドではひたすらsleepしてスクリプトが終了しないようにしておく。
    while True:
        time.sleep(1) 

if __name__ == "__main__":
    main()
