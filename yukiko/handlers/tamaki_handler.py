#-*- coding:utf-8 -*-

import re
import urllib2
import BeautifulSoup
import xml.parsers.expat
timeout = 10

KNOWN_ENCODINGS = ["cp932", "shift_jis_2004", "euc-jp-ms",
          "euc_jis_2004", "iso2022-jp-2", "iso2022-jp-3", "iso2022-jp-2004"]

def handle(msg, event):
    if event == u"RECEIVED":
        if re.search(u'ガンダム', msg.Body):
            msg.Chat.SendMessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.Body):
            opener = urllib2.build_opener()
            opener.addheaders = [('user-agent', 'mozilla/5.0')]
            html = opener.open(msg.Body,None,timeout)

            try:
                soup = BeautifulSoup.BeautifulSoup(html,convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
            except (TypeError, UnicodeError):
                soup = testKnownEncodings(html)            

            title = soup.title.string.replace("\n",'')
            msg.Chat.SendMessage(
                    title
               )
        elif re.match(u'\#V-MAX', msg.Body):
            msg.Chat.SendMessage(u"レディ")

def testKnownEncodings(html):
  for e in knownEncodings:
    try:
      soup = BeautifulSoup.BeautifulSoup(html, fromEncoding = e,convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
      return soup
    except (TypeError, UnicodeError):
      pass
