from random import random

from PunktMaterialny import ZbiorPunktowMaterialnych, PunktMaterialny, ObszarZabroniony, \
    ZbiorPunktowMaterialnychZObszaremZabronionym
from visual import *

from Fizyka.MyMath import Wektor
from Fizyka.MyMath import WersoryKierunkowe


class Iskry(ZbiorPunktowMaterialnych):
    def __init__(self):
        super(Iskry, self).__init__(1)

        self.WYMAGANY_CZAS = 1 / 30.0
        self.czas_do_stworzenia_nowej_iskry = self.WYMAGANY_CZAS  # raz na sekunde

        iskra = self.pobierz_punkt_materialny(0)
        iskra.ustaw_promien(0.05)
        iskra.ustaw_kolor(0.9, 0.3, 0.1)
        iskra.ustaw_polozenie(Wektor(0, 0, 0))
        iskra.wiek = 0
        iskra.czas_zycia = 0.001
        iskra.sphere.visible = False
        iskra.temperatura = random.random() * 600 + 400
        iskra.ustaw_predkosc(Wektor(random.random() * 0.4 - 0.2, 0.4, random.random() * 0.4 - 0.2))

    def po_kroku_naprzod(self, krok_czasowy):
        self.czas_do_stworzenia_nowej_iskry -= krok_czasowy

        for i in range(0, self.ilosc):
            p = self.pobierz_punkt_materialny(i)
            p.wiek += krok_czasowy
            if p.wiek > p.czas_zycia:
                self.usun_punkt_materialny(i)
            else:
                p.temperatura -= random.random() * 10
                # p.sphere.opacity = p.temperatura / 800.0
                p.ustaw_kolor(p.temperatura / 1000.0, 0.1, 1.0 - p.temperatura / 800.0)

        if self.czas_do_stworzenia_nowej_iskry < 0:
            self.czas_do_stworzenia_nowej_iskry = self.WYMAGANY_CZAS
            self.stworz_nowa_iskre()

        super(Iskry, self).po_kroku_naprzod(krok_czasowy)

    def sila(self, i):
        p = self.pobierz_punkt_materialny(i)
        predkosc_przeplywu = Wektor(0, 0.9, 0)
        lepkosc = 3.9
        r = p.promien
        return (p.predkosc - predkosc_przeplywu) * (6 * 3.14 * lepkosc * r * -1.0)

    def stworz_nowa_iskre(self):
        iskra = PunktMaterialny()
        iskra.ustaw_promien(0.01)
        iskra.ustaw_kolor(0.9, 0.1, 0.1)
        iskra.ustaw_polozenie(Wektor(0, 0, 0))
        iskra.wiek = 0
        iskra.czas_zycia = random.random() * 3 + 1
        iskra.temperatura = random.random() * 600 + 400

        max_polozenie_na_boki = 0.3
        iskra.ustaw_polozenie(Wektor(random.random() * max_polozenie_na_boki - max_polozenie_na_boki / 2.0,
                                     0,
                                     random.random() * max_polozenie_na_boki - max_polozenie_na_boki / 2.0))
        max_predkosc_na_boki = 0.6
        iskra.ustaw_predkosc(Wektor(random.random() * max_predkosc_na_boki - max_predkosc_na_boki / 2.0,
                                    0.0,
                                    random.random() * max_predkosc_na_boki - max_predkosc_na_boki / 2.0))
        self.dodaj_punkt(iskra)
        return iskra


class KrzywaLissajous(ZbiorPunktowMaterialnych):
    def __init__(self, k1=4, k2=9.0, punkt_poczatkowy=Wektor(-1, -1, 0)):
        self.k1 = k1
        self.k2 = k2
        super(KrzywaLissajous, self).__init__(1)

        punkt = self.pobierz_punkt_materialny(0)
        punkt.ustaw_promien(0.1)
        punkt.ustaw_polozenie(punkt_poczatkowy)
        # punkt.ustaw_predkosc(Wektor(1, 2, 0))
        punkt.ustaw_kolor(0, 0.5, 1)
        punkt.ustaw_promien(random.random() * 0.3)

        punkt.sphere.visible = False
        punkt.promien = 0.1
        punkt.sphere = sphere(radius=punkt.promien,
                              pos=[punkt.polozenie.x, punkt.polozenie.y, punkt.polozenie.z],
                              color=[punkt.kolor.r, punkt.kolor.g, punkt.kolor.b],
                              make_trail=True, trail_type="curve",
                              interval=1, retain=500
                              )

    def sila(self, i):
        return Wektor(self.pobierz_punkt_materialny(0).polozenie.x * -self.k1,
                      self.pobierz_punkt_materialny(0).polozenie.y * -self.k2,
                      0)


class Oscylator(ZbiorPunktowMaterialnych):
    def __init__(self, k=1.0):
        self.k = k
        super(Oscylator, self).__init__(1)

        punkt = self.pobierz_punkt_materialny(0)
        punkt.ustaw_polozenie(Wektor(-1, 0.5, 0))
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


class OscylatorySprzezone(ZbiorPunktowMaterialnychZObszaremZabronionym):
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
        self.sprezystoscTylkoPrzyRozciaganiu = True
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


class Podloze(ObszarZabroniony):
    def __init__(self, wspolczynnik_odbicia=0.2, wspolczynnik_tarcia=0.1, poziom_y=0.0):
        super(Podloze, self).__init__(wspolczynnik_odbicia, wspolczynnik_tarcia)
        self.poziom_y = poziom_y

    def czy_w_obszarze_zabronionym(self, polozenie, poprzednie_polozenie, margines, normalna):
        wynik = (polozenie.y + margines < self.poziom_y)

        if not normalna == None:
            normalna = Wektor(0, 1, 0)
            return wynik, normalna

        return wynik


class Kula(ObszarZabroniony):
    def __init__(self, wspolczynnik_odbicia, wspolczynnik_tarcia, srodek=Wektor(), promien=0.1):
        super(Kula, self).__init__(wspolczynnik_odbicia, wspolczynnik_tarcia)
        self.srodek = srodek
        self.promien = promien

    def czy_w_obszarze_zabronionym(self, polozenie, poprzednie_polozenie, margines, normalna):
        wektor_promienia = polozenie - self.srodek
        wynik = wektor_promienia.dlugosc() < self.promien + margines
        if wynik and normalna is not None:
            normalna = wektor_promienia
            normalna.normuj()
            return wynik, normalna

        return wynik


class WalecNieograniczonyWKierunkuZ(ObszarZabroniony):
    def __init__(self, wspolczynnik_odbicia, wspolczynnik_tarcia, srodek=Wektor(), promien=0.1):
        super(WalecNieograniczonyWKierunkuZ, self).__init__(wspolczynnik_odbicia, wspolczynnik_tarcia)
        self.srodek = srodek
        self.promien = promien

    def czy_w_obszarze_zabronionym(self, polozenie, poprzednie_polozenie, margines, normalna):
        wektor_promienia = polozenie - self.srodek
        wektor_promienia.z = 0
        wynik = wektor_promienia.dlugosc() < self.promien + margines
        if wynik and normalna is not None:
            normalna = wektor_promienia
            normalna.normuj()
            return wynik, normalna

        return wynik


class ProstopadloscianNieograniczonyWKierunkuZ(ObszarZabroniony):
    def __init__(self, wspolczynnik_odbicia, wspolczynnik_tarcia, minX, maxX, minY, maxY):
        super(ProstopadloscianNieograniczonyWKierunkuZ, self).__init__(wspolczynnik_odbicia, wspolczynnik_tarcia)
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

    def pobierz_rozmiar(self):
        return Wektor(self.maxX - self.minX, self.maxY - self.minY, 0)

    def pobierz_srodek(self):
        return Wektor((self.maxX + self.minX) / 2, (self.maxY + self.minY) / 2, 0)

    def czy_w_obszarze_zabronionym(self, polozenie, poprzednie_polozenie, margines, normalna):
        _minX = self.minX - margines
        _maxX = self.maxX + margines
        _minY = self.minY - margines
        _maxY = self.maxY + margines

        wynik = _minX < polozenie.x < _maxX and _minY < polozenie.y < _maxY

        if wynik and (not normalna is None):

            przemieszczenie = polozenie - poprzednie_polozenie
            if przemieszczenie.x != 0:
                normalna = Wektor(0, 0, 0)

                # prosta y=ax + b
                a = przemieszczenie.y / przemieszczenie.x
                b = polozenie.y - a * polozenie.x
                # przeciecie z lewa krawedzia
                y_minX = a * _minX + b
                if _minY <= y_minX < _maxY and poprzednie_polozenie.x < _minX:
                    normalna.x = -1

                # przeciecie z prawa krawedzia
                y_maxX = a * _maxX + b
                if _minY <= y_maxX <= _maxY and poprzednie_polozenie.x > _maxX:
                    normalna.x = 1

                # przeciecie z gorna krawedzia
                x_maxY = (_maxY - b) / a
                if _minX <= x_maxY <= _maxX and poprzednie_polozenie.y > _maxY:
                    normalna.y = 1

                # przeciecie z dolna krawedzia
                x_minY = (_minY - b) / a
                if _minX <= x_minY <= _maxX and poprzednie_polozenie.y < _minY:
                    normalna.y = -1
            else:
                if przemieszczenie.y > 0:
                    normalna = Wektor(0, -1, 0)
                else:
                    normalna = Wektor(0, 1, 0)

            return wynik, normalna

        return wynik


class PunktyUderzajaceWKule(ZbiorPunktowMaterialnychZObszaremZabronionym):
    def __init__(self, ilosc):
        super(PunktyUderzajaceWKule, self).__init__(ilosc)
        self.polozenie_x_min = -0.74
        self.polozenie_x_max = 0.74
        self.polozenie_y_min = 1.74
        self.polozenie_y_max = 2.74
        self.polozenie_z_min = -0.74
        self.polozenie_z_max = 0.74
        self.predkosc_x_min = 1.2
        self.predkosc_x_max = 2.4

        wspolczynnik_odbicia = 0.1
        wspolczynnik_tarcia = 0.2
        srodek = Wektor(2.5, 0, 0)
        promien = 1.0
        self.obszar_zabroniony = Kula(wspolczynnik_odbicia, wspolczynnik_tarcia, srodek, promien)

        for i in range(0, ilosc):
            polozenie_x = random.random() * (self.polozenie_x_max - self.polozenie_x_min) + self.polozenie_x_min
            polozenie_y = random.random() * (self.polozenie_y_max - self.polozenie_y_min) + self.polozenie_y_min
            polozenie_z = random.random() * (self.polozenie_z_max - self.polozenie_z_min) + self.polozenie_z_min
            predkosc_x = random.random() * (self.predkosc_x_max - self.predkosc_x_min) + self.predkosc_x_min
            punkt = self.pobierz_punkt_materialny(i)
            punkt.ustaw_polozenie(Wektor(polozenie_x, polozenie_y, polozenie_z))
            punkt.ustaw_predkosc(Wektor(predkosc_x, 0, 0))

    def sila(self, indeks):
        return Wektor(0, -1.81, 0)


class LinaZPodlozem2(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc,
                 poziom_podloza_y=-1.0):
        super(LinaZPodlozem2, self).__init__(ilosc,
                                             wspolczynnik_sprezystosci,
                                             wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                                             wspolczynnik_sztywnosci,
                                             dlugosc)

        self.obszar_zabroniony = Podloze(0.1, 0.1, poziom_podloza_y)


class LinaZProstopadloscianemNieograniczonymWKierunkuZ(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc):
        super(LinaZProstopadloscianemNieograniczonymWKierunkuZ, self).__init__(ilosc,
                                                                               wspolczynnik_sprezystosci,
                                                                               wspolczynnik_tlumienia,
                                                                               wpolczynnik_tlumienia_oscylacji,
                                                                               wspolczynnik_sztywnosci,
                                                                               dlugosc)

        self.obszar_zabroniony = ProstopadloscianNieograniczonyWKierunkuZ(0, 0, -1, 1, -3.75, -0.25)
        self.ustaw_wiezy(0, false)


class LinaZWalcemNieograniczonymWKierunkuZ(Lina):
    def __init__(self, ilosc,
                 wspolczynnik_sprezystosci,
                 wspolczynnik_tlumienia, wpolczynnik_tlumienia_oscylacji,
                 wspolczynnik_sztywnosci,
                 dlugosc):
        super(LinaZWalcemNieograniczonymWKierunkuZ, self).__init__(ilosc,
                                                                   wspolczynnik_sprezystosci,
                                                                   wspolczynnik_tlumienia,
                                                                   wpolczynnik_tlumienia_oscylacji,
                                                                   wspolczynnik_sztywnosci,
                                                                   dlugosc)

        wspolczynnik_tarcia = 0.1
        wspolczynnik_odbicia = 0.1
        srodek_walca = Wektor(0.1, -3, -3)
        promien = 1.0
        self.obszar_zabroniony = WalecNieograniczonyWKierunkuZ(wspolczynnik_tarcia, wspolczynnik_odbicia,
                                                               srodek_walca, promien)
        self.ustaw_wiezy(0, false)


wersory_kierunkowe_2D = WersoryKierunkowe.wersory_kierunkowe_2D


class Siatka(ZbiorPunktowMaterialnychZObszaremZabronionym):
    def __init__(self,
                 nx, ny,
                 wspolczynnik_sprezystosci, wspolczynnik_tlumienia,
                 wspolczynnik_tlumienia_oscylacji, wspolczynnik_sztywnosci,
                 przyspieszenie_ziemskie,
                 dlugosc_x, dlugosc_y,
                 obszar_zabroniony=None):

        super(Siatka, self).__init__(nx * ny)
        self.co_ktory_sasiad = 1  # 1 - takze po przekatnych (8)
        # 2- tylko na siatce pion poziom(4)

        self.nx = nx
        self.ny = ny
        self.k = wspolczynnik_sprezystosci
        self.t = wspolczynnik_tlumienia
        self.tt = wspolczynnik_tlumienia_oscylacji
        self.s = wspolczynnik_sztywnosci
        self.lx = float(dlugosc_x) / (nx - 1)
        self.ly = float(dlugosc_y) / (ny - 1)
        self.g = przyspieszenie_ziemskie
        self.obszar_zabroniony = obszar_zabroniony
        self.sily_sztywnosci = []

        self.sprezystosc_tylko_przy_rozciaganiu = True

        for ix in range(0, nx):
            for iy in range(0, ny):
                i = ix + nx * iy
                self.sily_sztywnosci.append(Wektor(0, 0, 0))
                punkt = self.pobierz_punkt_materialny(i)
                punkt.ustaw_polozenie(Wektor(-dlugosc_x / 2 + ix * self.lx, -dlugosc_y / 2 + iy * self.ly, 0))
                punkt.ustaw_predkosc(Wektor(0, 0, 0))
                punkt.ustaw_kolor(1, ix / (nx - 1), iy / (ny - 1))

        self.zeruj_predkosc_srednia()

    def przed_krokiem_naprzod(self, krok_czasowy):
        super(Siatka, self).przed_krokiem_naprzod(krok_czasowy)
        for i in range(0, self.liczba_punktow()):
            self.sily_sztywnosci[i] = Wektor(0, 0, 0)

        if self.s == 0:
            return

        for ix in range(1, self.nx - 1):
            for iy in range(1, self.ny - 1):
                indeks = ix + self.nx * iy
                wektor_wypadkowy_sasiadow = Wektor(0, 0, 0)

                kierunek = 0
                while kierunek < 8:
                    nx_sasiada = ix + wersory_kierunkowe_2D[kierunek].x
                    ny_sasiada = iy + wersory_kierunkowe_2D[kierunek].y

                    if 0 <= nx_sasiada < self.nx and 0 <= ny_sasiada < self.ny:
                        do_sasiada = self.pobierz_punkt_materialny(
                            indeks + wersory_kierunkowe_2D[kierunek].x
                            + self.nx * wersory_kierunkowe_2D[kierunek].y).polozenie \
                                     - self.pobierz_punkt_materialny(indeks).polozenie
                        wektor_wypadkowy_sasiadow += do_sasiada

                    kierunek += self.co_ktory_sasiad

                wektor_wypadkowy_sasiadow /= (8.0 / self.co_ktory_sasiad)
                sila_sztywnosci = wektor_wypadkowy_sasiadow * self.s

                self.sily_sztywnosci[indeks] += sila_sztywnosci

                kierunek = 0
                while kierunek < 8:
                    self.sily_sztywnosci[indeks + wersory_kierunkowe_2D[kierunek].x
                                         + self.nx * wersory_kierunkowe_2D[kierunek].y] \
                        -= sila_sztywnosci / (8.0 / self.co_ktory_sasiad)

                    kierunek += self.co_ktory_sasiad

    def sila(self, indeks):
        Nx = self.nx
        Ny = self.nx
        nx = indeks % Nx
        ny = (indeks - nx) / Nx

        sila = Wektor(0, 0, 0)
        kierunek = 0
        while kierunek < 8:
            nx_sasiada = nx + WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].x
            ny_sasiada = ny + WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].y

            if 0 <= nx_sasiada < Nx and 0 <= ny_sasiada < Ny:
                doSasiada = self.pobierz_punkt_materialny(
                    indeks + WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].x + Nx
                    * WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].y).polozenie \
                            - self.pobierz_punkt_materialny(indeks).polozenie

                odlegloscSpoczynkowa = sqrt((WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].x * self.lx) ** 2
                                            + (WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].y * self.ly) ** 2)

                wychylenie = doSasiada.dlugosc() - odlegloscSpoczynkowa

                if not self.sprezystosc_tylko_przy_rozciaganiu or wychylenie > 0:
                    doSasiada.normuj()
                    sila += doSasiada * (self.k * wychylenie)

                    roznica_predkosci = self.pobierz_punkt_materialny(
                        indeks + WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].x + Nx
                        * WersoryKierunkowe.wersory_kierunkowe_2D[kierunek].y).predkosc \
                                        - self.pobierz_punkt_materialny(indeks).predkosc

                    sila += doSasiada * (doSasiada * roznica_predkosci) * self.tt
            kierunek += self.co_ktory_sasiad

        if self.t != 0:
            sila -= self.pobierz_punkt_materialny(indeks).predkosc * self.t  # tlumienie

        if self.s != 0:
            sila += self.sily_sztywnosci[indeks]

        sila += self.g * self.pobierz_punkt_materialny(indeks).masa

        return sila
