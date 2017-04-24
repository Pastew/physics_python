from Fizyka.MyMath import Wektor
from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import KrzywaLissajous

punkt_poczatkowy = Wektor(-1, -1, 0)
k1 = 4
k2 = 9

# Mozna poeksperymentowac z roznymi k1 i k2
# k1 = 3.14/4.0
# k2 = 3.14/2.0

zpm = KrzywaLissajous(k1, k2)

symulacja = Symulacja(zpm, rysuj_linie=False)
symulacja.glowna_petla()
