from distutils.core import setup
import py2exe

setup(
    console=["Przyklad.py",
             "Przyklad1_Oscylator.py",
             "Przyklad1_Oscylatory.py",
             "Przyklad2_OscylatorySprzezone.py",
             "Przyklad3_UsztywnioneOscylatorySprzezone.py",
             "Przyklad4_Lina.py",
             "Przyklad5_LinaOddzialywaniaZDalszymi.py",
             "Przyklad6_Wlos.py",
             "Przyklad7_LinaZPodlozem.py",
             "Przyklad8_KilkaZPM.py"
             ],
)
