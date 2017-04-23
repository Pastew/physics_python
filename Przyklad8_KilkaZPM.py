from visual import *

from Fizyka.MojeOknoKilkaZPM import MojeOknoKilkaZPM
from Fizyka.MyMath import Wektor
from Fizyka.UkladyPunktowMaterialnych import Wlos, LinaZPodlozem


def zbuduj_wlos(x=0.0, y=0.0, z=0.0,
                ilosc=10,
                sprezystosc=10,
                tlumienie=0.1, tlumienie_oscylacji=0.0,
                sztywnosc=100.0,
                dlugosc=10,
                grawitacja_y=-0.1):
    ilosc = int(ilosc)
    wspolczynnik_sprezystosci = float(sprezystosc)
    wspolczynnik_tlumienia = float(tlumienie)
    wspolczynnik_tlumienia_oscylacji = float(tlumienie_oscylacji)
    wspolczynnik_sztywnosci = float(sztywnosc)
    dlugosc = float(dlugosc)

    zpm = Wlos(ilosc, wspolczynnik_sprezystosci,
               wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
               wspolczynnik_sztywnosci, dlugosc)

    zpm.g.y = float(grawitacja_y)

    l = dlugosc / float(ilosc)  # odleglosc miedzy punktami
    # wlos, czy trawa, zacznie sie w punkcie 0,0,0 i idzie do gory pionowo, troche pod katem
    max_range = 0.5
    x_dir = max_range * random.random() - max_range / 2
    z_dir = max_range * random.random() - max_range / 2
    for i in range(0, zpm.ilosc):
        punkt = zpm.pobierz_punkt_materialny(i)
        polozenie = Wektor(x + x_dir * i,
                           y + i * l,
                           z + z_dir * i)
        punkt.ustaw_polozenie(polozenie)

    return zpm


zpms = []
for i in range(0, 8):
    zpms.append(zbuduj_wlos(x=random.random() * 2,
                            z=random.random() * 2,
                            ilosc=random.random() * 8 + 2,
                            dlugosc=random.random() * 5,
                            sprezystosc=random.random() * 5 + 5,
                            sztywnosc=random.random() * 80 + 50)
                )

ilosc = 20
wspolczynnik_sprezystosci = 10
wspolczynnik_tlumienia = 0.02
wspolczynnik_tlumienia_oscylacji = 1
wspolczynnik_sztywnosci = 10
dlugosc = 5
poziom_podloza_y = 0

lina_z_podlozem = LinaZPodlozem(ilosc, wspolczynnik_sprezystosci,
                                wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                wspolczynnik_sztywnosci, dlugosc, poziom_podloza_y=poziom_podloza_y)
lina_z_podlozem.przesun_wszystkie_punkty(Wektor(-5, 3, 2))

zpms.append(lina_z_podlozem)

box(pos=[0, -0.25, 0], height=0.5, width=5, length=20)

moje_okno = MojeOknoKilkaZPM(zpms)
# moje_okno.schowaj_punkty()
moje_okno.grubosc_linii(0.025)
moje_okno.glowna_petla()
