from visual import *
from Fizyka.Symulacja import Symulacja
from Fizyka.MyMath import Wektor
from Fizyka.UkladyPunktowMaterialnych import Wlos

ilosc = 5
wspolczynnik_sprezystosci = 10
wspolczynnik_tlumienia = 0.1
wspolczynnik_tlumienia_oscylacji = 0
wspolczynnik_sztywnosci = 100
dlugosc = 2.0

zpm = Wlos(ilosc, wspolczynnik_sprezystosci,
           wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
           wspolczynnik_sztywnosci, dlugosc)

zpm.g.y = -0.1

l = dlugosc / float(ilosc)  # odleglosc miedzy punktami
# wlos, czy trawa, zacznie sie w punkcie 0,0,0 i idzie do gory pionowo
for i in range(0, zpm.ilosc):
    punkt = zpm.pobierz_punkt_materialny(i)
    polozenie = Wektor(0.1 * i, i * l, 0.1 * i)
    punkt.ustaw_polozenie(polozenie)

box(pos=[0, 0, 0], height=0.5, width=5, length=10)

symulacja = Symulacja(zpm)
# symulacja.schowaj_punkty()
symulacja.kolor_linii([0.8, 0.2, 0.2])
symulacja.glowna_petla()
