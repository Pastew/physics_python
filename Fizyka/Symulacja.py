from visual import *
import threading

from MyMath import Kolor, Wektor
from PunktMaterialny import Algorytm, ZbiorPunktowMaterialnych
from UkladyPunktowMaterialnych import Oscylator, OscylatorySprzezone, UsztywnioneOscylatorySprzezone, Lina, \
    LinaOddzialywaniaZDalszymiSasiadami, Wlos, LinaZPodlozem


class Symulacja(object):
    def __init__(self, zpms=None, rysuj_linie=True, przesun_do_srodka_masy=False):
        self.algorytm = Algorytm.VERLET
        self.poprzedni_czas = 0.0
        self.pauza = False
        self.typ_rzutowania = False
        self.przesun_do_srodka_masy = przesun_do_srodka_masy

        self.fps = 30.0
        self.czas_pomiedzy_dwoma_klatkami = 1.0 / self.fps
        self.biezacy_czas_pomiedzy_dwoma_klatkami = self.czas_pomiedzy_dwoma_klatkami
        self.iteracje_fizyki_na_jedna_klatke = 2
        self.delta_czas = self.czas_pomiedzy_dwoma_klatkami / self.iteracje_fizyki_na_jedna_klatke

        if isinstance(zpms, ZbiorPunktowMaterialnych):
            # Dostalismy jeden zbior punktow materialnych a nie liste, wiec zrobmy jedno-elementowa liste
            self.zpms = [zpms]

        if isinstance(zpms, list) and isinstance(zpms[0], ZbiorPunktowMaterialnych):
            # Dostalismy liste zbiorow punktow materialnych, wiec jest ok
            self.zpms = zpms

        if zpms is None:
            print("Podaj jakis zpm")
            exit()

        self.rysuj_linie = rysuj_linie
        if self.rysuj_linie:
            self.linie = []
            self.cienie = []
            for zpm in self.zpms:
                self.linie.append(curve(radius=0.01,
                                        color=Kolor(random.random(), random.random(), random.random()).rgb()))

                self.cienie.append(curve(radius=0.02,
                                         color=[0.2, 0.2, 0.2]))

        self.trzymany_punkt = self.zpms[0].pobierz_punkt_materialny(0)

    def obsluz_klawiature(self):
        if scene.kb.keys:
            s = scene.kb.getkey()  # get keyboard info
            zpm = self.zpms[0]
            zmiana_polozenia = 0.1
            if s == 'e':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(0, zmiana_polozenia, 0))
            if s == 'q':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(0, -zmiana_polozenia, 0))
            if s == 'a':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(-zmiana_polozenia, 0, 0))
            if s == 'd':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(zmiana_polozenia, 0, 0))
            if s == 'w':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(0, 0, -zmiana_polozenia))
            if s == 's':
                self.trzymany_punkt.ustaw_polozenie(self.trzymany_punkt.polozenie + Wektor(0, 0, zmiana_polozenia))
            if s == 'm':
                zpm.ustaw_wiezy(0, not zpm.wiezy[0])

            nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            if s in nums:
                print(s)
                zpm.ustaw_wiezy(int(s), not zpm.wiezy[int(s)])
                self.trzymany_punkt = zpm.pobierz_punkt_materialny(int(s))
        pass

    def glowna_petla(self):

        biezaca_klatka = 0.0  # Time of the current frame
        nastepna_klatla = biezaca_klatka + self.czas_pomiedzy_dwoma_klatkami  # Time of the next frame
        ostatni_czas = biezaca_klatka  # Time of the last update of the fps counter
        self.rysuj_uklad_wspolrzednych()

        while 1:
            rate(self.fps)
            # sleep(self.czas_pomiedzy_dwoma_klatkami)
            self.obsluz_klawiature()

            if biezaca_klatka - ostatni_czas > 1.0:
                print str(1 / self.czas_pomiedzy_dwoma_klatkami) + " fps"
                ostatni_czas = biezaca_klatka

            biezaca_klatka += self.czas_pomiedzy_dwoma_klatkami

            iteracja = self.iteracje_fizyki_na_jedna_klatke
            while iteracja != 0:
                for zpm in self.zpms:
                    zpm.krok_naprzod(self.delta_czas, self.algorytm)
                iteracja -= 1

            self.rysuj_aktorow()

    def schowaj_punkty(self):
        for zpm in self.zpms:
            for punkt in zpm.punkty:
                punkt.sphere.opacity = 0

    def pokaz_punkty(self):
        for zpm in self.zpms:
            for punkt in zpm.punkty:
                punkt.sphere.opacity = 1

    def rysuj_aktorow(self):
        jednostka_dlugosci = 1.0
        for i in range(0, len(self.zpms)):
            self.rysuj_zpm(self.zpms[i], jednostka_dlugosci)
            if self.rysuj_linie:
                if isinstance(self.zpms[i], LinaZPodlozem) or hasattr(self.zpms[i], 'poziom_podloza_y'):
                    self.rysuj_zpm_linie(i, self.zpms[i], jednostka_dlugosci,
                                         True, poziom_podloza_y=self.zpms[i].poziom_podloza_y)
                else:
                    self.rysuj_zpm_linie(i, self.zpms[i], jednostka_dlugosci)

    def rysuj_uklad_wspolrzednych(self):
        sphere(pos=[0, 0, 0], color=[1, 1, 1], radius=0.05)
        arrow_pos = [0, 0, 0]
        arrow_length = 0.4
        arrow(pos=arrow_pos, axis=[arrow_length, 0, 0], color=[1, 0.2, 0.3])
        arrow(pos=arrow_pos, axis=[0, arrow_length, 0], color=[0.2, 1, 0.3])
        arrow(pos=arrow_pos, axis=[0, 0, arrow_length], color=[0.5, 0.5, 1])

    def rysuj_zpm(self, zpm=None, jednostka_dlugosci=1.0):
        if self.przesun_do_srodka_masy:
            srodek_masy = zpm.srodek_masy()
            # TODO przekrec kamere tak zeby patrzyla na srodek_masy

        indeks = 0
        while indeks < zpm.liczba_punktow():
            punkt_materialny = zpm.pobierz_punkt_materialny(indeks)

            # Tu jest miejsce na filtrowanie rysowanych punktow

            punkt_materialny.aktualizuj_pozycje()
            # punkt_materialny.sphere.opacity = 0

            indeks += 1

    def rysuj_zpm_linie(self, indeks, zpm=ZbiorPunktowMaterialnych(0),
                        jednostka_dlugosci=1.0,
                        cien=False, poziom_podloza_y=0.0):
        if self.przesun_do_srodka_masy:
            srodekMasy = jednostka_dlugosci * zpm.srodek_masy()
            # TODO przesun kamere na srodek masy

        polozenia = zpm.pobierz_polozenia_kolejnych_punktow_xyz()
        self.linie[indeks].pos = polozenia

        if cien:
            polozenia_cienia = []
            for p in polozenia:
                polozenia_cienia.append([p[0], poziom_podloza_y, p[2]])

            self.cienie[indeks].pos = polozenia_cienia

    def grubosc_linii(self, grubosc):
        for l in self.linie:
            l.radius = grubosc

    def kolor_linii(self, kolor):
        for l in self.linie:
            l.color = kolor
