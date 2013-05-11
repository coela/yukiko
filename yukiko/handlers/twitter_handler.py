# -*- coding:utf-8 -*-
import re
import urllib2
import beautifulsoup

timeout = 10

def handle(msg, event):
    if event == u"received":
        elif re.match(u'http', msg.body):
            opener = urllib2.build_opener()
            opener.addheaders = [('user-agent', 'mozilla/5.0')]
						html = opener.open(msg.body,None,timeout)
						soup = BeautifulSoup.BeautifulSoup(html)
						twitter_context = soup.find("div", attrs={"class": "content"})
						twitter_textArray = twitter_context.findAll("p", attrs={"class": "js-tweet-text"},text=True)
						twitter_text = u''.join(twitter_textArray)
						twitter_time = twitter_context.find("p",attrs={"class": "tweet-timestamp js-permalink js-nav"}['title'] )

            msg.chat.sendmessage(
                beautifulsoup.beautifulsoup(
									twitter_text + u'[' + twitter_time + ']'
                )

