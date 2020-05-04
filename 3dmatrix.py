n=int(input("Enter the number of matrices: "))
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))

#arr[n][r][c]
for i in range(n):
    for j in range(r):
        for k in range(c):
            arr[i][j][k]=int(input())
for i in range(n):
    for j in range(r):
        for k in range(c):
            print(arr[i][j][k])