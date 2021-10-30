n1, m1 = map(int, input().split())
mat1 = []
for i in range(n1):
    l = []
    l = [int(input("enter the elements : ")) for i in range(m1)]
    mat1.append(l)
#---------------------------------------------------------------#
n2, m2 = map(int, input().split())
mat2 = []
for i in range(n2):
    l = []
    l = [int(input("enter the elements : ")) for i in range(m2)]
    mat2.append(l)
#---------------------------------------------------------------#
mat3 = []
if m1 == n2:
    for i in range(n1):
        l = []
        for j in range(m2):
            x = 0
            for k in range(n2):
                x = x+mat1[i][k]*mat2[k][j]
            l.append(x)
        mat3.append(l)

    for i in range(n1):
        for j in range(m2):
            print(mat3[i][j], end=" ")
        print(end="\n")

else:
    print("NOT POSSIBLE !!!")
