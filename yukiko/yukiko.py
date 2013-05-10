import Skype4Py
import time
from handlers import tamaki_handler
from handlers import ihara_handler

class Yukiko:
    def __init__(self):
        pass
    def maharagi(self):
        skype = Skype4Py.Skype() # Transport="x11"
        skype.RegisterEventHandler('MessageStatus', tamaki_handler.handle)
        skype.RegisterEventHandler('MessageStatus', ihara_handler.handle)
        skype.Attach()
        while True:
            time.sleep(1) 
