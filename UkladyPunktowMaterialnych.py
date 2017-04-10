from MyMath import Wektor
from PunktMaterialny import ZbiorPunktowMaterialnych


class Oscylator(ZbiorPunktowMaterialnych):
    def __init__(self, k=0.0):
        self.k = k

        ilosc_punktow_materialnych = 1
        super(Oscylator, self).__init__(ilosc_punktow_materialnych)

        punkt = self.pobierz_punkt_materialny(0)
        punkt.ustaw_polozenie(Wektor(-1.0, 0.0, 0.0))
        punkt.ustaw_kolor(0.0, 1.0, 0.5)
        punkt.ustaw_promien(0.3)

    def sila(self, i):
        return  self.pobierz_punkt_materialny(0).polozenie * (-self.k)


