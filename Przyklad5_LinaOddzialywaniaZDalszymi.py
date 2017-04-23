# Ten przykald dziwnie dziala
from Fizyka.MojeOkno import MojeOkno
from Fizyka.UkladyPunktowMaterialnych import LinaOddzialywaniaZDalszymiSasiadami

ilosc = 10
wspolczynnik_sprezystosci = 1000
wspolczynnik_tlumienia = 0.02
wspolczynnik_tlumienia_oscylacji = 10
wspolczynnik_sztywnosci = 0
dlugosc = 4

ile_dodatkowych_oddzialywan = 3

zpm = LinaOddzialywaniaZDalszymiSasiadami(ilosc, wspolczynnik_sprezystosci,
                                          wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                          wspolczynnik_sztywnosci, dlugosc,
                                          ile_dodatkowych_oddzialywan)

moje_okno = MojeOkno(zpm)
moje_okno.glowna_petla()
