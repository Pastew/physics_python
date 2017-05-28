from visual import *
from Fizyka.Symulacja import Symulacja
from Fizyka.MyMath import Wektor
from Fizyka.UkladyPunktowMaterialnych import LinaZProstopadloscianemNieograniczonymWKierunkuZ

ilosc = 20
wspolczynnik_sprezystosci = 200
wspolczynnik_tlumienia = 0.2
wspolczynnik_tlumienia_oscylacji = 1
wspolczynnik_sztywnosci = 10
dlugosc = 5
poziom_podloza_y = -3

zpm = LinaZProstopadloscianemNieograniczonymWKierunkuZ(ilosc, wspolczynnik_sprezystosci,
                                                       wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                                       wspolczynnik_sztywnosci, dlugosc)

# zpm.pobierz_punkt_materialny(0).ustaw_polozenie(Wektor(0, 0, 0))
zpm.pobierz_punkt_materialny(zpm.ilosc - 1).ustaw_polozenie(Wektor(1.2, 0.3, -0.1))

minX = -1
maxX = 1
minY = -3.75
maxY = -0.25

y = maxY - minY
x = maxX - minX
# Rysuj prostopadloscian
box(pos=[(minX + maxX)/2, (minY + maxY)/2, 0], height=y, width=10, length=x)

symulacja = Symulacja([zpm])
# symulacja.schowaj_punkty()
symulacja.kolor_linii([0.6, 0.1, 0.2])
symulacja.grubosc_linii(0.05)
symulacja.glowna_petla()
