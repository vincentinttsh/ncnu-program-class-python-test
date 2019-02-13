class Merchandise :
    def __init__(self):
        self.__product_and_price = list()
    def Add (self ,thing , price) :
        self.__product_and_price.append([thing , price])
    def PrintItem(self):
        for q in range(len(self.__product_and_price)):
            print('商品 ' + str(q+1) + ' ： ' + self.__product_and_price[q][0] + 
            ' ，' + self.__product_and_price[q][1] + ' 元' )
    def __ReturnChange(self , money , cost , cash = [1000 , 500 , 100 , 50 , 10 , 5 , 1]) :
        cash.sort(reverse = True)
        money -= cost
        for x in cash :
            if money//x > 0 :
                print(str(money//x) + ' 張 ' + str(x) , end='  ')
                money %= x
        print()
    def Buy_product(self):
        print('請輸入購買清單：')
        cost = 0
        buy=input().split()
        while buy[0] !='end' :
            cost +=int(self.__product_and_price[int(buy[0])-1][1]) * int(buy[1])
            buy=input().split()
        print('總共 ' + str(cost) + ' 元' )
        money = int(input('請輸入繳交金額：'))
        while money < cost :
            money = int(input('支付金額不足, 請重新輸入：'))
        self.__ReturnChange(money , cost)
def main():
    n=int(input())
    merchandise = Merchandise()
    for q in range(n):
        x,y = input().split()
        merchandise.Add(x,y)
    merchandise.PrintItem()
    merchandise.Buy_product()
main()