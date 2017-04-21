from random import random

from MyMath import Wektor
from PunktMaterialny import ZbiorPunktowMaterialnych


class Oscylator(ZbiorPunktowMaterialnych):
    def __init__(self, k=0.0):
        self.k = k

        ilosc_punktow_materialnych = 50
        super(Oscylator, self).__init__(ilosc_punktow_materialnych)

        for i in range(ilosc_punktow_materialnych):
            punkt = self.pobierz_punkt_materialny(i)
            punkt.ustaw_polozenie(Wektor(random()*2-1, random()*2-1, random()*2-1))
            punkt.ustaw_predkosc((Wektor((random()*2-1), (random()*2-1), (random()*2-1) )))
            punkt.ustaw_kolor(random(), random(), random())
            punkt.ustaw_promien(random()*0.3)

    def sila(self, i):
        return self.pobierz_punkt_materialny(0).polozenie * (-self.k)


