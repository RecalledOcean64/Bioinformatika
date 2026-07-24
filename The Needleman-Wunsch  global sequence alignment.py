def traceback(x,y,n,m,sm,bm,ak):
    i=m
    j=n
    out1=""
    out2=""
    while i>0 and j>0:
        if sm[j][i]==bm[ak.index(y[j-1])][ak]:
            out1+=x[i-1]
            out2+=y[j-1]
            i+=-1
            j+=-1
        elif sm[j][i] == sm[j-1][i]-8:
            out2 += y[j-1]
            out1 += "_"
            j += -1
        else:
            out1 += x[i-1]
            out2 += "_"
            i += -1
    if i==j:
        out1 += x[0]
        out2 += y[0]
    elif j==0:
        for t in range(i-1, -1, -1):
            out1 += x[t]
            out2 += "_"
    else:
        for t in range (j-1, -1, -1):
            out2 += y[t]
            out1 += "_"
    return out1[::-1], out2[::-1]

f1=open("acids.txt", "r")
ak=f1.readline()
f1.close()

bm=[]
f1=open("blosum50.txt", "r")
for i in range(20):
    line=f1.readline()
    vc=line.split()
    bm.append(vc[:])
for i in range(20):
    for j in range(20):
        bm[i][j]=int(bm[i][j])
f1.close()

x='HPEW'
y='PW'
m=len(x)
n=len(y)

sm=[] 
tmp=[]
for i in range(m+1):
    tmp.append(0)
for i in range(n+1):
    sm.append(tmp[:])


for i in range(n+1):
    sm[i][0]=-8*i
for i in range(m+1):
    sm[0][i]=-8*i

for i in range(1,n+1):
    for j in range(1,m+1):
        tmp=[]
        tmp.append(sm[i-1][j]-8)
        tmp.append(sm[i][j-1]-8)
        bb=bm[ak.index(y[i-1])][ak.index(x[j-1])]
        tmp.append(sm[i-1][j-1]+bb)
        tmp.sort()
        sm[i][j]=tmp[2]

