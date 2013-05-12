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
                soup = BeautifulSoup.BeautifulSoup(html)
            except (TypeError, UnicodeError):
                soup = testKnownEncodings(html)            
                soup = BeautifulSoup.BeautifulSoup(html)

            enc = soup.originalEncoding
            title = soup.title.string
            hoge = unescape(title)
            msg.Chat.SendMessage(
                    hoge
               )
        elif re.match(u'\#v-max', msg.Body):
            msg.Chat.SendMessage(u"レディ")

def convert_ascii(m):
    n = int(m.group(1))
    return unichr(n)

def testKnownEncodings(html):
  for e in knownEncodings:
    try:
      soup = BeautifulSoup.BeautifulSoup(html, fromEncoding = e)
      return soup
    except (TypeError, UnicodeError):
      pass


def unescape(s):
    want_unicode = False
    if isinstance(s, unicode):
        s = s.encode("utf-8")
        want_unicode = True

    # the rest of this assumes that `s` is UTF-8
    list = []

    # create and initialize a parser object
    p = xml.parsers.expat.ParserCreate("utf-8")
    p.buffer_text = True
    p.returns_unicode = want_unicode
    p.CharacterDataHandler = list.append

    # parse the data wrapped in a dummy element
    # (needed so the "document" is well-formed)
    p.Parse("<e>", 0)
    p.Parse(s, 0)
    p.Parse("</e>", 1)

    # join the extracted strings and return
    es = ""
    if want_unicode:
        es = u""
    return es.join(list)

