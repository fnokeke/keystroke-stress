######################################################
# __author__ = Fabian Okeke
# __date__ = March 11, 2015

# obtain the foreground application running in MAC OS
######################################################


# print the foreground application running in MAC OS
def print_fg_app(how_many):
    from AppKit import NSWorkspace
    import time

    count = 0
    while True:
        activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        import datetime
        print "%s | %20s" % (datetime.datetime.now(), activeAppName)
        time.sleep(10) #every seconds
        # if count % 10 == 0: 
        # count += 1


######################################################
#                   MAIN
######################################################
if __name__ == "__main__":
    how_many = 10000
    print_fg_app(how_many)
