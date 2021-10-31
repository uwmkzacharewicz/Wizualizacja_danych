import numpy as np

# ZADANIE 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
print("====================  ZADANIE 1  ====================")
x = np.random.randint(10, size=(1, 3))
y = np.random.randint(10, size=(1, 3))
z = np.arange(3)
print(x)
print(y)
print(x * y)            # liczba przez liczbe
# print(y.dot(x))       # iloczyn macierzy
print(np.multiply(x, y))

print("================================")
print(x.dot(y.T))
print(np.multiply(x, y))

# ZADANIE 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny
# i każdego rzędu.
print("====================  ZADANIE 2  ====================")

a = np.random.randint(100, size=(3, 3))
b = np.random.randint(100, size=(4, 4))
print(a)
print(b)

print(a.min(axis=1))         # wiersze
print(a.min(axis=0))         # kolumny
# print(np.amin(a, axis=0))

print(b.min(axis=1))    # wiersze
print(b.min(axis=0))    # kolumny

# ZADANIE 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
# Liczba kolumn pierwszej macieczy musi być równa liczbie wierszy drugiej
# dlatego należy wykonać transponowanie drugiej macierzy
print("====================  ZADANIE 3  ====================")
print(x.dot(y.T))

# ZADANIE 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite,
# a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
print("====================  ZADANIE 4  ====================")
a = np.random.randint(100, size=(1, 3), dtype='int32')
b = np.random.randn(1, 3)
print(a)
print(b)
print(a * b)                    # mnożenie tablicowe
print(np.multiply(a, b))
print(a.dot(b.T))               # mnożenie macierzy przez macierz

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości
# i zapisz do zmiennej “a”.

print("====================  ZADANIE 5  ====================")
A = np.random.randint(10, size=(2, 3))
print(A)
a = np.sin(A)
print(a)

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej
# z jej wartości i zapisz do zmiennej “b”.
print("====================  ZADANIE 6  ====================")
B = np.random.randint(10, size=(2, 3))
print(B)
b = np.cos(B)
print(b)

# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
print("====================  ZADANIE 7  ====================")


def dodaj_macierze(a, b):
    return a + b


print(a)
print(b)
print(dodaj_macierze(a, b))

# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
print("====================  ZADANIE 8  ====================")
X = np.random.randint(100, size=(3, 3))
print(X)

for i in range(X.shape[0]):
    print("Rzad[{}]: {}".format(i, X[i]))

# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając
# z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
print("====================  ZADANIE 9  ====================")
Y = np.random.randint(100, size=(3, 3))
print(Y)
for x in Y.flat:
    print(x)

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
# Rozmiar macierzy kwadratowej nxm musi być równy iloczynie rozmiaru macierzy pierwotnej (9x9=81)
# więc mamy tyle możliwości, ile jest możliwych kombinacji n x m = 81
print("====================  ZADANIE 10  ====================")
M = np.random.randint(100, size=(9, 9))
print(M)
M1 = M.reshape((27, 3))
M2 = M.reshape((3, 27))
M3 = M.reshape((1, 81))
M4 = M.reshape((81, 1))
M5 = M.reshape((9, 9))

# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
print("====================  ZADANIE 11  ====================")

N1 = np.random.randint(100, size=12)
print(N1)
N1 = N1.reshape((3, 4))
print(N1)
N2 = np.random.randint(100, size=12)
print(N2)
N2 = N2.reshape((4, 3))
print(N2)
N3 = np.random.randint(100, size=12)
print(N3)
N3 = N3.reshape((2, 6))
print(N3)

N1 = N1.ravel()
N2 = N2.ravel()
N3 = N3.ravel()

# Ten sam rozmiar wiec pod wzgledem rozmiaru sa identyczne
print(N1)
print(N2)
print(N3)
