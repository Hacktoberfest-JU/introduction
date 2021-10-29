'''Write a Python function equallasttext(str1,str2,n) which takes three
arguments, the first two being strings str1 , str2 and the last one being a
positive integer . The program should return True if the last
characters of the
str1 and str2 are equal and returns False otherwise.'''
def equallasttext(str1,str2,n):
if str1[-n:] == str2[-n:]:
return True
else:
return False
equallasttext('Shreya','eya',3)
