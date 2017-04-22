# Ten przyklad nie dziala. Chyba sily sztywnosci sa zle zaimplementowane

from MojeOkno import MojeOkno
from UkladyPunktowMaterialnych import Oscylator

zpm = Oscylator(1)

moje_okno = MojeOkno(zpm, rysuj_linie=False)
moje_okno.glowna_petla()
