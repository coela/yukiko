import Skype4Py
import sys, time
from handlers import incdec_handler
from handlers import twitter_handler
from handlers import tamaki_handler
from handlers import homeru_handler
from handlers import codon_handler
from handlers import ihara_handler

class Yukiko:
    def __init__(self):
        pass
    def maharagi(self):
        if sys.argv[1] == 'OSX':
            skype = Skype4Py.Skype()
        else:
            skype = Skype4Py.Skype(Transport='x11')
        skype.RegisterEventHandler('MessageStatus', tamaki_handler.handle)
        skype.RegisterEventHandler('MessageStatus', twitter_handler.handle)
        skype.RegisterEventHandler('MessageStatus', incdec_handler.handle)
        skype.RegisterEventHandler('MessageStatus', homeru_handler.handle)
        skype.RegisterEventHandler('MessageStatus', codon_handler.handle)
        skype.Attach()
        while True:
            time.sleep(1) 
