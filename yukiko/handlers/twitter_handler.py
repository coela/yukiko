# -*- coding:utf-8 -*-
import re
import urllib2
import BeautifulSoup
import xml.parsers.expat

timeout = 10

def handle(msg, event):
    if event == u"RECEIVED":
        if re.match(u'https://twitter.com/[^\/]+/status/', msg.Body):
            opener = urllib2.build_opener()
            opener.addheaders = [('user-agent', 'mozilla/5.0')]
            html = opener.open(msg.Body,None,timeout)
            soup = BeautifulSoup.BeautifulSoup(html)
            twitter_context = soup.find("div", attrs={"class": "content"})
            twitter_textArray = twitter_context.find("p", attrs={"class": "js-tweet-text"})
            twitter_text = u''.join(twitter_textArray.findAll(text=True))
            twitter_time = twitter_context.find("a",attrs={"class": "tweet-timestamp js-permalink js-nav"})['title']
            hoge = unescape(twitter_text)
            msg.Chat.SendMessage(
                hoge + u'\n[' + twitter_time + ']'
                )


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

