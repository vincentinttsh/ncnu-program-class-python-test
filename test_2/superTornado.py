def start_turn (array , n , d) :
    array_2 = [[array[n//2][n//2] for x in range(n)]for y in range(n)]
    for i in range (d , n//2 , 2) :                 #turn left
        for j in range (i , n-1-i) :
            array_2[i][j] = array[i][j+1]           #up
            array_2[n-i-1][j+1] = array[n-i-1][j]   #down
            array_2[j+1][i] = array[j][i]           #left
            array_2[j][n-i-1] = array[j+1][n-i-1]   #right
    for i in range (not d , n//2 , 2) :             #turn right
        for j in range (i , n-1-i) :
            array_2[i][j+1] = array[i][j]           #up
            array_2[n-i-1][j] = array[n-i-1][j+1]   #down
            array_2[j][i] = array[j+1][i]           #left
            array_2[j+1][n-i-1] = array[j][n-i-1]   #right
    return array_2
def print_all (array) :
    for x in range(len(array)) :
        for y in range(len(array[x])) :
            print(array[x][y],end='\t')
        print()
def Main():
    n = int(input())
    print_all(start_turn([[x+1+y*n for x in range(n)]for y in range(n)] , n , input()>='r'))
Main()