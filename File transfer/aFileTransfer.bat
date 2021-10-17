@echo off

@REM checking for privilege  Adminstrator usage .
 net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Administrative permissions confirmed .
        cls
    
    ) else (
        msg %USERNAME% Admininstrator Privilige Required
        echo Failure: Current permissions inadequate PLEASE OPEN IT WITH ADMIN LEVEL privilege.
        PAUSE
        
        exit
    )

@REM checking for python 
python --version  >nul 2>&1

    if %errorLevel% == 0 (
        echo python is present
        cls
    ) else (
        msg %USERNAME% python not found in system
        echo python is Required
        PAUSE
        
    )


echo PLEASE ENTER PASSWORD (8digit MUST)
SET /P hotspotKey=" Set hotspot password:"
SET /P hotspotName="Set hotspot name:"

netsh wlan set hostednetwork mode=allow ssid=%hotspotName% key=%hotspotKey%
echo Initiating Hotspot
Msg %USERNAME% Initiated Hotspot

@REM Initiating Hotspot
netsh wlan start hostednetwork
cls



cls


@REM if loop breaking the code don't know the reason using same command to change drive  and in same drive location stucked here for more than 1 day 

@REM if %choice% == 1  (
@REM     goto SameDirectory
@REM ) else (
      goto changingDirectory
@REM )

@REM Stuck in changing directory for more than 1 day to change drive use cd /D "then enter path"


:rest

 set /P portNumber="Enter the port number for webserver (like 8000):"



@REM used for getting the ip Address
ipconfig | findstr /c:"IPv4 Address. . . . . . . . . . ."

set /p ipaddr="Enter the wirless lan ip address(Type the above ip shown of form 192.XXX.XXX.XXX):"

cls  
echo Please press FORGET NETWORK if you use the SAME NAME and DIFFERENT PASSWORD
echo.  
echo Hotspot Name:%hotspotName%
echo Hotspot Key:%hotspotKey%
echo.
echo Folder Sharing Path: %anyDirectory%
echo.
echo.
echo Connect the devices to PC hotspot and enter the web Address as mentioned below 192.XXX.XX.XX:XXXX


@REM local webser deployed 
msg %USERNAME% Press Ctrl+C to stop
python -m http.server %portNumber% --bind %ipaddr%



@REM General variable defined to stop auto termination of command line could also use PAUSE
SET /P WantToStopHotspot="Press ENTER to STOP hotspot: "

netsh wlan stop hostednetwork
Msg %USERNAME% Hotspot Stopped

:SameDirectory
set /p anyDirectory="Enter the  folder location:"
cd /D "%anyDirectory%"
goto rest


:changingDirectory
set /p anyDirectory="Enter the folder location to be shared:"
cd /D "%anyDirectory%"
goto rest