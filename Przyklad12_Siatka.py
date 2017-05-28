from Fizyka.MyMath import Wektor
from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Siatka

nx = 10
ny = 10
wspolczynnik_sprezystosci = 10
wspolczynnik_tlumienia = 0.1
wspolczynnik_tlumienia_oscylacji = 10
wspolczynnik_sztywnosci = 10
przyspieszenie_ziemskie = Wektor(0, 0, -0.1)
dlugosc_x = 4
dlugosc_y = 4
obszar_zabroniony = None

zpm = Siatka(nx, ny,
             wspolczynnik_sprezystosci, wspolczynnik_tlumienia,
             wspolczynnik_tlumienia_oscylacji, wspolczynnik_sztywnosci,
             przyspieszenie_ziemskie,
             dlugosc_x, dlugosc_y,
             obszar_zabroniony)

zpm.ustaw_wiezy(0,True)
zpm.ustaw_wiezy(nx - 1, True)
zpm.ustaw_wiezy(nx*(nx-1), True)
zpm.ustaw_wiezy(nx*ny-1, True)


krok_czasowy = 0.005
symulacja = Symulacja([zpm], rysuj_linie=False)
#symulacja.schowaj_punkty()
symulacja.glowna_petla()
