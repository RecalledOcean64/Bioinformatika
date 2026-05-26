import random
import math

def sed(x, y): # udaljenost točaka (kvadrat euklidske metrike)
    dist = 0
    for i in range(len(x)):
        dist = dist + (x[i] - y[i]) * (x[i] - y[i])
    return dist

def sad(x, y): # zbrajanje vektora
    v = []
    for i in range(len(x)):
        v.append(x[i] + y[i])
    return v

def init(data, k):  # inicijalizacija (obično)
    c = random.sample(data, k)
    return c

def init_pp(data, k):  # inicijalizacija (k-means++)
    c = [random.choice(data)]
    n = len(data)
    for t in range(1, k):
        dist = []
        for i in range(n):
            cl_dist = sed(data[i], c[0])
            for j in range(t):
                temp_dist = sed(data[i], c[j])
                if temp_dist < cl_dist:
                    cl_dist = temp_dist
            dist.append(cl_dist)
            
        ind = []
        sum_d = sum(dist)
        for i in range(n):
            dist[i] = dist[i] / sum_d
            ind.append(i)
        a = random.choices(ind, weights=dist, k=1)
        c.append(data[a[0]])
    return c

def assign(data, cent):
    c_id = []
    for i in range(len(data)):
        min_dist = sed(data[i], cent[0])
        cl_index = 0
        for j in range(1, len(cent)):
            temp_dist = sed(data[i], cent[j])
            if temp_dist < min_dist:
                min_dist = temp_dist
                cl_index = j
        c_id.append(cl_index)
    return c_id

def update(data, cent, c_id):
    n = len(data)
    dim = len(data[0])
    k = len(cent)

    # Stvaramo potpuno novu matricu u memoriji kako ne bismo prepisivali originale
    novi_centari = [[0.0] * dim for _ in range(k)]
    
    for i in range(k):
        v = [0.0] * dim
        cl_count = 0
        for j in range(n):
            if c_id[j] == i:
                cl_count = cl_count + 1
                v = sad(v, data[j]) # Koristi se isključivo lokalni parametar 'data'
        
        if cl_count > 0:
            for j in range(dim):
                novi_centari[i][j] = v[j] / cl_count
        else:
            novi_centari[i] = list(cent[i])
            
    return novi_centari


#########################################

# Učitavanje podataka (promijeni "data01.txt" u ime svoje datoteke ako je potrebno)
f1 = open("data01.txt", "r")

k = int(f1.readline())      # broj centara = broj grupa
n = int(f1.readline())      # broj tocaka
dim = int(f1.readline())    # dimenzija tocaka

x = []  # matrica točaka
for i in range(n):
    line = f1.readline() 
    vector = line.split() 
    x.append(vector[:]) 
for i in range(n):
    for j in range(dim):
        x[i][j] = float(x[i][j])
f1.close()

# Inicijalizacija centara pomoću k-means++ algoritma
C = init_pp(x, k)   

it = 25     # broj iteracija optimizacije

# Glavna petlja u kojoj algoritam odrađuje konvergenciju (bez suvišnih ispisa)
for t in range(it):
    c_id = assign(x, C)
    C = update(x, C, c_id)

# Zadnji, fiksni assignment nakon što su se centri prestali micati
c_id = assign(x, C)

# =====================================================================
# ČISTI I TOČAN ISPIS REZULTATA
# =====================================================================

print("KOORDINATE CENTARA:")
print("-" * 30)
for i in range(k):
    # Zaokruživanje koordinata centara na 4 decimale radi preglednosti
    zaokruzeni_centar = [round(koord, 4) for koord in C[i]]
    print(f"Centar {i + 1}: {zaokruzeni_centar}")

print("\nPRIPADNOST TOČAKA KLASTERIMA:")
print("-" * 30)
for i in range(k):
    print(f"{i + 1}. centru pripada cluster:")
    # Izbacuje isključivo originalne točke iz matrice x
    for j in range(n):
        if c_id[j] == i:
            print(f"  Točka {j}: {x[j]}")
    print()