#-*- coding:utf-8 -*-

import os, sys
path = os.path.abspath(os.path.dirname(__file__)) + '/..'
sys.path.append(path)

from yukiko import yukiko

def main():
    _yukiko = yukiko.Yukiko()
    _yukiko.maharagi()

if __name__ == "__main__":
    main()
