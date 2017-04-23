# Ten przyklad nie dziala. Chyba sily sztywnosci sa zle zaimplementowane

from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Oscylatory

k = 10
liczba_punktow = 50
zpm = Oscylatory(k, liczba_punktow)

moje_okno = Symulacja(zpm, rysuj_linie=False)
moje_okno.glowna_petla()
