import re

n = int(input())
dokumenty = [input() for _ in range(n)]
zapytanie = input().strip()

dokumenty_tokenizowane = [re.sub(r'\.', '', d).lower().split() for d in dokumenty]
zapytanie_tokenizowane = re.sub(r'\.', '', zapytanie).lower().split()

czestotliwosc_wystepowania_terminow = []
for dokument in dokumenty_tokenizowane:
    czestotliwosc = {}
    liczba_slow = len(dokument)
    for slowo in dokument:
        czestotliwosc[slowo] = czestotliwosc.get(slowo, 0) + 1 / liczba_slow
    czestotliwosc_wystepowania_terminow.append(czestotliwosc)

korpus = sum(dokumenty_tokenizowane, [])
czestotliwosc_korpusu = {}
liczba_slow_korpusu = len(korpus)
for slowo in set(korpus):
    czestotliwosc_korpusu[slowo] = korpus.count(slowo) / liczba_slow_korpusu

prawdopodobienstwa = []
lambda_v = 0.5
for czestotliwosc in czestotliwosc_wystepowania_terminow:
    prawdopodobienstwa.append({
        slowo: lambda_v * czestotliwosc.get(slowo, 0) + (1 - lambda_v) * czestotliwosc_korpusu.get(slowo, 0)
        for slowo in czestotliwosc_korpusu
    })

prawdopodobienstwa_zapytania = []
for p in prawdopodobienstwa:
    wynik = 1
    for slowo in zapytanie_tokenizowane:
        wynik *= p.get(slowo, 0)
    prawdopodobienstwa_zapytania.append(wynik)

ranking = sorted(range(len(dokumenty)), key=lambda i: prawdopodobienstwa_zapytania[i], reverse=True)

print(ranking)
