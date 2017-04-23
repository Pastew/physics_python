from Fizyka.MojeOkno import MojeOkno
from Fizyka.UkladyPunktowMaterialnych import UsztywnioneOscylatorySprzezone

ilosc = 10
wspolczynnik_sprezystosci = 0
wspolczynnik_tlumienia = 0
wspolczynnik_tlumienia_oscylacji = 0
wspolczynnik_sztywnosci = 1
dlugosc = 4

# zpm = UsztywnioneOscylatorySprzezone(ilosc,
#                                     wspolczynnik_sprezystosci,
#                                     wspolczynnik_tlumienia,
#                                     wspolczynnik_tlumienia_oscylacji,
#                                     wspolczynnik_sztywnosci,
#                                     dlugosc)

zpm = UsztywnioneOscylatorySprzezone(10, 0, 0, 0, 1, 4)
moje_okno = MojeOkno(zpm)
moje_okno.glowna_petla()
