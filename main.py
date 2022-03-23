import math
import random
import ciagi.geometryczne as geo
import ciagi.arytmetyczne as arytm

# zad1
# A = [1-x for x in range (1,11)]
# B = [4**x for x in range(0,8)]
# C = [x for x in B if x%2==0]
#
# print(A,'\n',B,'\n',C)

# zad2
# lista1 = [random.randint(1,9)*x for x in range(1,11)]
# lista2 = [x for x in lista1 if x%2==0]
#
# print(lista1,'\n',lista2)

# zad3
# produkty = {'dlugopis':'szt','ryz':'kg','jaja':'szt','pomidory':'kg','cukierki':'kg'}
# sztuki = [x for x in produkty if produkty[x]=='szt']
#
# print(sztuki)

# zad4
# def trojkat(a,b,c):
#     if a**2+b**2==c**2:
#         return print('trojkat jest prostokatny')
#     else:
#         return print('trojkat nie jest prostokatny')
#
# trojkat(3,4,5)
# trojkat(3,4,6)

# zad5
# def trapez(a=3,b=4,h=2):
#     return print(0.5*(a+b)*h)
#
# trapez()
# trapez(4,5,3)

# zad6
# def ciag(a=1,b=4,ile=10):
#     return [a*(b**x) for x in range(0,ile)]
# print(ciag())

# zad7
# def ciag2(a=1,b=4,*ile):
#     return [a * (b ** x) for x in range(0, *ile)]
# print(ciag2(1,4,10))

# zad8
# def suma_zakupow(**lista):
#     return print('lacznie kupiono {0} produktow za kwote {1}'.format(len(lista),sum(lista.values())))
# suma_zakupow(kasznka=10,pomidor=7,chleb=4,napoj=20,papierosy=15)

# zad9
# print(arytm.utworz(1,4,10))
# print(geo.utworz(1,4,10))

# def zadanie10():
#     liczby = [x for x in range(1,101) if x%4==0]
#     plik = open('zadanie.txt','a+')
#     plik.writelines(str(liczby))
#     plik.close()
#
# zadanie10()

# def zadanie11():
#     plik = open('zadanie.txt','r')
#     tekst = plik.readline()
#     plik.close()
#     return tekst
#
# print(zadanie11())