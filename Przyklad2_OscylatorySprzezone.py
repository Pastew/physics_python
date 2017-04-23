from Fizyka.MojeOkno import MojeOkno
from Fizyka.UkladyPunktowMaterialnych import OscylatorySprzezone

ilosc = 10
wspolczynnik_sprezystosci = 1
wspolczynnik_tlumienia = 0.0
wspolczynnik_tlumienia_oscylacji = 1
dlugosc = 4.0

zpm = OscylatorySprzezone(ilosc, wspolczynnik_sprezystosci,
                          wspolczynnik_tlumienia,
                          wspolczynnik_tlumienia_oscylacji,
                          dlugosc)

moje_okno = MojeOkno(zpm)
moje_okno.glowna_petla()
