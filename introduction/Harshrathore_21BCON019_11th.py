string = input("Enter a String : ")
length = len(string)
a = 0
end = length
string_2 = ''
while a<length:
    if a==0:
        string_2 += string[0].upper()
        a += 1
    elif (string[a] == '' and string[a+1]!=''):
        string_2 += string[a]
        string_2 += string[a+1].upper()
        a += 2
    else:
        string_2 += string[a]
        a += 1
print("Original String : ",string)
print("Capitalized word String : ",string_2)
