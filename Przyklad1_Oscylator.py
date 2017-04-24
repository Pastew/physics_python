from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Oscylator

zpm = Oscylator(2)

symulacja = Symulacja(zpm, rysuj_linie=False)
symulacja.glowna_petla()
