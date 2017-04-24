from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import UsztywnioneOscylatorySprzezone

ilosc = 10
wspolczynnik_sprezystosci = 0
wspolczynnik_tlumienia = 0
wspolczynnik_tlumienia_oscylacji = 0
wspolczynnik_sztywnosci = 1
dlugosc = 4

zpm = UsztywnioneOscylatorySprzezone(ilosc,
                                     wspolczynnik_sprezystosci,
                                     wspolczynnik_tlumienia,
                                     wspolczynnik_tlumienia_oscylacji,
                                     wspolczynnik_sztywnosci,
                                     dlugosc)

symulacja = Symulacja(zpm)
symulacja.glowna_petla()
