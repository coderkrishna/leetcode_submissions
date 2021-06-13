inputlist = list(map(int,input().split()))
target = int(input())
result = []

for i in range(len(inputlist)):
    for j in range(i+1,len(inputlist)):
        if(inputlist[i] + inputlist[j] == target): 
            result.append({i,j})
            
print(result)            