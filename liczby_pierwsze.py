#Liczby pierwsze, dwa algorytmy, wykresy czasu wykonania
import time
print('Program do znajdowania liczb pierwszych')
max_l = int(input('Podaj, do jakiej wartości szukać liczb pierwszych (>2): '))
#Algorytm 1
def pierwsze1(max_l):
    pierwsza=False
    licznik=0
    start=time.time()
    for i in range(3,max_l+1):
        for j in range(2,i):
            pierwsza = True
            if i%j == 0:
                pierwsza = False
                break
        if pierwsza:
            #print(i)
            licznik+=1
    koniec=time.time()
    czas=koniec-start
    print(10*'-'+'\nZnalezionych liczb pierwszych:',licznik)
    print('Czas wykonania programu: {:.3f}'.format(czas))
    return czas
    
#algorytm 2
def pierwsze2(max_l):
    pierwsza=False
    licznik=0
    lista=[2]
    start=time.time()
    for i in range(3,max_l+1):
        for j in lista:
            pierwsza = True
            if i%j == 0:
                pierwsza = False
                break
        if pierwsza:
            #print(i)
            lista.append(i)
            licznik+=1
    koniec=time.time()
    czas=koniec-start
    print(10*'-'+'\nZnalezionych liczb pierwszych:',licznik)
    print('Czas wykonania programu: {:.3f}'.format(czas))
    return czas
#pierwsze2(max_l)

import matplotlib.pyplot as plt
x = list(range(1000,20001,1000))
y1=[]
y2=[]
for l in x:
    y1.append(pierwsze1(l))
    y2.append(pierwsze2(l))
plt.plot(x,y1,x,y2)
plt.show()

