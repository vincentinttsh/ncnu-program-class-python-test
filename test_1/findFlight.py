from datetime import datetime
from datetime import timedelta
# plance = èªç­åç¨± now = ç¾å¨ä½ç½® arrive = çµé» hado = å·²æ­ç­æ© times = ç¾å¨æé takeflight = å·²å»å°æ¹ n = è¡ç­æ¸ alltime = å¨é¨æé qq = è½æ©æ¸
def findPath (plance , now , arrive , hado , times , takeflight , n ,alltime , qq):
    if now == arrive :
    	# print infromation
        print('è½æ© '+str(qq)+' æ¬¡, ç¸½è¡ç¨æéçº: '+str(alltime)+'åé')
        print(plance[hado[0]][0],end='')
        #print flight
        for i in range(1 , len(hado)) :
            print(' -> '+plance[hado[i]][0],end='')
        print()
        return
    for i in range(n) :
    	# plance can take , time ok , no get there before 
        if plance[i][1] == now and datetime.strptime(plance[i][3],'%m/%d,%H:%M') >= times+timedelta(minutes=int(plance[i][5])) and  plance[i][2] not in takeflight :
            takeflight[plance[i][2]] = True # got there
            hado.append(i) # take the plance no 
            temp = datetime.strptime(plance[i][4],'%m/%d,%H:%M') + timedelta(minutes=int(plance[hado[len(hado)-1]][5]))
            spend = temp -  datetime.strptime(plance[i][3],'%m/%d,%H:%M')
            findPath(plance , plance[i][2] , arrive , hado , datetime.strptime(plance[i][4],'%m/%d,%H:%M') , takeflight , n,alltime + spend.seconds//60,qq+1)
            del takeflight[plance[i][2]]
            del hado[len(hado)-1]
    return
def main () :
    plance = list()
    hado = list()
    takeflight = dict()
    n , start , right = input().split()
    n = int(n)
    for i in range(n) :
        plance.append(input().split())
    for i in range(n):
        if plance[i][1] == start :
            takeflight[plance[i][1]] = True
            takeflight[plance[i][2]] = True
            hado.append(i)
            temp = datetime.strptime(plance[i][4],'%m/%d,%H:%M')
            spend = temp - datetime.strptime(plance[i][3],'%m/%d,%H:%M')
            findPath(plance , plance[i][2] , right , hado , temp , takeflight , n,spend.seconds//60,0)
            del takeflight[plance[i][2]]
            del hado[len(hado)-1]
main()
