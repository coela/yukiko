#-*- coding:utf-8 -*-

import sys
import re
import urllib2
import BeautifulSoup
try:
    import cPickle as pickle
except:
	  import pickle


try:
    f = file('data/score.dump', 'r')
    score = pickle.load(f)
    f.close()
except:
    score = {}

timeout = 10

inc = re.compile(r'(\S+)\+\+')
dec = re.compile(r'(\S+)\-\-')

def handle(msg, event):
    if event == u"RECEIVED":
        if re.search(u'ガンダム', msg.Body):
            msg.Chat.SendMessage(u"俺がガンダムだ")
        elif re.match(u'http', msg.Body):
            msg.Chat.SendMessage(
                BeautifulSoup.BeautifulSoup(
                    urllib2.urlopen(msg.Body,None,timeout)
                    ).title.string
                )
        elif re.match(u'\#V-MAX', msg.Body):
            msg.Chat.SendMessage(u"レディ")

        incmatch = inc.search(msg.Body)
        if incmatch:
            print incmatch.group(1)
            score.setdefault(incmatch.group(1), 0)
            score[incmatch.group(1)] += 1
            f2 = file('data/score.dump', 'w')
            pickle.dump(score, f2)
            f2.close()
            msg.Chat.SendMessage(u'( ' + incmatch.group(1) + u': 累計 ' + str(score[incmatch.group(1)]) + u' )' )

        decmatch = dec.search(msg.Body)
        if decmatch:
            print decmatch.group(1) 
            score.setdefault(decmatch.group(1), 0)
            score[decmatch.group(1)] -= 1
            f2 = file('data/score.dump', 'w')
            pickle.dump(score, f2)
            f2.close()
            msg.Chat.SendMessage(u'( ' + decmatch.group(1) + u': 累計 ' + str(score[decmatch.group(1)]) + u' )' )
