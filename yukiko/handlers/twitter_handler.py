# -*- coding:utf-8 -*-
import re
import urllib2
import BeautifulSoup

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
            hoge = twitter_text.replace('&#10;',"\n")
            msg.Chat.SendMessage(
                hoge + u'\n[' + twitter_time + ']'
                )



