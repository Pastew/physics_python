from visual import *

from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import LinaZWalcemNieograniczonymWKierunkuZ

ilosc = 20
wspolczynnik_sprezystosci = 200
wspolczynnik_tlumienia = 0.2
wspolczynnik_tlumienia_oscylacji = 1
wspolczynnik_sztywnosci = 10
dlugosc = 5
poziom_podloza_y = -3

zpm = LinaZWalcemNieograniczonymWKierunkuZ(ilosc, wspolczynnik_sprezystosci,
                                           wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                           wspolczynnik_sztywnosci, dlugosc)

# Rysuj walec
oz_walec = zpm.obszar_zabroniony
scene.autocenter = False
cylinder(pos=oz_walec.srodek.xyz(), radius=oz_walec.promien, axis=(0, 0, 10))

symulacja = Symulacja([zpm], rysuj_linie=True)
#symulacja.schowaj_punkty()
symulacja.glowna_petla()
