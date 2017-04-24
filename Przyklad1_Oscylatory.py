from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Oscylatory

k = 10
liczba_punktow = 50
zpm = Oscylatory(k, liczba_punktow)

symulacja = Symulacja(zpm, rysuj_linie=False)
symulacja.glowna_petla()
