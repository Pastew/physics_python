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

    def przygotuj_ruch(self, krok_czasowy, algorytm=Algorytm.VERLET):
        for i in range(self.ilosc):
            if self.wiezy[i] is False:
                self.punkty[i].przygotuj_ruch(self.sila(i), krok_czasowy, algorytm)

    def wykonaj_ruch(self):
        for i in range(self.ilosc):
            if self.wiezy[i] is False:
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
        for p in self.punkty:
            if p.do_usuniecia:
                del p.sphere
                self.punkty.remove(p)
                self.ilosc -= 1
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
            self.punkty[indeks].ustaw_predkosc(Wektor(0, 0, 0))

    # Zwraca polozenia kolejnych punktow, na przyklad dla 4 elementowego zpm:
    # [[x1,y1,z1],
    #  [x2,y2,z2],
    #  [x3,y3,z3],
    #  [x4,y4,z4]]
    def pobierz_polozenia_kolejnych_punktow_xyz(self):
        polozenia = []
        for i in range(self.ilosc):
            punkt = self.pobierz_punkt_materialny(i)
            polozenie = punkt.polozenie.xyz()
            polozenia.append(polozenie)
        return polozenia

    def przesun_wszystkie_punkty(self, wektor):
        for p in self.punkty:
            p.polozenie += wektor

    def dodaj_punkt(self, punkt):
        self.ilosc += 1
        self.punkty.append(punkt)
        self.wiezy.append(False)

    def usun_punkt_materialny(self, i):
        p = self.pobierz_punkt_materialny(i)
        p.sphere.visible = False
        p.do_usuniecia = True


class ObszarZabroniony(object):
    def __init__(self, wspolczynnik_odbicia=0.3, wspolczynnik_tarcia=0.1):
        self.wspolczynnik_odbicia = wspolczynnik_odbicia
        self.wspolczynnik_tarcia = wspolczynnik_tarcia

    def czy_w_obszarze_zabronionym(self, polozenie, poprzednie_polozenie, margines, normalna):
        return None


class ZbiorPunktowMaterialnychZObszaremZabronionym(ZbiorPunktowMaterialnych):
    def __init__(self, ilosc):
        super(ZbiorPunktowMaterialnychZObszaremZabronionym, self).__init__(ilosc)
        self.obszar_zabroniony = None
        self.zaznacz_kontakt_punktu_z_obszarem_zabronionym = True

    def przygotuj_ruch(self, krok_czasowy, algorytm=Algorytm.VERLET):
        for i in range(self.ilosc):
            if self.wiezy[i] is False:
                self.punkty[i].przygotuj_ruch(self.sila(i), krok_czasowy, algorytm)
                if not self.obszar_zabroniony is None and self.obszar_zabroniony.czy_w_obszarze_zabronionym(
                        self.punkty[i].nastepne_polozenie,
                        self.punkty[i].poprzednie_polozenie,
                        self.punkty[i].promien,
                        None):
                    self.przygotuj_ruch_przy_kontakcie_z_obszarem_zabronionym(i, krok_czasowy)
                    if self.zaznacz_kontakt_punktu_z_obszarem_zabronionym:
                        self.punkty[i].ustaw_kolor(1, 0, 0)

                else:
                    if self.zaznacz_kontakt_punktu_z_obszarem_zabronionym:
                        self.punkty[i].ustaw_kolor(0, 1, 0)

    def przygotuj_ruch_przy_kontakcie_z_obszarem_zabronionym(self, indeks, krok_czasowy):
        if self.obszar_zabroniony is None:
            return

        punkt = self.pobierz_punkt_materialny(indeks)
        normalna = Wektor()

        # Zakladamy, ze nastepne polozenie jest juz obliczone
        w_obszarze_zabronionym, normalna = self.obszar_zabroniony.czy_w_obszarze_zabronionym(
            punkt.nastepne_polozenie,
            punkt.polozenie,
            punkt.promien,
            normalna)

        if w_obszarze_zabronionym:
            # Eliminacja skladowej normalnej sily
            sila = self.sila(indeks)
            skladowa_normalna_sily = normalna * sila
            if skladowa_normalna_sily < 0:  # usuwanie skladowej sily skierowanej do powierzchni
                sila -= normalna * skladowa_normalna_sily  # dzialanie sily kontaktowej

            # uwzglednienie odbicia (zmiana aktualnego wektora predkosci)
            predkosc = punkt.predkosc
            skladowa_normalna_predkosci = normalna * predkosc
            if skladowa_normalna_predkosci < 0:  # usuwanie skladowej predkosci skierowanej do powierzchni
                predkosc -= normalna * ((self.obszar_zabroniony.wspolczynnik_odbicia + 1) * skladowa_normalna_predkosci)

            punkt.ustaw_predkosc(predkosc)

            #tarcie
            if skladowa_normalna_sily < 0 and predkosc.dlugosc() > 0:
                tarcie = predkosc * -1
                tarcie.normuj()
                tarcie *= math.fabs(self.obszar_zabroniony.wspolczynnik_tarcia * skladowa_normalna_sily)
                sila += tarcie

            # ponowne przygotowanie ruchu z nowymi sila i predkoscia
            # musi byc metoda Eulera, bo ta widzi zmiane predkosci
            punkt.przygotuj_ruch(sila, krok_czasowy, algorytm=Algorytm.EULER)


class PunktMaterialny:
    numer_kroku = 0

    def __init__(self, polozenie=Wektor(), predkosc=Wektor(), masa=1.0, promien=0.1, kolor=Kolor()):

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
                             color=[self.kolor.r, self.kolor.g, self.kolor.b]
                             )

        self.do_usuniecia = False
        # self.sphere = sphere(radius=self.promien,
        #                      pos=[self.polozenie.x, self.polozenie.y, self.polozenie.z],
        #                      color=[self.kolor.r, self.kolor.g, self.kolor.b],
        #                      make_trail=True, trail_type="curve",
        #                      interval=1, retain=500
        #                      )

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
            self.przygotuj_ruch_euler(przyspieszenie, krok_czasowy)
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
        self.promien = float(promien)
        self.sphere.radius = self.promien

    def ustaw_kolor(self, r=0.0, g=0.0, b=0.0):
        self.kolor.r = float(r)
        self.kolor.g = float(g)
        self.kolor.b = float(b)
        self.sphere.color = [self.kolor.r, self.kolor.g, self.kolor.b]
