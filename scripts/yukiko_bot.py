#-*- coding:utf-8 -*-

import os, sys
path = os.path.abspath(os.path.dirname(__file__)) + '/..'
sys.path.append(path)

import Skype4Py
import time
from yukiko.handlers import tamaki_handler
from yukiko.handlers import ihara_handler
print tamaki_handler

def main():
    skype = Skype4Py.Skype() # Transport="x11"
    skype.RegisterEventHandler('MessageStatus', tamaki_handler.handle)
    skype.RegisterEventHandler('MessageStatus', ihara_handler.handle)
    skype.Attach()
    # イベントハンドラは別スレッドにて実行されるので、
    # 本スレッドではひたすらsleepしてスクリプトが終了しないようにしておく。
    while True:
        time.sleep(1) 

if __name__ == "__main__":
    main()
