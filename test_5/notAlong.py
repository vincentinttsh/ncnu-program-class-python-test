def printGroup(item) :
    for x in range(len(item)):
        if len(item[x]) !=0:
            print(item[x])
def findGroup(item):
    n = len(item)
    x = 0
    for x in range(n):
        if len(item[x]) == 1:
            if x != 0 :
                a = 0
                b = len(item[a])
            else :
                a = 1
                b = len(item[a])
            for y in range(len(item)):
                if len(item[y]) < b and len(item[y])!=0  and y != x:
                    b = len(item[y])
                    a = y
            item[x].update(item[a])
            item[a].clear()
    return item
def main() :
    n = int(input())
    group = list()
    where_group=[-1 for x in range(n)]
    alone = False
    for x in range(n):
        te = int(input())
        if where_group[x] == -1 and where_group[te] == -1 :
            group.append(set([te , x]))
            where_group[x] , where_group[te] = len(group)-1 , len(group)-1
        elif where_group[x] != -1 :
            group[where_group[x]].add(te)
            where_group[te] = where_group[x]
        else :
            group[where_group[te]].add(x)
            where_group[x] = where_group[te]
    printGroup(group)
    for x in range(len(group)):
        if len(group[x]) == 1 :
            alone = True
            break
    if alone :
        print()
        printGroup(findGroup(group))
main()   