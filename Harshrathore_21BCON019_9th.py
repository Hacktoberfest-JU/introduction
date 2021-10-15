#Taking input of tuple 1

values_1 = input("Input some comma seprated numbers : ")
list_1 = values_1.split(",")
tuple_1 = tuple(list_1)
print('Tuple 1 : ',tuple_1)

#Taking input of tuple 2

values_2 = input("Input some comma seprated numbers : ")
list_2 = values_2.split(",")
tuple_2 = tuple(list_2)
print('Tuple 2 : ',tuple_2)

#tuple 1 + tuple 2
tuple_3 = tuple_1 + tuple_2
print('Tuple 3 = ',tuple_3)
