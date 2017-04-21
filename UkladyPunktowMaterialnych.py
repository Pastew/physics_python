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
            punkt.ustaw_polozenie(Wektor(random() * 2 - 1, random() * 2 - 1, random() * 2 - 1))
            punkt.ustaw_predkosc((Wektor((random() * 2 - 1), (random() * 2 - 1), (random() * 2 - 1))))
            punkt.ustaw_kolor(random(), random(), random())
            punkt.ustaw_promien(random() * 0.3)

    def sila(self, i):
        return self.pobierz_punkt_materialny(0).polozenie * (-self.k)


class OscylatorySprzezone(ZbiorPunktowMaterialnych):
    def __init__(self, ilosc, wspolczynnikSprezystosci, dlugosc, wspolczynnikTlumienia=0.0):
        super(OscylatorySprzezone, self).__init__(ilosc)
        self.k = float(wspolczynnikSprezystosci)
        self.l = float(dlugosc / float(ilosc - 1))
        # Jesli False - sprezyna. Odpycha sie gdy odleglosc < 1, przyciaga gdy wieksza
        # Jesli True - gumka, dziala tylko przyciaganie gdy odleglosc > 1
        self.sprezystoscTylkoPrzyRozciaganiu = False
        self.t = float(wspolczynnikTlumienia)

        for i in range(0, ilosc):
            punkt = self.pobierz_punkt_materialny(i)
            punkt.ustaw_polozenie(Wektor(-dlugosc / float(2.0 + i * self.l), 0, 0))
            #punkt.ustaw_polozenie(Wektor(dlugosc*i, 0, 0))
            punkt.ustaw_predkosc(Wektor(0, 0, 0))
            punkt.ustaw_kolor(0, i / float(ilosc - 1), 1)  # TODO moze trzeba castowac na float

        self.pobierz_punkt_materialny(0).ustaw_predkosc(Wektor(0.3, 0, 0.2))
        #self.pobierz_punkt_materialny(ilosc-1).ustaw_predkosc(Wektor(-0.3, -0.1, 0))
        self.zeruj_predkosc_srednia()

    def sila(self, indeks):
        sila_z_lewej = Wektor(0, 0, 0)
        sila_z_prawej = Wektor(0, 0, 0)

        if indeks > 0:
            do_lewego = self.pobierz_punkt_materialny(indeks-1).polozenie \
                       - self.pobierz_punkt_materialny(indeks).polozenie

            wychylenie = do_lewego.dlugosc() - self.l
            if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                do_lewego.normuj()
                sila_z_lewej = do_lewego * self.k * wychylenie

        if indeks < self.liczba_punktow() - 1:
            do_prawego = self.pobierz_punkt_materialny(indeks + 1).polozenie \
                        - self.pobierz_punkt_materialny(indeks).polozenie
            wychylenie = do_prawego.dlugosc() - self.l

            if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                do_prawego.normuj()
                sila_z_prawej = do_prawego * self.k * wychylenie

        sila = sila_z_lewej + sila_z_prawej
        if self.t != 0:
            sila -= self.pobierz_punkt_materialny(indeks).predkosc * (self.t * 2.0)
        return sila
