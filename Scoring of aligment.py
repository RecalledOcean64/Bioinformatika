
f=open("acids.txt", "r")

ak=f.readline()

f.close()

m=[]

f=open("blosum50.txt", "r")



for i in range(20):

    line=f.readline()

    lista=line.split()

    for j in range(20):

        lista[j]=int(lista[j])

    m.append(lista)



f.close()

f=open("por001.txt", "r")

x=f.readline()

y=f.readline()

f.close()

score=0



for i in range(len(x)-1):

    if x[i]=='_' or y[i]=='_':

        score+=-8

    else:

        r=ak.index(x[i])

        s=ak.index(y[i])

        score+=m[r][s]

print(score)
