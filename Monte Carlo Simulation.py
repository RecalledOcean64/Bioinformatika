from random import choices
def maximum(sim):
    max=0
    k=0
    for i in range(200):
        if(sim[i]==1):
            k+=1
        elif(k>max):
            max=k
            k=0
        elif(k<=max):
            k=0
    return max          

f=open("rezultati.txt","w")
for i in range(1000):
    sim=choices([0,1],k=200)
    m=maximum(sim)
    f.write(str(m)+"\n")
f.close()
