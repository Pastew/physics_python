from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import OscylatorySprzezone

ilosc = 11
wspolczynnik_sprezystosci = 1
wspolczynnik_tlumienia = 0.0
wspolczynnik_tlumienia_oscylacji = 1
dlugosc = 4.0

zpm = OscylatorySprzezone(ilosc, wspolczynnik_sprezystosci,
                          wspolczynnik_tlumienia,
                          wspolczynnik_tlumienia_oscylacji,
                          dlugosc)

symulacja = Symulacja(zpm)
symulacja.glowna_petla()
