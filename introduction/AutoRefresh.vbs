'Tired with manually refreshing .This program will help you to refresh your device automatically Hassle free'


Option Explicit
dim ref

' Alert Message only. Can be removed '
msgbox "Don't open Anything Refreshing your PC",vbCritical,"Self programmed"   


' Alert Message only. Can be removed .ADVICE Dont Remove'
wscript.sleep 2000
set ref = CreateObject("wscript.shell")

dim a

a=1
Do until a=16
ref.sendkeys"{F5}"
a=a+1

'sleep time between each refresh attempt'
wscript.sleep 100

loop


msgbox "Refreshed 15 times",vbInformation,"Self Programmed"
