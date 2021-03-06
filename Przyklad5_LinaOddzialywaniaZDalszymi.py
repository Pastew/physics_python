# Ten przykald dziwnie dziala
from Fizyka.Symulacja import Symulacja
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

symulacja = Symulacja(zpm)
symulacja.glowna_petla()
