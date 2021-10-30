def vowelappears():
    str1 = input("Enter line : ")
    cnt = 0
    for letter in str1:
        if letter in ('a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"):
            cnt += 1
    print("Number of vowels = ", cnt)


vowelappears()
