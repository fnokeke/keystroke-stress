# keystroke-stress

### Keyboard actions
Shows the keys you're currently typing irrespective of the application involved -- if using terminal, Safari, Notes, etc, it still logs these keys.

### Mouse actions
Shows x-y coordinates of your mouse movement as well as clicking events.

### Show current foreground application
shows the current application in focus. So if using safari then it's 'Safari'; if notes then it shows 'Notes', etc.

### EMA and PAM applications
collect the user's PAM and stress status report during hardcoded intervals of the day. 

### Operating System
Current focus is on MAC (others coming soon)

#### <i class="icon-hdd"></i> Dataset 
You need to open each of the applications using AppleScriptEditor and then change the dataset directory to your own choice (currently hardcoded).

#### <i class="icon-trash"></i> Deleting data
Just delete your 'datasets' directory -- all data is currently stored locally. Goal is to maintain this approach.

> **Note:**
> - The directories with extension '.app' are applications on MAC. Just like 'adobe.app', 'Safari.app', this will be 'label'.app where label is the name of the directory. You start them by double-clicking just like you would a regular application.
> - The applications will show on the dock when run in MAC. To have them not show, go to <app_name>/Contents/Info.plist where <app_name> is the name of one of the listed applications you're interested. Then following the XML format of the file, add:
```<key>LSIU Element></key> 
   <true/>
``` 
