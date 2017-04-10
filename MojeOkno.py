from visual import *
import threading

from PunktMaterialny import Algorytm
from UkladyPunktowMaterialnych import Oscylator


class MojeOkno(object):
    def __init__(self, zpm=None, przesun_do_srodka_masy=False):
        self.algorytm = Algorytm.VERLET
        self.poprzedni_czas = 0.0
        self.pauza = False
        self.typ_rzutowania = False

        self.fps = 60.0
        self.czas_pomiedzy_dwoma_klatkami = 1.0 / self.fps
        self.biezacy_czas_pomiedzy_dwoma_klatkami = self.czas_pomiedzy_dwoma_klatkami
        self.iteracje_fizyki_na_jedna_klatke = 16
        self.delta_czas = self.czas_pomiedzy_dwoma_klatkami / self.iteracje_fizyki_na_jedna_klatke

        self.zpm = Oscylator(1)
        self.przesun_do_srodka_masy = przesun_do_srodka_masy

    def glowna_petla(self):

        biezaca_klatka = 0.0  # Time of the current frame
        nastepna_klatla = biezaca_klatka + self.czas_pomiedzy_dwoma_klatkami  # Time of the next frame
        ostatni_czas = biezaca_klatka  # Time of the last update of the fps counter
        self.rysuj_uklad_wspolrzednych()

        while 1:
            # rate(self.fps)
            sleep(self.czas_pomiedzy_dwoma_klatkami)

            if biezaca_klatka - ostatni_czas > 1.0:
                print str(1 / self.czas_pomiedzy_dwoma_klatkami) + " fps"
                ostatni_czas = biezaca_klatka

            iter = self.iteracje_fizyki_na_jedna_klatke
            while iter != 0:
                self.zpm.krok_naprzod(self.delta_czas, self.algorytm)
                iter -= 1

            self.rysuj_aktorow()

    def rysuj_aktorow(self):
        jednostka_dlugosci = 1.0
        self.rysuj_zpm(self.zpm, jednostka_dlugosci)

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

            indeks += 1
