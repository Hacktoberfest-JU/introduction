Option Explicit
Dim WindowsFirewall,main,Kane

MsgBox "Injected Trojan!!",16,"System32"
WindowsFirewall=MsgBox ("Trojan detected, trying to REMOVE",48+vbSystemModal,"Widows Firewall")

if WindowsFirewall=VBOK then
 MsgBox "Failed!",48,"Windows Firewall"
 MsgBox "DEACTIVATED",48,"Windows Firewall"

End if
MsgBox "Trying to Restore Dont do anything",16,"System32"

set Kane = createobject("SAPI.SpVoice")

Kane.rate= 1
kane.volume=100
Kane.speak "Hello Victim, Surprise . I have stolen your credentials and something personal wanna say something,  sorry I cant hear buddy I forgot to take control of your mic.  "



Kane.speak "You have been Hacked. I  Copied sam files,cookies,credentials Thanks User Destroyed your firewall and Anti-virus"
