# records both keystrokes and keyboard
# http://stackoverflow.com/questions/12389665/python-capture-keystrokes-values-in-text-file-on-os-x
# http://stackoverflow.com/questions/12389665/python-capture-keystrokes-values-in-text-file-on-os-x
import exceptions
import sys
from Foundation import NSObject, NSLog
from AppKit import NSApplication, NSApp, NSWorkspace
from Cocoa import *
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from PyObjCTools import AppHelper
import keycode
import datetime

# these are the only keys collected
wanted_keys = [ 
    '36', #ENTER/RETURN
    '48', #TAB
    '49', #SPACEBAR
    '51', #DELETE
    '53', #ESC
    '123', #LEFT-ARROW,
    '124', #RIGHT-ARROW
    '125', #DOWN-ARROW
    '126', #UP-ARROW
]

evtypes = dict(
    NSLeftMouseDown     = 1,
    NSLeftMouseUp       = 2,
    NSRightMouseDown    = 3,
    NSRightMouseUp      = 4,
    NSMouseMoved        = 5,
    NSLeftMouseDragged  = 6,
    NSRightMouseDragged = 7,
    NSMouseEntered      = 8,
    NSMouseExited       = 9,
    NSKeyDown           = 10,
    NSKeyUp             = 11,
    NSFlagsChanged      = 12,
    NSAppKitDefined     = 13,
    NSSystemDefined     = 14,
    NSApplicationDefined = 15,
    NSPeriodic          = 16,
    NSCursorUpdate      = 17,
    NSScrollWheel       = 22,
    NSTabletPoint       = 23,
    NSTabletProximity   = 24,
    NSOtherMouseDown    = 25,
    NSOtherMouseUp      = 26,
    NSOtherMouseDragged = 27
)

evtypes_rev = dict([[v,k] for k,v in evtypes.items()])

class Hooker(object):
    def __call__(self, *args, **kwargs):
        try:
            evt = kwargs.get('event')
            del kwargs['event']
            items = [ x[0]+"="+unicode(x[1]) for x in kwargs.iteritems()]
            current_key = 0
            items_len = len(items)
            if items_len >= 3: 
                current_key = str(items[2]).strip("key=")

            # block out unwanted keys typed
            if self.__class__.__name__ == "KeyHooker":
                if current_key not in wanted_keys and items_len >= 3:
                    items[0] = 'char=$$'
                    items[2] = 'key=$$'
                # stop enter/return key from causing new line 
                if current_key == '36': 
                    items[0] = 'char=$$'

            items = ' '.join(items)
            print "%s | %20s | %22s | %s" % ( datetime.datetime.now(), self.__class__.__name__, evtypes_rev[evt.type()], items)
        except Exception as e:
            print 'Horrific error!', e
            AppHelper.stopEventLoop()
            sys.exit(0)

class KeyHooker(Hooker): pass
class MouseButtonHooker(Hooker): pass
class MouseMoveHooker(Hooker): pass
class ScreenHooker(Hooker): pass

class SniffCocoa:

    def __init__(self):

        self.key_hook = KeyHooker()
        self.mouse_button_hook = MouseButtonHooker()
        self.mouse_move_hook = MouseMoveHooker()
        self.screen_hook = ScreenHooker()
        self.currentApp = None

    def createAppDelegate (self) :

        sc = self
        class AppDelegate(NSObject):
            def applicationDidFinishLaunching_(self, notification):
                mask = (
                          NSKeyDownMask
                        | NSKeyUpMask
                        | NSLeftMouseDownMask
                        | NSLeftMouseUpMask
                        | NSRightMouseDownMask
                        | NSRightMouseUpMask
                        | NSMouseMovedMask
                        | NSScrollWheelMask
                       )
                NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, sc.handler)
        return AppDelegate

    def run(self):
        NSApplication.sharedApplication()
        delegate = self.createAppDelegate().alloc().init()
        NSApp().setDelegate_(delegate)
        self.workspace = NSWorkspace.sharedWorkspace()
        AppHelper.runEventLoop()

    def cancel(self):
        AppHelper.stopEventLoop()

    def handler(self, event):

        try:

            activeApps = self.workspace.runningApplications()
            for app in activeApps:
                if app.isActive():
                    if app.localizedName() != self.currentApp:
                        self.currentApp = app.localizedName()
                        options = kCGWindowListOptionOnScreenOnly
                        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

                        for window in windowList:
                            if window['kCGWindowOwnerName'] == self.currentApp:
                                geom = window['kCGWindowBounds']
                                self.screen_hook( event=event,
                                                name = window['kCGWindowName'],
                                                owner = window['kCGWindowOwnerName'],
                                                x = geom['X'],
                                                y = geom['Y'],
                                                w = geom['Width'],
                                                h = geom['Height'])
                                break
                    break

            loc = NSEvent.mouseLocation()

            # mouse clicky buttons
            if event.type() in ( NSLeftMouseDown, NSRightMouseDown, NSLeftMouseUp, NSRightMouseUp):
                self.mouse_button_hook(event=event, x=loc.x, y=loc.y)

            # mouse scrolly buttons
            elif event.type() == NSScrollWheel:
                if event.deltaY() > 0 and event.deltaY() < 0:
                    self.mouse_button_hook(event=event, x=loc.x, y=loc.y)
                if event.deltaX() > 0 and event.deltaX() < 0:
                    self.mouse_button_hook(event=event, x=loc.x, y=loc.y)

            # keys down
            elif event.type() in ( NSKeyDown, NSKeyUp ):

                flags = event.modifierFlags()
                modifiers = [] # OS X api doesn't care it if is left or right
                if (flags & NSControlKeyMask):
                    modifiers.append('CONTROL')
                if (flags & NSAlternateKeyMask):
                    modifiers.append('ALTERNATE')
                if (flags & NSCommandKeyMask):
                    modifiers.append('COMMAND')
                # @author: Fabian
                # @date: April 17
                if (flags & NSAlphaShiftKeyMask): #capslock
                    modifiers.append('ALPHA-SHIFT')
                if (flags & NSShiftKeyMask):
                    modifiers.append('SHIFT')
                if (flags & NSFunctionKeyMask):
                    modifiers.append('FUNCTION')
                # if (flags & NSUpArrowFunctionKey):
                #     modifiers.append('ARROW-UP')
                # if (flags & NSDownArrowFunctionKey):
                #     modifiers.append('ARROW-DOWN')
                # if (flags & NSLeftArrowFunctionKey):
                #     modifiers.append('ARROW-LEFT')
                # if (flags & NSRightArrowFunctionKey):
                #     modifiers.append('ARROW-RIGHT')


                self.key_hook(event=event, key=event.keyCode(), char=keycode.tostring( event.keyCode() ), mods=modifiers, is_repeat=event.isARepeat())

            # Mouse moved
            elif event.type() == NSMouseMoved:
                self.mouse_move_hook(event=event, x=loc.x, y=loc.y)
            else:
                pass

        except ( KeyboardInterrupt ) as e:
            print 'handler', e
            AppHelper.stopEventLoop()


if __name__ == '__main__':
    sc = SniffCocoa()
    sc.run()
