#!/usr/bin/env python

import os
import sys
import time
from os.path import getmtime
from threading import Thread


WATCHED_FILES = [__file__]
WATCHED_FILES_MTIMES = [(f, getmtime(f)) for f in WATCHED_FILES]

closing = False

def watcher():
    while True:
        if closing:
            break
        for f, mtime in WATCHED_FILES_MTIMES:
            if getmtime(f) != mtime:
                time.sleep(.5)
                os.execv(__file__, sys.argv)

        # Wait for inputs and act on them.

watch_thread = Thread(target=watcher)
watch_thread.start()

def getMode():
    mode = ''
    while mode == '':
        inMode = input('Play mode? [n]etworked; [s]tandalone: ')
        if inMode in ('n','s'):
            mode = inMode

getMode()

closing=True
