#Wypisuje na ekranie tabliczkę mnożenia, ładnie sformatowaną
print('Tabliczka mnożenia\n'+18*'-')
for i in range(1,11):
    for j in range(1,11):
        print('{:4d}'.format(i*j),end='')
    print('')
    
        
