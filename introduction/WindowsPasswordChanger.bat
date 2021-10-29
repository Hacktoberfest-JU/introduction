@echo off

SET /A safety=0
net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Administrative permissions confirmed .
        echo Jokes Apart.This will seriously change your password
        echo list of User on this PC
        @REM Remeber need to declare variable again took almost 3hours to figure out.
        SET /A "safety=1"

    ) else (
        echo Failure: Current permissions inadequate PLEASE OPEN IT WITH ADMIN LEVEL privilege.
        echo Still Continuing You WIll DEFINITELY FACE ERROR 
        SET /A safety=0
    )
PAUSE
cls

echo Displaying all User
@REM Scope of improvement need to filter out only username
net user

SET /P UserName="Enter UserName:"

if %safety% == 1 (
    msg %USERNAME% ALERT!! YOU ARE TRYING TO CHANGE PASSWORD
)


net user %UserName% *

PAUSE

@REM later part of the code set's the password to random . So its commented you can remove the comment but be ON YOUR TOES 
@REM net user %UserName% /random
