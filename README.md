## Jak uruchomic
Zainstaluj po kolei:
http://python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi
http://sourceforge.net/projects/vpythonwx/files/6.11-release/VPython-Win-64-Py2.7-6.11.exe/download
https://www.jetbrains.com/pycharm/

## Jak zbudowac samodzielny plik exe:
Zainstaluj:
http://prdownloads.sourceforge.net/py2exe/py2exe-0.6.9.win64-py2.7.amd64.exe?download
Copy all dll files from DLLs dir of this repo to C:\Python27\DLLs
How co create exe file:
cmd
cd <project_dir>
C:\Python27\python setup.py py2exe (or run build.bat)
(Modify setup.py file before that)
Copy all tga files from tgas dir of this repo to dist directory (where .exe file was generated)

## Sterowanie
* WSAD EQ - poruszanie trzymanym punktem
* M - zablokuj/odblokuj trzymany punkt (nie beda na niego dzialac sily)
* 0-9 - zlap punkt

## Przyklad7
![Przyklad7](/screenshots/przyklad7.PNG)
## Przyklad8
![Przyklad8](/screenshots/przyklad8.PNG)
