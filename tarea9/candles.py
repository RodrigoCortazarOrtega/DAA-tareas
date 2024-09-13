def candles(a: list[int]) -> int:
    m=0 
    rep_m=0
    for i in range(len(a)):
        if a[i]>m:
            #print("Nuevo max")
            m=a[i]
            rep_m=1
        elif a[i]==m:
            rep_m+=1
        #print("m: {} rep_m:{}".format(m,rep_m))
        #print("-----------------------------")
    return rep_m


first=[2,6,4,1,3,2,2,1,4,2,4,7,6,1]
second=[2,6,4,1,3,2,2,1,4,2,6,1]
third=[2,4,1,3,2,4,2,1,4,2,1]
print(candles(third))



