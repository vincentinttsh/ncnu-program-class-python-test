def Main():
    n = int(input())
    squre = [[x+1+y*n for x in range(n)]for y in range(n)]
    for i in range(n):
        for j in range(n):
            print(squre[i][j],end='\t')
        print()
    print()
    for i in range(n-1 , -1 , -1):
        for j in range(n):
            print(squre[i][j],end='\t')
        print()
    print()
    for i in range(n):
        for j in range(n-1 , -1 , -1):
            print(squre[i][j],end='\t')
        print()
    print()
    for i in range(n):
        for j in range(n-1 , -1 , -1):
            print(squre[j][i],end='\t')
        print()
    print()
    for i in range(n-1 , -1 , -1):
        for j in range(n-1 , -1 , -1):
            print(squre[i][j],end='\t')
        print()
    print()
    for i in range(n-1 , -1 , -1):
        for j in range(n):
            print(squre[j][i],end='\t')
        print()
    print()
Main()