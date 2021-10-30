@echo off

@REM checking for privilege  Adminstrator usage . Only this part is taken from stackoverflow.
 net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Administrative permissions confirmed .
    ) else (
        echo Failure: Current permissions inadequate PLEASE OPEN IT WITH ADMIN LEVEL privilege.
        PAUSE
        exit
    )

echo PLEASE ENTER 8digit PASSWORD MUST
SET /P hotspotKey=" Set hotspot password:"
SET /P hotspotName="Set hotspot name:"

netsh wlan set hostednetwork mode=allow ssid=%hotspotName% key=%hotspotKey%
echo Initiating Hotspot

@REM Initiating Hotspot
netsh wlan start hostednetwork

cls  
echo Please press FORGET NETWORK if you use the SAME NAME and DIFFERENT PASSWORD
echo Hotspot Name:%hotspotName%
echo Hotspot Key:%hotspotKey%

@REM General variable defined to stop auto termination of command line could also use PAUSE
SET /P WantToStopHotspot="Press ENTER to STOP hotspot: "

netsh wlan stop hostednetwork
