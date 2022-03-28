prices=list(map(int,input().split(" ")))
maxx=0
i=0
j=1
while j<len(prices):
    if prices[i]<prices[j]:
        profit=prices[j]-prices[i]
        maxx=max(maxx,profit)
    else:
        i=j
    j+=1
print(maxx)
