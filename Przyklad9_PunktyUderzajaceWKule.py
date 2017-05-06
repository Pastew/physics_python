from visual import *
from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import PunktyUderzajaceWKule

ilosc = 20

zpm = PunktyUderzajaceWKule(ilosc)

# Rysuj kule
oz_kula = zpm.obszar_zabroniony
scene.autocenter = False
sphere(pos=oz_kula.srodek.xyz(), radius=oz_kula.promien)

symulacja = Symulacja([zpm], rysuj_linie=False)
symulacja.glowna_petla()
