from visual import *
from Fizyka.MyMath import Wektor
from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Siatka, Kula

nx = 10
ny = 10
wspolczynnik_sprezystosci = 10
wspolczynnik_tlumienia = 0.1
wspolczynnik_tlumienia_oscylacji = 10
wspolczynnik_sztywnosci = 10
przyspieszenie_ziemskie = Wektor(0, 0, -0.1)
dlugosc_x = 4
dlugosc_y = 4
obszar_zabroniony = Kula(0, 0, Wektor(0.2, 0.2, -1.5), 1.2)

zpm = Siatka(nx, ny,
             wspolczynnik_sprezystosci, wspolczynnik_tlumienia,
             wspolczynnik_tlumienia_oscylacji, wspolczynnik_sztywnosci,
             przyspieszenie_ziemskie,
             dlugosc_x, dlugosc_y,
             obszar_zabroniony)

sphere(pos=obszar_zabroniony.srodek.xyz(), radius=obszar_zabroniony.promien)
symulacja = Symulacja([zpm], rysuj_linie=False)
# symulacja.schowaj_punkty()
symulacja.glowna_petla()
