import random

from ciagi import *


# zadanie 1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
print("\n----- ZADANIE 1 -----")
A = [1-x for x in range(1, 10)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

# zadanie 2
# Wygeneruj losowo 10 elementów, zapisz je do listy1,
# następnie wykorzystując Python Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy
print("\n----- ZADANIE 2 -----")
lista1 = random.sample(range(0, 100), 10)
print(lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)
lista2.sort()
print(lista2)

# zadanie 3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu
# a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
print("\n----- ZADANIE 3 -----")
warzywniak = {"Pomidor": "szt", "Cebula": "kg", "Ananas": "szt", "Ogórek": "kg"}
print(warzywniak)
# na_sztuki = {key:value for (key,value) in warzywniak.items() if value == 'szt'}
lista_sztuki = [x[0] for x in warzywniak.items() if x[1] == 'szt']
print(lista_sztuki)

# zadanie 4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

print("\n----- ZADANIE 4 -----")


def tr_prost(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if (a >= b) and (a >= c):
            return a ** 2 == b ** 2 + c ** 2
        elif (b >= a) and (b >= c):
            return b ** 2 == a ** 2 + c ** 2
        else:
            return c ** 2 == a ** 2 + b ** 2
    else:
        return False


print(tr_prost(10, 4, 5))
print(tr_prost(3, 4, 5))
print(tr_prost(5, 12, 13))
print(tr_prost(15, 8, 17))
print(tr_prost(12, 12, 12))

# zadanie 5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
print("\n----- ZADANIE 5 -----")


def pole_trapez(a=5, b=2, h=10):
    return (a+b)*h/2


print(pole_trapez(12))
print(pole_trapez(2, 10, 5))
print(pole_trapez(h=4, a=7, b=15))
print(pole_trapez(h=12))

# zadanie 6
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

print("\n----- ZADANIE 6 -----")


def ciag(a=1, b=4, ile=10):
    lista = [a]
    for x in range(ile):    # 10 razy mnozy, czyli 11 wyrazow
        wynik = lista[x]*b
        lista.append(wynik)
    return lista


def ciag2(a=1, b=4, ile=10):
    return [a * b ** x for x in range(ile+1)]


print(ciag())
print(ciag2())

print(ciag(2, 4, 12))
print(ciag2(2, 4, 12))

# zadanie 7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.
print("\n----- ZADANIE 7 -----")


def ciag2(*liczby, b=2):
    iloczyn = 1
    if len(liczby):
        for i in liczby:
            iloczyn *= i*b
        return iloczyn
    else:
        return 0


print(ciag2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, b=4))

# zadanie 8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci:
# klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.
print("\n----- ZADANIE 8 -----")


def zakupy(**produkty):
    ilosc = len(produkty)
    wartosc = 0
    for pr in produkty:
        wartosc += produkty[pr]
        print("{}\t: {:.2f}".format(pr, produkty[pr]))
    print("== {} pozycji ===" .format(ilosc))
    print("================" .format(ilosc))
    return wartosc


zakup = zakupy(majonez=5.25, kapusta=4.25, pomidor=1.75, chleb=3.20, mars=3.00, LMblue=17.20)
print("=== {} zł === ".format(zakup))

# zadanie 9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych
# z ciągami arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

print("\n----- ZADANIE 9 -----")
print("\n----- ARYTMETYCZNY -----")
ciag_arytm.wyswietl_ciag(5, -5, 6)
ciag_arytm.wyswietl_ciag(1, 7, 10)
print(ciag_arytm.suma_n_wyrazow(10, 5, -5))

ciag1 = [11, 8, 5, 2, -1]
print(ciag_arytm.w_roznica(ciag1[1], ciag1[0]))
print(ciag_arytm.suma_n_wyrazow(len(ciag1), ciag1[0], ciag_arytm.w_roznica(ciag1[1], ciag1[0])))

print("\n----- GEOMETRYCZNY -----")
print(ciag_geom.suma_n_wyrazow(10, 1, 4))
print(ciag_geom.n_wyraz(9, 1, 2))
print(ciag_geom.suma_n_wyrazow(5, 1, 2))

ciag_geom.wyswietl_ciag(1, 2, 10)
ciag2 = [1, 2, 4, 8, 16, 32, 64, 128]

print(ciag_geom.suma_n_wyrazow(len(ciag2), ciag2[0], ciag_geom.w_iloraz(ciag2[1], ciag2[0])))

# zadanie 10
# Z przedziału od 0 do 100 wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
print("\n----- ZADANIE 10 -----")
lista_liczb = [x for x in range(0, 100) if x % 4 == 0]
print("Otwarcie pliku")
file = open("podzielneprzez4.txt", "w")
file.writelines(str(lista_liczb))
file.close()

file1 = open("podzielneprzez4_2.txt", "w")

for x in range(100):
    if x % 10 == 0 and x != 0:
        file1.write("\n")
    if x % 4 == 0:
        file1.write(str(x) + "\t")

file1.close()

# zadanie 11
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli
print("\n----- ZADANIE 11 -----")
file2 = open("podzielneprzez4.txt", "r")
file3 = open("podzielneprzez4_2.txt", "r")

print(file2.readline())
cala_zawartosc = file3.read()
print(cala_zawartosc)

file2.close()
file3.close()
