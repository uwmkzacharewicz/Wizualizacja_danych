import sys as system

# Karol Zacharewicz
# Zadanie 1.
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
print("============== ZADANIE 1 ==============")
zdanie = input("Wpisz zdanie: ")
print(zdanie.count('a'))

# Zadanie 2.
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c.
# Użyj instrukcji readline() i write()).
print("============== ZADANIE 2 ==============")
system.stdout.write("a: ")
liczba_a = system.stdin.readline()
system.stdout.write("b: ")
liczba_b = system.stdin.readline()
system.stdout.write("c: ")
liczba_c = system.stdin.readline()
a = int(liczba_a)
b = int(liczba_b)
c = int(liczba_c)
system.stdout.write(str(a ** b + c))

# Zadanie 3.
# Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
print("\n============== ZADANIE 3 ==============")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a>=b :
    if a>=c :
        print("Liczba {} jest najwieksza" .format(a))
    else :
        print("Liczba {} jest najwieksza" .format(c))
else:
    if b>=c :
        print("Liczba {} jest najwieksza" .format(b))
    else :
        print("Liczba {} jest najwieksza" .format(c))

# Zadanie 4.
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
print("\n============== ZADANIE 4 ==============")
lista = [1, 2.0, 3.25, 5, 6.75]
for item in lista:
    print(item ** 2)

# Zadanie 5.
# Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
print("\n============== ZADANIE 5 ==============")
parzyste = []
licznik = 0
while licznik < 10 :
    liczba = input("Podaj liczbę: ")
    liczba = int(liczba)
    if liczba%2 == 0 :
        parzyste.append(liczba)
    licznik += 1

for item in parzyste:
    print(item)