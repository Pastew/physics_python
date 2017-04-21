from MyMath import Wektor, Kolor
from visual import *
from enum import Enum


class Algorytm(Enum):
    EULER = 1
    VERLET = 2


class ZbiorPunktowMaterialnych(object):
    def __init__(self, ilosc):
        self.ilosc = ilosc

        #: :type: list of PunktMaterialny
        self.punkty = []

        # self.punkty = [] # type: list[PunktMaterialny] <- this is for python 3.6
        #: :type: list of bool
        self.wiezy = []
        for i in range(ilosc):
            self.punkty.append(PunktMaterialny())
            self.wiezy.append(False)

    def sila(self, i):
        return Wektor()

    def przygotuj_ruch(self, krok_czasowy, algorytm=Algorytm.EULER):
        for i in range(self.ilosc):
            if self.wiezy[i] is False:
                self.punkty[i].przygotuj_ruch(self.sila(i), krok_czasowy, algorytm)

    def wykonaj_ruch(self):
        for i in range(self.ilosc):
            self.punkty[i].wykonaj_ruch()

    def krok_naprzod(self, krok_czasowy, algorytm):
        self.przed_krokiem_naprzod(krok_czasowy)
        self.przygotuj_ruch(krok_czasowy, algorytm)
        self.po_przygotowaniu_ruchu(krok_czasowy)
        self.wykonaj_ruch()
        self.po_kroku_naprzod(krok_czasowy)

    def przed_krokiem_naprzod(self, krok_czasowy):
        pass

    def po_przygotowaniu_ruchu(self, krok_czasowy):
        pass

    def po_kroku_naprzod(self, krok_czasowy):
        pass

    def srodek_masy(self):
        srodek_masy = Wektor(0.0, 0.0, 0.0)
        for i in range(self.ilosc):
            srodek_masy += self.punkty[i].polozenie

        srodek_masy /= self.ilosc
        return srodek_masy

    def zeruj_predkosc_srednia(self):
        ilosc_z_wiezami = 0
        predkosc_srednia = Wektor(0.0, 0.0, 0.0)
        for i in range(self.ilosc):
            if self.wiezy[i] is False:
                predkosc_srednia += self.pobierz_punkt_materialny(i).predkosc
            else:
                ilosc_z_wiezami += 1

        predkosc_srednia /= self.ilosc - ilosc_z_wiezami

    def pobierz_punkt_materialny(self, i):
        if i < 0 or i >= self.ilosc:
            return None
        return self.punkty[i]

    def liczba_punktow(self):
        return self.ilosc

    def ustaw_wiezy(self, indeks, ustalona_pozycja):
        if indeks >= 0 and indeks < self.ilosc:
            self.wiezy[indeks] = ustalona_pozycja


class PunktMaterialny:
    numer_kroku = 0

    def __init__(self, polozenie=Wektor(), predkosc=Wektor(), masa=1.0, promien=1.0, kolor=Kolor()):

        self.polozenie = polozenie
        self.predkosc = predkosc
        self.poprzednie_polozenie = Wektor()
        self.nastepne_polozenie = Wektor()
        self.nastepna_predkosc = Wektor()
        self.masa = masa
        self.promien = promien
        self.kolor = kolor

        self.sphere = sphere(radius=self.promien,
                             pos=[self.polozenie.x, self.polozenie.y, self.polozenie.z],
                             color=[self.kolor.r, self.kolor.g, self.kolor.b])

    # Moze lepiej funkcje rysujace oddzielic od fizyki.
    # Ale jakby co to tak mozna narysowac punkt materialny:
    def aktualizuj_pozycje(self):
        self.sphere.pos = [self.polozenie.x, self.polozenie.y, self.polozenie.z]

    def przygotuj_ruch_euler(self, przyspieszenie=Wektor(), krok_czasowy=0.0):
        self.nastepna_predkosc = self.predkosc + przyspieszenie * krok_czasowy
        self.nastepne_polozenie = self.polozenie + self.nastepna_predkosc * krok_czasowy

    def przygotuj_ruch_verlet(self, przyspieszenie=Wektor(), krok_czasowy=0.0):
        if self.numer_kroku == 0:
            self.przygotuj_ruch_euler(przyspieszenie, krok_czasowy)
        else:
            self.nastepne_polozenie = self.polozenie * 2.0 - self.poprzednie_polozenie + przyspieszenie * krok_czasowy ** 2
            self.nastepna_predkosc = (self.nastepne_polozenie - self.poprzednie_polozenie) / (2.0 * krok_czasowy)

    def przygotuj_ruch(self, sila=Wektor(), krok_czasowy=0.0, algorytm=Algorytm.EULER):

        przyspieszenie = sila / self.masa

        if algorytm == Algorytm.EULER:
            self.przygotuj_ruch_euler()
        elif algorytm == Algorytm.VERLET:
            self.przygotuj_ruch_verlet(przyspieszenie, krok_czasowy)

    def wykonaj_ruch(self):
        self.poprzednie_polozenie = self.polozenie
        self.polozenie = self.nastepne_polozenie
        self.predkosc = self.nastepna_predkosc
        self.numer_kroku += 1

    def ustaw_polozenie(self, polozenie=Wektor()):
        self.polozenie = polozenie

    def ustaw_predkosc(self, predkosc=Wektor()):
        self.predkosc = predkosc

    def ustaw_promien(self, promien=1.0):
        self.promien = promien
        self.sphere.radius = promien

    def ustaw_kolor(self, r=0.0, g=0.0, b=0.0):
        self.kolor.r = r
        self.kolor.g = g
        self.kolor.b = b
        self.sphere.color=[self.kolor.r, self.kolor.g, self.kolor.b]