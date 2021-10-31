import math

# Karol Zacharewicz
# Zadanie 1.
# Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
print("============== ZADANIE 1 ==============")
calkowita = 1
calkowita2 = 123
zmiennop = 12.25
zniennop1 = 2.72145
complex1 = 5 + 5j
complex2 = 4j
napis1 = "Żegnaj okrutny świecie"
napis2 = ' '

print(calkowita)
print(calkowita2)
print(zmiennop)
print(zniennop1)
print(complex1)
print(complex2)
print(napis1 + napis2 + napis1)

# Zadanie 2.
# Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
print("============== ZADANIE 2 ==============")
liczba = 1.25
liczba2 = 5

liczba += liczba2
liczba -= liczba2
print(liczba)

nowa_liczba = 100
nowa_liczba /= liczba2
print(nowa_liczba)
nowa_liczba *= liczba
print(nowa_liczba)
nowa_liczba **= 2
print(nowa_liczba)
nowa_liczba %= 25
print(nowa_liczba)

# Zadanie 3.
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
print("============== ZADANIE 3 ==============")
print(math.e)
przyklad1 = math.exp(10)
print(przyklad1)

przyklad2 = math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6)
print(przyklad2)

przyklad3 = math.floor(3.55)
print(przyklad3)

przyklad4 = math.ceil(4.80)
print(przyklad4)

# Zadanie 4.
# Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)
print("============== ZADANIE 4 ==============")
imie = 'JOHN'
nazwisko = 'SMITH'
print(imie.capitalize() + " " + nazwisko.capitalize())

# Zadanie 5.
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się
# słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)
print("============== ZADANIE 5 ==============")
piosenka = "Tra la la la la, fa fa fa..."
znajdz1 = "la"
znajdz2 = "fa"

print(piosenka.count(znajdz1))
print(piosenka.count(znajdz2))

# Zadanie 6
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
print("============== ZADANIE 6 ==============")
tablica_znakow = "Myślę, więc jestem ... A potem zniknął ..."
print(tablica_znakow[1])
# print(tablica_znakow[len(tablica_znakow)-1])
print(tablica_znakow[-1])

# Zadanie 7
# Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy.
# (trzeba użyć metody split)
print("============== ZADANIE 7 ==============")
oddziel = tablica_znakow.split()
print(oddziel)

# Zadanie 8
# Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
print("============== ZADANIE 8 ==============")
satelita = "Księżyc"
odl_do_slonca = 149600000
odl_do_ksiezyca = 384400
ob_ziemi = 40075
masa_slonca = 1.984E30
print('Prędkość światła równa jest %(predkosc_swiatla)d m/s' % {'predkosc_swiatla':int('11DE784A', 16)})
print("Masa słońca jest równa {:.2f} kg, co odpowiada {:d} masom ziemi".format(masa_slonca, 332946))
print("Odległość Gwiazdy od naszej planety równa jest {:20d} km".format(odl_do_slonca))
print('Co odpowiada %(zm).2f okrążeń wokół ziemi' % {'zm':(odl_do_slonca/ob_ziemi)})
print("Odległość Satelity %10s od naszej planety równa jest %d  km" % (satelita, odl_do_ksiezyca))
print("Co dpowiada {:.4f} okrążeń wokół ziemi".format(odl_do_ksiezyca/ob_ziemi))


# Zadanie 9
# Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją,
# a następnie dodaj mniej lubiane sporty na sam koniec.
print("============== ZADANIE 9 ==============")
planety = ["Merkury", "Wenus", "Ziemia", "Mars", "Jowisz", "Saturn", "Uran", "Neptun"]
for item in planety:
    print(item)
planety.reverse()
print(planety)
planety.append("Pluton")
planety.append("Haumea")
planety.append("Makemake")
planety.append("Eris")
print(planety)
planety.sort()
print(planety)

# Zadanie 10
# Stwórz słownik.
print("============== ZADANIE 10 ==============")
adres_Ziemi = {
    "Supercluster": "Supergromada, zgrupowanie setek lub tysięcy grup i gromad galaktyk",
    "Laniakea": "Supergromada Laniakea, supergromada galaktyk o średnicy około 500 milionów lat świetlnych",
    "Local Group": "Grupa Lokalna, grupa kilkudziesięciu galaktyk (co najmniej 54)",
    "Milky Way" : "Droga Mleczna, galaktyka spiralna z poprzeczką, nazywana jest też po prostu Galaktyką",
    "Solar System" : "Układ Słoneczny, układ planetarny, składający się ze Słońca i powiązanych z nim grawitacyjnie ciał niebieskich"
}
print(adres_Ziemi["Milky Way"])
print(adres_Ziemi.keys())
print(adres_Ziemi.values())
