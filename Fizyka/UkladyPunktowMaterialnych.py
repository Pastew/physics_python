from random import random

from PunktMaterialny import ZbiorPunktowMaterialnych
from visual import *

from Fizyka.MyMath import Wektor


class Oscylator(ZbiorPunktowMaterialnych):
    def __init__(self, k=1.0):
        self.k = k

        super(Oscylator, self).__init__(1)

        punkt = self.pobierz_punkt_materialny(0)
        punkt.ustaw_polozenie(Wektor(-1, 0, 0))
        punkt.ustaw_predkosc(Wektor(1, 1, 0))
        punkt.ustaw_kolor(0, 0.5, 1)
        punkt.ustaw_promien(random.random() * 0.3)

    def sila(self, i):
        return self.pobierz_punkt_materialny(0).polozenie * (-self.k)


class Oscylatory(ZbiorPunktowMaterialnych):
    def __init__(self, k=1.0, ilosc_punktow=10):
        self.k = k

        super(Oscylatory, self).__init__(ilosc_punktow)

        for i in range(0, ilosc_punktow):
            punkt = self.pobierz_punkt_materialny(i)
            polozenie = Wektor(random.random() * 2.0 - 1, random.random() * 2.0 - 1, random.random() * 2.0 - 1)
            punkt.ustaw_polozenie(polozenie)

            predkosc = Wektor(random.random(), random.random(), random.random())
            punkt.ustaw_predkosc(predkosc)

            punkt.ustaw_kolor(random.random(), random.random(), random.random())
            punkt.ustaw_promien(random.random() * 0.3)

    def sila(self, i):
        return self.pobierz_punkt_materialny(0).polozenie * (-self.k)


class OscylatorySprzezone(ZbiorPunktowMaterialnych):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia=0.0, wspolczynnik_tlumienia_oscylacji=0.0,
                 dlugosc=2.0):
        super(OscylatorySprzezone, self).__init__(ilosc)
        self.k = float(wspolczynnik_sprezystosci)
        self.l = float(dlugosc / float(ilosc - 1))
        # Jesli False - sprezyna. Odpycha sie gdy odleglosc < 1, przyciaga gdy wieksza
        # Jesli True - gumka, dziala tylko przyciaganie gdy odleglosc > 1
        self.sprezystoscTylkoPrzyRozciaganiu = False
        self.t = float(wspolczynnik_tlumienia)
        self.tt = float(wspolczynnik_tlumienia_oscylacji)

        for i in range(0, ilosc):
            punkt = self.pobierz_punkt_materialny(i)
            punkt.ustaw_polozenie(Wektor(-dlugosc / 2.0 + i * self.l, 0, 0))
            # punkt.ustaw_polozenie(Wektor(dlugosc*i, 0, 0))
            punkt.ustaw_predkosc(Wektor(0, 0, 0))
            punkt.ustaw_kolor(0, i / float(ilosc - 1), 1)

        self.pobierz_punkt_materialny(ilosc / 2).ustaw_predkosc(Wektor(0, 2.1, 0))
        self.zeruj_predkosc_srednia()

    def sila(self, indeks):
        sila_z_lewej = Wektor(0, 0, 0)
        sila_z_prawej = Wektor(0, 0, 0)

        if indeks > 0:
            do_lewego = self.pobierz_punkt_materialny(indeks - 1).polozenie \
                        - self.pobierz_punkt_materialny(indeks).polozenie

            wychylenie = do_lewego.dlugosc() - self.l
            if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                do_lewego.normuj()
                sila_z_lewej = do_lewego * self.k * wychylenie
                roznica_predkosci = self.pobierz_punkt_materialny(indeks - 1).predkosc \
                                    - self.pobierz_punkt_materialny(indeks).predkosc
                sila_z_lewej += do_lewego * (do_lewego * roznica_predkosci) * self.tt

        if indeks < self.liczba_punktow() - 1:
            do_prawego = self.pobierz_punkt_materialny(indeks + 1).polozenie \
                         - self.pobierz_punkt_materialny(indeks).polozenie
            wychylenie = do_prawego.dlugosc() - self.l

            if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                do_prawego.normuj()
                sila_z_prawej = do_prawego * self.k * wychylenie
                roznica_predkosci = self.pobierz_punkt_materialny(indeks + 1).predkosc - self.pobierz_punkt_materialny(
                    indeks).predkosc
                sila_z_prawej += do_prawego * (do_prawego * roznica_predkosci) * self.tt

        sila = sila_z_lewej + sila_z_prawej
        if self.t != 0:
            sila -= self.pobierz_punkt_materialny(indeks).predkosc * (self.t * 2.0)

        return sila


class UsztywnioneOscylatorySprzezone(OscylatorySprzezone):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc):
        super(UsztywnioneOscylatorySprzezone, self).__init__(ilosc, wspolczynnik_sprezystosci,
                                                             wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                                             dlugosc)
        self.s = float(wspolczynnik_sztywnosci)
        self.sily_sztywnosci = []
        for i in range(0, ilosc):
            self.sily_sztywnosci.append(Wektor(0, 0, 0))

        wielkosc_sily = 0.3
        self.pobierz_punkt_materialny(0).ustaw_predkosc(Wektor(0, wielkosc_sily, 0))
        self.pobierz_punkt_materialny((ilosc - 1) / 2).ustaw_predkosc(Wektor(0, -wielkosc_sily, 0))
        self.pobierz_punkt_materialny((ilosc - 1) / 2 + 1).ustaw_predkosc(Wektor(0, -wielkosc_sily, 0))
        self.pobierz_punkt_materialny(ilosc - 1).ustaw_predkosc(Wektor(0, wielkosc_sily, 0))

    def przed_krokiem_naprzod(self, krok_czasowy):
        super(UsztywnioneOscylatorySprzezone, self).przed_krokiem_naprzod(krok_czasowy)
        for i in range(0, self.liczba_punktow()):
            self.sily_sztywnosci[i] = Wektor(0, 0, 0)
            if self.s == 0:
                return

        for i in range(1, self.liczba_punktow() - 1):
            do_lewego = self.pobierz_punkt_materialny(i - 1).polozenie - self.pobierz_punkt_materialny(i).polozenie
            do_prawego = self.pobierz_punkt_materialny(i + 1).polozenie - self.pobierz_punkt_materialny(i).polozenie
            sila_sztywnosci = (do_lewego + do_prawego) * (self.s / 2.0)
            self.sily_sztywnosci[i] += sila_sztywnosci
            self.sily_sztywnosci[i - 1] -= sila_sztywnosci / 2.0
            self.sily_sztywnosci[i + 1] -= sila_sztywnosci / 2.0

    def sila(self, indeks):
        sila = super(UsztywnioneOscylatorySprzezone, self).sila(indeks)
        if self.s != 0:
            sila += self.sily_sztywnosci[indeks]

        return sila


class Lina(UsztywnioneOscylatorySprzezone):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc):
        super(Lina, self).__init__(ilosc,
                                   wspolczynnik_sprezystosci,
                                   wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                                   wspolczynnik_sztywnosci,
                                   dlugosc)

        self.g = Wektor(0, -9.81, 0)
        self.sprezystoscTylkoPrzyRozciaganiu = False
        for i in range(0, self.ilosc):
            punkt = self.pobierz_punkt_materialny(i)
            punkt.ustaw_predkosc(Wektor(0, 0, 0))

        self.ustaw_wiezy(0, True)
        # self.ustaw_wiezy(ilosc - 1, True)
        # self.ustaw_wiezy(ilosc / 2, True)

    def sila(self, indeks):
        return super(Lina, self).sila(indeks) + self.g * self.pobierz_punkt_materialny(indeks).masa


class LinaOddzialywaniaZDalszymiSasiadami(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc,
                 ile_dodatkowych_oddzialywan=3):
        super(LinaOddzialywaniaZDalszymiSasiadami, self).__init__(ilosc,
                                                                  wspolczynnik_sprezystosci,
                                                                  wspolczynnik_tlumienia,
                                                                  wpolczynnik_tlumienia_oscylacji,
                                                                  wspolczynnik_sztywnosci,
                                                                  dlugosc)

        self.ile_dodatkowych_oddzialywan = ile_dodatkowych_oddzialywan

    def sila(self, indeks):
        sila = super(LinaOddzialywaniaZDalszymiSasiadami, self).sila(indeks)

        for n in range(2, self.ile_dodatkowych_oddzialywan + 2):
            sila_z_lewej = Wektor(0, 0, 0)
            sila_z_prawej = Wektor(0, 0, 0)

            if indeks >= n:
                od_lewego = self.pobierz_punkt_materialny(indeks).polozenie \
                            - self.pobierz_punkt_materialny(indeks - n).polozenie
                wychylenie = od_lewego.dlugosc() - n * self.l
                if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                    od_lewego.normuj()
                    sila_z_lewej = od_lewego * wychylenie * -self.k

            if indeks < self.liczba_punktow() - n:
                do_prawego = self.pobierz_punkt_materialny(indeks + n).polozenie \
                             - self.pobierz_punkt_materialny(indeks).polozenie
                wychylenie = do_prawego.dlugosc() - n * self.l
                if not self.sprezystoscTylkoPrzyRozciaganiu or wychylenie > 0:
                    do_prawego.normuj()
                    sila_z_prawej = do_prawego * wychylenie * self.k

        sila += sila_z_prawej
        sila += sila_z_lewej

        return sila


class Wlos(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc):
        super(Wlos, self).__init__(ilosc,
                                   wspolczynnik_sprezystosci,
                                   wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                                   wspolczynnik_sztywnosci,
                                   dlugosc)

        self.ustaw_wiezy(0, True)
        self.ustaw_wiezy(1, True)


class LinaZPodlozem(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc,
                 poziom_podloza_y=-1.0):
        super(LinaZPodlozem, self).__init__(ilosc,
                                            wspolczynnik_sprezystosci,
                                            wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                                            wspolczynnik_sztywnosci,
                                            dlugosc)

        self.poziom_podloza_y = poziom_podloza_y

    def po_kroku_naprzod(self, krok_czasowy):
        for i in range(0, self.liczba_punktow()):
            punkt = self.pobierz_punkt_materialny(i)
            if punkt.polozenie.y <= self.poziom_podloza_y:
                punkt.polozenie.y = self.poziom_podloza_y
                punkt.predkosc.y = 0

    def sila(self, indeks):
        sila = super(LinaZPodlozem, self).sila(indeks)
        sp = 1.1  # wspolczynnik tarcia podloza
        punkt = self.pobierz_punkt_materialny(indeks)
        if punkt.polozenie.y <= self.poziom_podloza_y:
            sila += punkt.predkosc * (-2 * sp)

        return sila
