from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Lina

ilosc = 10
wspolczynnik_sprezystosci = 1000
wspolczynnik_tlumienia = 0.02
wspolczynnik_tlumienia_oscylacji = 10
wspolczynnik_sztywnosci = 1
dlugosc = 4

zpm = Lina(ilosc, wspolczynnik_sprezystosci,
           wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
           wspolczynnik_sztywnosci, dlugosc)

moje_okno = Symulacja(zpm)
moje_okno.glowna_petla()
