import appscript

while True:
    print appscript.app("Safari").windows.first.current_tab.URL()
