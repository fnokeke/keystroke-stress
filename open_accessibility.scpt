display dialog "Please click the lock icon on the next popup dialog and add these apps to accessibility:
********************************************************
                1) startup_keystroke.app, 
                2) startup_foreground.app, 
                3) pam_and_self_report.app
********************************************************
Thank you!"

tell application "System Preferences"
    --get a reference to the Security & Privacy preferences pane
    set securityPane to pane id "com.apple.preference.security"

    --tell that pane to navigate to its "Accessibility" section under its Privacy tab
    --(the anchor name is arbitrary and does not imply a meaningful hierarchy.)
    tell securityPane to reveal anchor "Privacy_Accessibility"

    --open the preferences window and make it frontmost
    activate
end tell
