# String slicing
String = 'HARSH RATHORE'
s1 = slice(-6)
s2 = slice(-1, -6, -2)
print("String slicing")
print("Slicing without step value : ", String[s1])
print("Slicing with step value : ", String[s2])
 
# List slicing
L = ['H','A','R','S','H','','R','A','T','H','O','R','E']
s1 = slice(-6)
s2 = slice(-1, -6, -2)
print("\nList slicing")
print("Slicing without step value : ", L[s1])
print("Slicing with step value : ",L[s2])
 
# Tuple slicing
T = ('H','A','R','S','H','','R','A','T','H','O','R','E')
s1 = slice(-6)
s2 = slice(-1, -6, -2)
print("\nTuple slicing")
print("Slicing without step value : ",T[s1])
print("Slicing with step value : ",T[s2])
