#-*- coding:utf-8 -*-

import sys
import re
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

inc = re.compile(r'([^-+\s]+)\+\+(\+*)$')
dec = re.compile(r'([^-+\s]+)\-\-(\-*)$')

def handle(msg, event):
    if event == u"RECEIVED":
        print msg.Body
        incmatch = inc.match(msg.Body)
        if incmatch:
            print incmatch.group(1)
            score.setdefault(incmatch.group(1), 0)
            mojinaga = 0
            if ( incmatch.group(2)):
                mojinaga = len(incmatch.group(2))
            score[incmatch.group(1)] += ( 1 + mojinaga)
            f2 = file('data/score.dump', 'w')
            pickle.dump(score, f2)
            f2.close()
            msg.Chat.SendMessage(u'( ' + incmatch.group(1) + u': 累計 ' + str(score[incmatch.group(1)]) + u' )' )

        decmatch = dec.match(msg.Body)
        if decmatch:
            print decmatch.group(1) 
            score.setdefault(decmatch.group(1), 0)
            mojinaga = 0
            if ( decmatch.group(2)):
                print decmatch.group(2) 
                mojinaga = len(decmatch.group(2))
            score[decmatch.group(1)] -= (1 + mojinaga)
            f2 = file('data/score.dump', 'w')
            pickle.dump(score, f2)
            f2.close()
            msg.Chat.SendMessage(u'( ' + decmatch.group(1) + u': 累計 ' + str(score[decmatch.group(1)]) + u' )' )
