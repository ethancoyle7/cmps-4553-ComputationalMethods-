n=12
block=[]
for i in range(n):
    block.append([])
    block[i].append(1)
    for j in range(1,i):
        block[i].append(block[i-1][j-1]+block[i-1][j])
    if(n!=0):
        block[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(block[i][j]),end=" ",sep=" ")
    print()
