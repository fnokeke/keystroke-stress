# keystroke-stress
The primary goal of this project is to predict stress based on computer usage. The following timestamped input are collected:
- keystrokes 
- mouse actions
- foreground applications
- photographic affect meter (PAM) self-report 
- user self-report 


### How to use 
This assumes that you already have [python installed].

##### navigate to location where you want to store project
`cd /path/you/want/to/download/project/`

##### download keystroke-stress/ directory
`git clone https://github.com/fnokeke/keystroke-stress.git` 

##### run startup script to install necessary libraries
`./set_up.sh` #this is located in your /keystroke-stress/ directory downloaded above

##### For Yosemite
`Go to System Preferences >> Security & Privacy >> Privacy (tab) >> Accessibility (bottom-left)`

`Add terminal or iterm2` if you plan on printing output on the terminal during development

`Add startup_keystroke.app` using to the list of apps. 

`Double-click startup_keystroke.app` to launch the app (it should appear in dock as one of your applications running)


##### For Mavericks
`Go to System Preferences >> Security & Privacy >> Privacy (tab) >> Accessibility (bottom-left)`
`Open Finder and navigate to the app`
`Drag and drop the app into Accessibility`


### Why all this trouble?
**Note:** Not doing this means your application will not capture keystrokes and mouse clicks. This restriction is by Apple so that users can control permissions.
### Privacy managed
In order to manage privacy, every data collected is stored on the user's computer; no data is sent to any server. This means that a user can decide to remove the parts of the data they are not comfortable with if this is used for a research experiment.

### Dataset
All dataset is stored in the data directory.

[***You need to open each of the applications using AppleScriptEditor and then change the dataset directory to your own choice -- currently hardcoded.***]

### Keystroke actions
Shows the keys you're currently typing irrespective of the application involved -- if using terminal, Safari, Notes, etc, it still logs these keys with the times they were entered.

### Mouse actions
Shows x-y coordinates of your mouse movement as well as clicking events. This is timestamped and stored in a log file in the dataset directory.

### Show current foreground application
shows the current application in focus. So if using safari then it's 'Safari'; if notes then it shows 'Notes', etc.

### Self-Report and PAM applications
Collect the user's PAM and stress status report during hardcoded intervals of the day. 
- PAM involves selecting a picture to express your current mood (image below).
- Self-Report survey asks 3 questions with 5 choices each. Select one from each category (image below). 

### Operating System
Current focus is on OS X (other operating systems coming soon...)

### OS X Applications
    > **Note:**
    > - The directories with extension '.app' are applications on OS X. Just like 'adobe.app', 'Safari.app', this will be 'label'.app where label is the name of the directory. You start them by double-clicking just like you would a regular application.
    > - The applications will show on the dock when run in OS X. To have them not show, go to <app_name>/Contents/Info.plist where <app_name> is the name of one of the listed applications you're interested. 

    Then following the XML format of the file, add:

    `<key>LSUIElement</key>`

    `<true/>`

### Data Analysis
For data analysis, you can go to the folder 'analysis', there are scripts and associated readme files regarding how to run the data analysis.

### TO-DO
    - update time-format so that files follow a chronological order
    - change hardcoded dataset directory in applescript
    - change hardcoded overall 
    - simple demo-analysis on local server
    - add dataset directory
    - add image of PAM
    - add image of EMA
    - how to install pyobjc
    - automatically install pykeycode for the user
    - reference pykeycode
    - explain that is_repeat=True when a key pressed and held down.
    - automatically create ninja_data directory



    [pam-logo]: link
    [python installed]: link
    [pykeycode]: link
