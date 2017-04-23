from visual import *

from Fizyka.MojeOkno import MojeOkno
from Fizyka.MyMath import Wektor
from Fizyka.UkladyPunktowMaterialnych import LinaZPodlozem

ilosc = 20
wspolczynnik_sprezystosci = 50
wspolczynnik_tlumienia = 0.02
wspolczynnik_tlumienia_oscylacji = 1
wspolczynnik_sztywnosci = 10
dlugosc = 5
poziom_podloza_y = -3

zpm = LinaZPodlozem(ilosc, wspolczynnik_sprezystosci,
                    wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                    wspolczynnik_sztywnosci, dlugosc, poziom_podloza_y=poziom_podloza_y)

#zpm.pobierz_punkt_materialny(0).ustaw_polozenie(Wektor(0, 0, 0))
zpm.pobierz_punkt_materialny(zpm.ilosc - 1).ustaw_polozenie(Wektor(1.2, 0.3, -0.1))

# Rysuj podloge
box_height = 0.5
box(pos=[0, poziom_podloza_y - 0.5 * box_height, 0], height=box_height, width=5, length=10)

moje_okno = MojeOkno([zpm])
#moje_okno.schowaj_punkty()
moje_okno.kolor_linii([0.6, 0.1, 0.2])
moje_okno.grubosc_linii(0.05)
moje_okno.glowna_petla()
