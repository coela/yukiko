import Skype4Py
import time
from handlers import incdec_handler
from handlers import twitter_handler
from handlers import tamaki_handler
from handlers import homeru_handler
from handlers import ihara_handler

class Yukiko:
    def __init__(self):
        pass
    def maharagi(self):
        skype = Skype4Py.Skype(Transport='x11') # Transport="x11"
        skype.RegisterEventHandler('MessageStatus', tamaki_handler.handle)
        skype.RegisterEventHandler('MessageStatus', twitter_handler.handle)
        skype.RegisterEventHandler('MessageStatus', incdec_handler.handle)
        skype.RegisterEventHandler('MessageStatus', homeru_handler.handle)
#       skype.RegisterEventHandler('MessageStatus', ihara_handler.handle)
        skype.Attach()
        while True:
            time.sleep(1) 
