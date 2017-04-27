from Fizyka.MyMath import Wektor
from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import KrzywaLissajous, Iskry
from visual import *
zpm = Iskry()

scene.autocenter = False
#scene.autoscale = False
symulacja = Symulacja(zpm, rysuj_linie=False)
symulacja.schowaj_uklad_wspolrzednych()
symulacja.glowna_petla()
