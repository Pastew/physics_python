from visual import *
from Fizyka.Symulacja import Symulacja
from Fizyka.MyMath import Wektor
from Fizyka.UkladyPunktowMaterialnych import LinaZPodlozem, LinaZPodlozem2

ilosc = 10
wspolczynnik_sprezystosci = 50
wspolczynnik_tlumienia = 0.2
wspolczynnik_tlumienia_oscylacji = 1
wspolczynnik_sztywnosci = 10
dlugosc = 5
poziom_podloza_y = -3

zpm = LinaZPodlozem2(ilosc, wspolczynnik_sprezystosci,
                    wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                    wspolczynnik_sztywnosci, dlugosc, poziom_podloza_y=poziom_podloza_y)

# zpm.pobierz_punkt_materialny(0).ustaw_polozenie(Wektor(0, 0, 0))
zpm.pobierz_punkt_materialny(zpm.ilosc - 1).ustaw_polozenie(Wektor(1.2, 0.3, -0.1))

# Rysuj podloge
box_height = 0.5
box(pos=[0, poziom_podloza_y -  box_height, 0], height=box_height, width=10, length=10)

symulacja = Symulacja([zpm])
# symulacja.schowaj_punkty()
symulacja.kolor_linii([0.6, 0.1, 0.2])
symulacja.grubosc_linii(0.05)
symulacja.glowna_petla()
