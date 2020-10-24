#Liczby pierwsze, dwa algorytmy, wykresy czasu wykonania
import time
print('Program do znajdowania liczb pierwszych')
#max_l = int(input('Podaj, do jakiej wartości szukać liczb pierwszych (>2): '))
#Algorytm 1
def pierwsze1(max_l):
    pierwsza=False
    licznik=1
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
    licznik=1
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

#algorytm 3 - sito Eratostenesa,

def pierwsze3(max_l):
    start = time.time()
    lista = list(range(2,max_l+1))
    for l in lista:
        i = 2
        while i*l<=max_l:
            multiple = l * i
            if multiple in lista:
                lista.remove(multiple)
            i+=1

    koniec = time.time()
    czas = koniec - start
    licznik = len(lista)
    print(10 * '-' + '\nZnalezionych liczb pierwszych:', licznik)
    print('Czas wykonania programu: {:.3f}'.format(czas))
    return czas
import matplotlib.pyplot as plt
x = list(range(1000,20001,1000))
y1=[]
y2=[]
y3=[]
y4=[]

def pierwsze4(n):
    start = time.time()
    is_prime=[True]*(n-1)
    p=2
    licznik=0
    while True:
        multiplier=2
        multiple=p*multiplier
        while multiple<=n:
            is_prime[multiple-2]=False
            multiplier+=1
            multiple=p*multiplier

        for i,prime in enumerate(is_prime):
            if prime and i+2>p:
                p=i+2
                licznik+=1
                break
        else:
            break
    koniec=time.time()
    czas = koniec - start
    print(10 * '-' + '\nZnalezionych liczb pierwszych:', licznik)
    print('Czas wykonania programu: {:.3f}'.format(czas))
    return czas

pierwsze2(10000)
'''
for l in x:
    y1.append(pierwsze1(l))
    y2.append(pierwsze2(l))
    y3.append(pierwsze3(l))
    y4.append(pierwsze4(l))
plt.title('Czas generowania liczb pierwszych')
plt.xlabel('Zbiór liczb')
plt.ylabel('Czas (s)')
plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.show()
'''
