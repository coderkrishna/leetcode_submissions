inputlist = list(map(int,input().split()))
target = int(input())
result = []

for i in range(len(inputlist)):
    for j in range(i,len(inputlist)):
        if(inputlist[i] + inputlist[j] == target): 
            print(list({i,j}))
            