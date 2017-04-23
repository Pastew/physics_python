# Ten przyklad nie dziala. Chyba sily sztywnosci sa zle zaimplementowane

from Fizyka.MojeOkno import MojeOkno
from Fizyka.UkladyPunktowMaterialnych import Oscylator

zpm = Oscylator(1)

moje_okno = MojeOkno(zpm, rysuj_linie=False)
moje_okno.glowna_petla()
