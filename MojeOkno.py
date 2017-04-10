from visual import *
import threading

from PunktMaterialny import Algorytm
from UkladyPunktowMaterialnych import Oscylator


class MojeOkno(object):
    def __init__(self, zpm=None, przesun_do_srodka_masy=False):
        self.algorytm = Algorytm.VERLET
        self.krok_czasowy = 0.001
        self.ilosc_krokow_w_serii = 100
        self.poprzedni_czas = 0.0
        self.pauza = False
        self.typ_rzutowania = False

        self.zpm = Oscylator(1)
        self.przesun_do_srodka_masy = przesun_do_srodka_masy

        self.timer_rysowania_tick()
        self.timer_obliczen_tick()

    def rysuj_aktorow(self):
        jednostka_dlugosci = 1.0
        self.rysuj_uklad_wspolrzednych()
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
            polozenie_punktu = punkt_materialny.polozenie
            kolor_punktu = punkt_materialny.kolor

            print "pos:    " + str(punkt_materialny.polozenie)
            #print "radius: " + str(punkt_materialny.promien)

            # Tu jest miejsce na filtrowanie rysowanych punktow
            sphere(pos=[polozenie_punktu.x, polozenie_punktu.y, polozenie_punktu.z],
                   radius=punkt_materialny.promien,
                   color=[kolor_punktu.r, kolor_punktu.g, kolor_punktu.b])

            indeks += 1

    def timer_obliczen_tick(self):
        i = 0
        while i < self.ilosc_krokow_w_serii:
            self.zpm.krok_naprzod(self.krok_czasowy, self.algorytm)
            i += 1

        #print ("Timer obliczen")
        threading.Timer(0.01, self.timer_obliczen_tick).start()

    def timer_rysowania_tick(self):
        self.rysuj_aktorow()
        #print ("Timer rysowania")
        threading.Timer(1.0/30.0, self.timer_rysowania_tick).start()



