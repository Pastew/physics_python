from visual import *
import threading

from MyMath import Kolor
from PunktMaterialny import Algorytm, ZbiorPunktowMaterialnych
from UkladyPunktowMaterialnych import Oscylator, OscylatorySprzezone, UsztywnioneOscylatorySprzezone, Lina, \
    LinaOddzialywaniaZDalszymiSasiadami, Wlos, LinaZPodlozem


class MojeOkno(object):
    def __init__(self, zpm=None, rysuj_linie=True, przesun_do_srodka_masy=False):
        self.algorytm = Algorytm.VERLET
        self.poprzedni_czas = 0.0
        self.pauza = False
        self.typ_rzutowania = False
        self.przesun_do_srodka_masy = przesun_do_srodka_masy

        self.fps = 30.0
        self.czas_pomiedzy_dwoma_klatkami = 1.0 / self.fps
        self.biezacy_czas_pomiedzy_dwoma_klatkami = self.czas_pomiedzy_dwoma_klatkami
        self.iteracje_fizyki_na_jedna_klatke = 4
        self.delta_czas = self.czas_pomiedzy_dwoma_klatkami / self.iteracje_fizyki_na_jedna_klatke

        ilosc = 10
        wspolczynnik_sprezystosci = 100
        wspolczynnik_tlumienia = 0.02
        wspolczynnik_tlumienia_oscylacji = 1
        wspolczynnik_sztywnosci = 1
        dlugosc = 2

        self.zpm = zpm
        if zpm is None:
            self.zpm = LinaZPodlozem(ilosc, wspolczynnik_sprezystosci,
                                     wspolczynnik_tlumienia, wspolczynnik_tlumienia_oscylacji,
                                     wspolczynnik_sztywnosci, dlugosc)

        self.rysuj_linie = rysuj_linie
        if self.rysuj_linie:
            self.linie = curve(pos=self.zpm.pobierz_polozenia_kolejnych_punktow(), radius=0.01, color=Kolor(1, 1, 1).rgb())

    def glowna_petla(self):

        biezaca_klatka = 0.0  # Time of the current frame
        nastepna_klatla = biezaca_klatka + self.czas_pomiedzy_dwoma_klatkami  # Time of the next frame
        ostatni_czas = biezaca_klatka  # Time of the last update of the fps counter
        self.rysuj_uklad_wspolrzednych()

        while 1:
            rate(self.fps)
            #sleep(self.czas_pomiedzy_dwoma_klatkami)

            if biezaca_klatka - ostatni_czas > 1.0:
                print str(1 / self.czas_pomiedzy_dwoma_klatkami) + " fps"
                ostatni_czas = biezaca_klatka

            biezaca_klatka += self.czas_pomiedzy_dwoma_klatkami

            iteracja = self.iteracje_fizyki_na_jedna_klatke
            while iteracja != 0:
                self.zpm.krok_naprzod(self.delta_czas, self.algorytm)
                iteracja -= 1

            self.rysuj_aktorow()

    def schowaj_punkty(self):
        for punkt in self.zpm.punkty:
            punkt.sphere.opacity = 0

    def pokaz_punkty(self):
        for punkt in self.zpm.punkty:
            punkt.sphere.opacity = 1

    def rysuj_aktorow(self):
        jednostka_dlugosci = 1.0
        self.rysuj_zpm(self.zpm, jednostka_dlugosci)
        if self.rysuj_linie:
            self.rysuj_zpm_linie(self.zpm, jednostka_dlugosci)

    def rysuj_uklad_wspolrzednych(self):
        sphere(pos=[0, 0, 0], color=[1, 1, 1], radius=0.05)
        arrow_pos = [0, 0, 0]
        arrow_length = 0.4
        arrow(pos=arrow_pos, axis=[arrow_length, 0, 0], color=[1, 0.2, 0.3])
        arrow(pos=arrow_pos, axis=[0, arrow_length, 0], color=[0.2, 1, 0.3])
        arrow(pos=arrow_pos, axis=[0, 0, arrow_length], color=[0.5, 0.5, 1])

    def rysuj_zpm(self, zpm=None, jednostka_dlugosci=1.0):
        if self.przesun_do_srodka_masy:
            srodek_masy = self.zpm.srodek_masy()
            # TODO przekrec kamere tak zeby patrzyla na srodek_masy

        indeks = 0
        while indeks < zpm.liczba_punktow():
            punkt_materialny = zpm.pobierz_punkt_materialny(indeks)

            # Tu jest miejsce na filtrowanie rysowanych punktow

            punkt_materialny.aktualizuj_pozycje()
            # punkt_materialny.sphere.opacity = 0

            indeks += 1

    def rysuj_zpm_linie(self, zpm=ZbiorPunktowMaterialnych(0), jednostka_dlugosci=1.0, grubosc_linii=0.01,
                        kolor=Kolor(1, 1, 1)):
        if self.przesun_do_srodka_masy:
            srodekMasy = jednostka_dlugosci * zpm.srodek_masy()
            # TODO przesun kamere na srodek masy

        self.linie.pos = zpm.pobierz_polozenia_kolejnych_punktow()
