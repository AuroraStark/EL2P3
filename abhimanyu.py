#chakravyihu
nm = int(input())
c = []
for x in range(nm):
    x = []
    for y in range(nm):
        x.append(0)
    c.append(x)
p = []
p.append((0,0))
start,end,n = 0,nm-1,1
for i in range((nm+1)//2):
    for j in range(start,end+1):
        c[start][j] = n
        if n%11==0:
            p.append((start,j))
        n +=1
    for j in range(start+1,end+1):
        c[j][end] = n
        if n%11==0:
            p.append((j,end))
        n +=1
    for j in range(end-1,start-1,-1):
        c[end][j] = n
        if n%11==0:
            p.append((end,j))
        n +=1
    for j in range(end-1,start,-1):
        c[j][start] = n
        if n%11==0:
            p.append((j,start))
        n +=1
    start +=1
    end -= 1
for i in range(nm):
    for j in range(nm):
        print(c[i][j],end='\t')
    print()
print('Total Power points :',len(p))
print(*p,sep='\t')