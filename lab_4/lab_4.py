import numpy as np
import random

# Zadanie 1
# Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.
print("=========  ZADANIE 1  =============")

x = np.arange(3, (15*3)+1, 3)
print(x)

print("===================================")

# Zadanie 2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych
# a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64
print("=========  ZADANIE 2  =============")

arr = np.array([1.75, 2.25, 3.5, 4.99, 5.01])
print(arr)
print(arr.dtype)

int_arr = arr.astype(np.int64)
print(int_arr)
print(int_arr.dtype)

print("===================================")

# Zadanie 3
# Napisz funkcję, która będzie:
# •	Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# •	Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
print("=========  ZADANIE 3  =============")


def stworz_tablice(n):
    arr1 = np.array([x + 1 for x in range(0, n*n)])
    arr1 = arr1.astype(int)
    arr1 = arr1.reshape((n, n))
    return arr1


nowa_tablica = stworz_tablice(6)
print(nowa_tablica)

print("===================================")


# Zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry:
# liczbę, która będzie podstawą operacji potęgowania oraz
# ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg
# podanej liczby, np. generuj(2,4) -> [2,4,8,16]
print("=========  ZADANIE 4  =============")


def generuj(liczba, ile):
    arr2 = np.logspace(1, ile, ile, base=liczba)
    arr2 = arr2.astype(int)
    return arr2


arr = generuj(2, 4)
print(arr)

print("===================================")

# Zadanie 5
# Napisz funkcję, która:
# •	Na wejściu przyjmuje jeden parametr określający długość wektora
# •	Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# •	Generuj macierz diagonalną z w/w wektorem jako przekątną
print("=========  ZADANIE 5  =============")


def stworz_macierz_diag(n):
    wektor = np.array([a for a in range(n)])
    return np.diag(wektor[::-1])


mat_diag = stworz_macierz_diag(5)
print(mat_diag)

print("===================================")

# Zadanie 6
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa)
# w postaci wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie,
# jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane
# od prawej do lewej.
print("=========  ZADANIE 6  =============")

dl_n = 6
# utworzenie losowej wykreslanki
wykresl = np.empty((dl_n, dl_n), dtype='S1')

for i in range(dl_n):
    for j in range(dl_n):
        wykresl[i][j] = chr(random.randint(65, 90))

print(wykresl)

print("+++++++++++++++++++++++++")

dl_n = 6

slowo1 = 'KAMERA'
slowo2 = 'REALIA'
slowo3 = 'PIASEK'

tab_slow1 = np.array(list(slowo1), dtype='S1')
tab_slow2 = np.array(list(slowo2), dtype='S1')
tab_slow3 = np.array(list(slowo3), dtype='S1')

# POZIOMO: wyciecie pierwszego wiersza
ciach = wykresl[0]
# wstawienie slowo1
ciach[0:6] = tab_slow1

# PIONOWO: bezposrednia zmiana 5 kolumny
wykresl[:, 4] = tab_slow2

# SKOS: Wstawienie słowa przez for
# przekatna: [i][i] w od prawej do lewej

tab_slow3 = tab_slow3[::-1]

for i in range(dl_n):
    wykresl[i][i] = tab_slow3[i]
print(wykresl)

print("===================================")

# Zadanie 7
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n
# i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych
# rozchodzących się od głównej przekątnej.
print("=========  ZADANIE 7  =============")


def macierz_w(n, liczba):           # dołożyłem dodatkowy parametr dla liczby
    tab = np.diag(np.ones(n), k=0)
    tab = tab.astype(np.int)
    np.fill_diagonal(tab, liczba)

    for y in range(1, n):
        np.fill_diagonal(tab[y:, :], (y + 1) * liczba)
        np.fill_diagonal(tab[:, y:], (y + 1) * liczba)

    return tab


A = macierz_w(10, 2)
print(A)

print("===================================")

# Zadanie 8
# Napisz funkcję, która:
# •	jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy
#   oraz parametr ‘kierunek’,
# •	parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# •	funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat,
#   że ilość wierszy lub kolumn, w zależności od kierunku podziału,
#   nie pozwala na operację)
print("=========  ZADANIE 8  =============")


def podziel_tablice(tab, kierunek):
    # sprawdzenie rozmiaru tablicy
    # kierunek = 0 => POZIOMO
    #            1 => PIONOWO

    rz, kol = tab.shape

    if kierunek == 0:
        if rz % 2 != 0:
            print("Nie można podzielić poziomo")
            return 0, 0

        gora = tab[0:int(rz / 2)]
        dol = tab[int(rz / 2):int(rz)]

        return gora, dol

    if kierunek == 1:
        # sprawdzenie rozmiaru:
        if kol % 2 != 0:
            print("Nie można podzielić pionowo")
            return 0, 0

        lewa = tab[:, :int(kol / 2)]
        prawa = tab[:, int(kol / 2):]

        return lewa, prawa


tab1 = np.zeros((5, 2))
tab2 = np.zeros((2, 3))
tab3 = np.zeros((4, 4))
tab4 = np.zeros((4, 2))
tab5 = np.zeros((2, 5))

print("=============================")

print("tab1(5,2) - poziomo:")
t1, t2 = podziel_tablice(tab1, 0)

print("tab1(5,2) - pionowo:")
t3, t4 = podziel_tablice(tab1, 1)
print(t3)
print(t4)

print("tab2(2,3) - poziomo:")
t5, t6 = podziel_tablice(tab2, 0)
print(t5)
print(t6)

print("tab2(2,3) - pionowo:")
t7, t8 = podziel_tablice(tab2, 1)
print(t7)
print(t8)

print("tab4(4,4) - poziomo:")
t9, t10 = podziel_tablice(tab4, 0)
print(t9)
print(t10)

print("tab4(4,4) - pionowo:")
t11, t12 = podziel_tablice(tab4, 1)
print(t11)
print(t12)
print("===================================")

# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy
# i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
print("=========  ZADANIE 9  =============")

n = 5

ciag_fib = np.ones(n*n)
ciag_fib = ciag_fib.astype(int)

for x in range(2, n*n):
    ciag_fib[x] = ciag_fib[x-2] + ciag_fib[x-1]

ciag_fib = ciag_fib.reshape(5, 5)
print(ciag_fib)

print("===================================")