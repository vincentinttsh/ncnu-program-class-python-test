from datetime import datetime , timedelta
def time_set (x) :
    return datetime.strptime(x,'%m/%d,%H:%M')
def time_ok(x , y , flight) :
    if time_set(flight[x][3]) >= time_set(flight[y][4]) + timedelta(minutes=int(flight[x][5])) :
        return True
    return False
def time_all(x , flight):
    spend = (time_set(flight[x[0]][4]) - time_set(flight[x[0]][3])).seconds//60
    for i in range(1 , len(x)) :
        spend +=  (time_set(flight[x[i]][4]) - time_set(flight[x[i]][3])).seconds//60 + int(flight[x[i]][5])
    return str(spend)
def findPath(flight , end_place , had_go , take_flight) :
    now = take_flight[-1] 
    if flight[now][2] == end_place :
        print('è½æ© '+str(len(take_flight) - 1)+' æ¬¡, ç¸½è¡ç¨æéçº: '+time_all(take_flight , flight)+' åé')
        print(flight[take_flight[0]][0],end='')
        for i in range(1,len(take_flight)) :
            print(' -> '+flight[take_flight[i]][0],end='')
        print()
        return
    for i in range(len(flight)) :
        if flight[i][1] == flight[now][2] and time_ok(i , now , flight) and flight[i][2] not in had_go :
            had_go[flight[i][2]] = True
            take_flight.append(i)
            findPath(flight , end_place , had_go , take_flight)
            del had_go[flight[i][2]]
            take_flight.pop()
    return
def Main():
    flight = list()
    n , start , end_place = input().split()
    had_go = {start : True}
    for i in range(int(n)) :
        flight.append(input().split())
    for i in range(int(n)) :
        if flight[i][1] == start :
            had_go[flight[i][2]] = True
            findPath(flight , end_place , had_go , [i])
            del had_go[flight[i][2]]
Main()