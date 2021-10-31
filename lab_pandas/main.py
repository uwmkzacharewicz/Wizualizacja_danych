import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
frame = pd.read_excel(xlsx, header=0)
print(frame)

print("======================================================================")
print("=> tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku")
print(frame[frame.Liczba > 1000])

print("======================================================================")
print("=> tylko rekordy gdzie imie = KAROL")
print(frame[frame.Imie == 'KAROL'])

print("======================================================================")
print("=> sumę wszystkich urodzonych dzieci w całym danym okresie")
# print(frame['Liczba'].sum())
print(frame.Liczba.sum())

print("======================================================================")
print("=> sumę dzieci urodzonych w latach 2000-2005")
print(frame[(frame.Rok >= 2000) & (frame.Rok <= 2005)].Liczba.sum())

print("======================================================================")
print("=> sumę urodzonych chłopców i dziewczynek")
kobiety = (frame[(frame.Plec == 'K')].Liczba.sum())
mezczyzni = (frame[(frame.Plec == 'M')].Liczba.sum())
print("Kobiet: {}, Mężczyzn: {}".format(kobiety, mezczyzni))

print("======================================================================")
print("=> najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)")


def wybierz(df):
    row1 = df[(df.Plec == 'K')].sort_values(by='Liczba')[-1:]
    row2 = df[(df.Plec == 'M')].sort_values(by='Liczba')[-1:]
    nowy = pd.DataFrame(row1)
    nowy = nowy.append(row2)
    return nowy


print(frame.groupby('Rok').apply(wybierz))

print("======================================================================")
print("=> najbardziej popularne imię dziewczynki i chłopca w całym danym okresie ")
naj_k = frame[(frame.Plec == 'K')].groupby('Imie').Liczba.sum().sort_values()[-1:]
naj_m = frame[(frame.Plec == 'M')].groupby('Imie').Liczba.sum().sort_values()[-1:]
print(naj_k)
print(naj_m)

print("======================================================================")
print("======================================================================")
# ZADANIE 2
print("=============================  ZADANIE 2  ============================")
df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.', parse_dates=['Data zamowienia'])
print(df)

print("======================================================================")
print("=>listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame) ")
unikalne = df.Sprzedawca.unique()
print(unikalne)

print("======================================================================")
print("=>5 najwyższych wartości zamówień")
print(df['Utarg'].sort_values(ascending=False)[0:5])

print("======================================================================")
print("=>ilość zamówień złożonych przez każdego sprzedawcę")
ilosc_z = df.groupby('Sprzedawca').idZamowienia.count()
print(ilosc_z)
ilosc_wsz = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count'], 'Utarg': ['sum']})
print(ilosc_wsz)

print("======================================================================")
print("=>Sumę zamówień dla każdego kraju ")
# suma_k = df.groupby('Kraj').Utarg.sum()
suma_z = df.groupby(['Kraj']).agg({'idZamowienia': ['count'], 'Utarg': ['sum']})
print(suma_z)

print("======================================================================")
print("=> sumę zamówień dla roku 2005, dla sprzedawców z Polski")
print(df[(df['Data zamowienia'].dt.year == 2005) & (df['Kraj'] == 'Polska')].Utarg.sum())

print("======================================================================")
print("=>średnią kwotę zamówienia w 2004 roku")
srednia = df[(df['Data zamowienia'].dt.year == 2004)].Utarg.mean()
print("Srednia z roku 2004: {:.2f}".format(srednia))

print("======================================================================")
print("=>zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv")
dane_2004 = df[df['Data zamowienia'].dt.year == 2004]
dane_2005 = df[df['Data zamowienia'].dt.year == 2005]

dane_2004.to_csv('zamowienia_2004.csv', index=False)
dane_2005.to_csv('zamowienia_2005.csv', index=False)
