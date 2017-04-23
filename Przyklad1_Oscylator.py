# Ten przyklad nie dziala. Chyba sily sztywnosci sa zle zaimplementowane

from Fizyka.Symulacja import Symulacja
from Fizyka.UkladyPunktowMaterialnych import Oscylator

zpm = Oscylator(1)

moje_okno = Symulacja(zpm, rysuj_linie=False)
moje_okno.glowna_petla()
