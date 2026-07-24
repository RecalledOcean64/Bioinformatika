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



rj = ""



def traceback(s, i, j):



    if(i==0 and j==0):

        global rj 

        rj = rj + s + '\n'

        return



    if((i-1) > -1 and (sm[i-1][j]-8) == sm[i][j] ):

        s = 'G' + s

        traceback(s,i-1,j)

        

    if((j-1) > -1 and (sm[i][j-1]-8) == sm[i][j] ):

        s = 'L' + s

        traceback(s,i,j-1)

        

    bb=bm[ak.index(y[i-1])][ak.index(x[j-1])]	

    if((i-1) > -1 and (j-1) > -1 and(sm[i-1][j-1] + bb) == sm[i][j] ):

        s = 'D' + s

        traceback(s,i-1,j-1)

traceback('', n, m)

print(rj)