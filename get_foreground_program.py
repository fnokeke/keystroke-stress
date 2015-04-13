######################################################
# __author__ = Fabian Okeke
# __date__ = March 11, 2015

# obtain the foreground application running in MAC OS
######################################################


# print the foreground application running in MAC OS
def print_fg_app(how_many):
    from AppKit import NSWorkspace

    count = 0
    while count < how_many:
        activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        print activeAppName
        count += 1


######################################################
#                   MAIN
######################################################
if __name__ == "__main__":
    how_many = 10000
    print_fg_app(how_many)
