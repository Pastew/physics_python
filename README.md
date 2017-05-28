## Jak uruchomic
Zainstaluj po kolei:
* http://python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi
* http://sourceforge.net/projects/vpythonwx/files/6.11-release/VPython-Win-64-Py2.7-6.11.exe/download
* https://www.jetbrains.com/pycharm/

## Jak zbudowac samodzielny plik exe:

Zainstaluj:
* http://prdownloads.sourceforge.net/py2exe/py2exe-0.6.9.win64-py2.7.amd64.exe?download

Skopiuj wszystkie pliki .dll z tego repozytorium do C:\Python27\DLLs

Jak zbudowac plik exe:
```
Zmodyfikuj plik setup.py (dopisz nowy przyklad ktory chcesz zbudowac jesli go tam brakuje)
W command line
cd <project_dir>
C:\Python27\python setup.py py2exe
Skopiuj wszystkie pliki tga z folderu tgas z tego repozytorium do folderu dist ktory zostal wlasnie stworzony. 
Tam znajdziesz tez pliki .exe ze zbudowanymi programami.
Mozesz tez odpalic build.bat
```

## Sterowanie (na dzien 23 kwietnia 2017)
* WSAD EQ - poruszanie trzymanym punktem
* M - zablokuj/odblokuj trzymany punkt (nie beda na niego dzialac sily)
* 0-9 - zlap punkt

## Przyklad7
![Przyklad7](/screenshots/przyklad7.PNG)

Tutaj widac ze jest w sumie 20 punktow i dwa sa zablokowane w powietrzu.
![Przyklad7_2](/screenshots/przyklad7_2.PNG)
## Przyklad8
![Przyklad8](/screenshots/przyklad8.PNG)
