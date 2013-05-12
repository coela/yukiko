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
            soup = BeautifulSoup.BeautifulSoup(html,convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
            twitter_context = soup.find("div", attrs={"class": "content"})
            twitter_textArray = twitter_context.find("p", attrs={"class": "js-tweet-text"})
            twitter_text = u''.join(twitter_textArray.findAll(text=True))
            twitter_time = twitter_context.find("a",attrs={"class": "tweet-timestamp js-permalink js-nav"})['title']
            msg.Chat.SendMessage(
                twitter_text + u'\n[' + twitter_time + ']'
                )

