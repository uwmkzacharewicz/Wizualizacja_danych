import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

print("======================================================================")
print("=====================  ZADANIE 1  ====================================")
dane = df.groupby('Rok').sum()

wykres = dane.plot(marker='o', markersize=8, markerfacecolor='red')
plt.xticks(dane.index.tolist(), rotation=70)
plt.legend(loc="upper right")
plt.title('Liczba urodzeń w poszczególnych latach', fontsize=16)
plt.show()

print("======================================================================")
print("=====================  ZADANIE 2  ====================================")
dane1 = df.groupby('Plec').Liczba.sum()
print(dane1)

wykres1 = dane1.plot.bar(color='green')
wykres1.set_ylabel("Mln")
wykres1.set_xlabel("Płeć")
plt.title('Liczba urodzeń kobiet i mężczyzn', fontsize=16)
plt.xticks(np.arange(2), ['Kobieta', 'Mężczyzna'], rotation=0)
plt.show()

print("======================================================================")
print("=====================  ZADANIE 3  ====================================")
dane2 = df[(df.Rok >= 2013) & (df.Rok <= 2017)].groupby('Plec').agg({'Liczba': ['sum']})
print(dane2)

wykres2 = dane2.plot.pie(subplots=True, autopct='%.2f %%', fontsize=15, figsize=(6, 6), legend=(0, 0),
                         labels=["Kobieta", "Mężczyzna"])
plt.legend(loc="lower right")
plt.title('Liczba urodzeń w ostatnich 5 latach (wg płci)', fontsize=16)
plt.show()

print("=====================  MATPLOTLIB  ==================================")
print("=====================  ZADANIE 1  ====================================")
x = np.linspace(1, 20)
y = 1 / x

plt.plot(x, y, label='f(x) = 1/x')
plt.title('Wykres funkcji f(x) dla [1,20]', fontsize=16)
plt.text(3, 0.4, 'f(x) = 1/x')
plt.legend(loc="upper right")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([1, 20])
plt.ylim([0, 1])

plt.show()

print("=====================  ZADANIE 2  ====================================")

plt.plot(x, y, label='f(x) = 1/x', linestyle=':', marker='>', markersize=5, color='green')
plt.title('Wykres funkcji f(x) dla [1,20]', fontsize=16)
plt.text(3, 0.4, 'f(x) = 1/x')
plt.legend(loc="upper right")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([0, 20])
plt.ylim([0, 1])

plt.show()

print("=====================  ZADANIE 3  ====================================")

x1 = np.arange(0, 30, 0.1)
y1 = np.sin(x1)
y2 = np.cos(x1)

plt.plot(x1, y1, 'b', label='f(x) = sin(x)')
plt.plot(x1, y2, 'g', label='f(x) = cos(x)')
plt.title('Wykres funkcji sin(x) i cos(x)', fontsize=16)
plt.legend(loc="upper right")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([0, 30])
plt.ylim([-1, 1])
plt.show()

print("=====================  ZADANIE 4  ====================================")

df = pd.read_csv('iris.csv', header=0, sep=",", decimal=".", usecols=[0, 1])

data = {'a': df['sepal length'],
        'b': df['sepal width'],
        'c': np.random.randint(0, 50, 150)}
data['d'] = np.abs(data['a'] - data['b']) * 80
print(data)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.show()

# print("=====================  ZADANIE 5  ====================================")


xlsx = pd.ExcelFile('imiona.xlsx')
frame = pd.read_excel(xlsx, header=0)

# Dane do wykresów
dane1 = frame.groupby('Plec').Liczba.sum()
dane2k = frame[frame.Plec == 'K'].groupby('Rok').sum()
dane2m = frame[frame.Plec == 'M'].groupby('Rok').sum()
dane3 = frame.groupby('Rok').Liczba.sum()

# Wykresy

kolor_e = '#3a0ca3'

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.subplots_adjust(wspace=0.25)

# Wykres 1
ax1.set_title("Liczba narodzin w całym okresie", fontsize=18, color=kolor_e)
ax1.set_xlabel("Płeć", fontsize=14, color=kolor_e)
ax1.set_ylabel("Liczba urodzeń", fontsize=14, color=kolor_e)
ax1.bar(dane1.index, dane1,
        width=0.7,
        color="#f72585",
        edgecolor='#3a0ca3',
        linewidth=2,
        tick_label=["Kobiety", "Mężczyźni"])

# Wykres 2
ax2.set_title("Ilość narodzin wg płci", fontsize=18, color=kolor_e)
ax2.set_xlabel("Rok", fontsize=14, color=kolor_e)
ax2.set_ylabel("Liczba urodzeń", fontsize=14, color=kolor_e)
ax2.plot(dane2m, color='#4cc9f0', marker='o', markersize=5, markerfacecolor='#4361ee')
ax2.plot(dane2k, color='#f72585', marker='o', markersize=5, markerfacecolor='#b5179e')
ax2.xaxis.grid(True, which='major')
ax2.legend(['Mężczyźni', 'Kobiety'], loc=4, fontsize=12)
ax2.set_xticks(dane2m.index.tolist())
ax2.set_xticklabels(dane2m.index.tolist(), rotation=50)

# Wykres 3
ax3.bar(dane3.index, dane3,
        color="#4361ee",
        edgecolor='#3a0ca3')
ax3.set_title("Ilość narodzin w danym roku", fontsize=18, color=kolor_e)
ax3.set_xlabel("Rok", fontsize=14, color=kolor_e)
ax3.set_ylabel("Liczba urodzeń", fontsize=14, color=kolor_e)
ax3.set_xticks(dane2m.index.tolist())
ax3.set_xticklabels(dane2m.index.tolist(), rotation=90)

plt.show()

print("=========================  ZADANIE 6  ====================================")
df1 = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.', parse_dates=['Data zamowienia'])
print(df1)

sprz = df1.groupby('Sprzedawca').Utarg.sum()

# wyznaczenie najlepszego i najgorszego pracownika (do explode)
najwieksza = sprz[0]
najmniejsza = sprz[0]
inx_najw = 0
inx_najm = 0
wyznacz = np.zeros(len(sprz))

for x in range(len(sprz)):
    if sprz[x] > najwieksza:
        najwieksza = sprz[x]
        inx_najw = x
    if sprz[x] < najmniejsza:
        najmniejsza = sprz[x]
        inx_najm = x

for x in range(len(sprz)):
    if x == inx_najw:
        wyznacz[x] = 0.2
    if x == inx_najm:
        wyznacz[x] = 0.1

# wykres

colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600', '#ffd100']

wykres = sprz.plot.pie(subplots=True,
                       colors=colors,
                       autopct='%.1f%%',
                       explode=wyznacz,
                       # explode=(sprz == max(sprz)) * 0.1,
                       fontsize=14,
                       figsize=(6, 6),
                       legend=None,
                       shadow=True)

plt.title('Suma zamówień dla sprzedawców', fontsize=20)
plt.axes().set_ylabel('')  # proszę wybaczyć błąd :(
plt.show()
