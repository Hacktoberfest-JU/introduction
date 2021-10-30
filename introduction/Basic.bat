@echo off

:options
cls
    echo Press 1 to Change date
    echo Press 2 to Change time
    echo Press 3 to shutdown
    echo Press 4 to Abort shutdown
    echo Press 5 to logout
    echo Press 6 to exit 
    
PAUSE



 SET /P choice="Enter Choice:"
  
 net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Administrative permissions confirmed .
    )

    @REM  else (
    @REM     msg %USERNAME% Admininstrator Privilige Required
    @REM     echo Failure: Current permissions inadequate PLEASE OPEN IT WITH ADMIN LEVEL privilege.
    @REM     PAUSE
        
    @REM )

    if %choice% == 1 (
        @REM Validating Admin Preivilige
        if %errorLevel% == 0 (
            date
            goto options
        ) else (
            msg %username% Admininstrator Privilige Required
            goto options
        )
    ) 
    
    if  %choice% == 2 (
        @REM Validating Admin Preivilige
        if %errorLevel% == 0 (
            time
            goto options
        )
        else (
            msg %username% Admininstrator Privilige Required
            goto options
        )
    ) 
    
    if %choice% == 3 (
           
        shutdown /s /t 20
        pause
        goto options
    ) 
    
    if %choice% == 4 (
        shutdown /a
        goto options
    ) 
    
    if %choice% == 5 (
        shutdown /l
    )

    if %choice% == 6 (
        exit
    )
