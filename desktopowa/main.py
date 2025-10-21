import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from layout import Ui_Dialog


class SzyfrCezara:
    @staticmethod
    def szyfruj(tekst, klucz):
        klucz %= 26
        wynik = ""
        for znak in tekst:
            if "a" <= znak <= "z":
                kod = ord(znak) + klucz
                if kod > ord("z"):
                    kod -= 26
                wynik += chr(kod)
            else:
                wynik += znak
        return wynik


class Okno(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnDodaj.clicked.connect(self.szyfruj_tekst)
        self.ui.btnZapisz.clicked.connect(self.zapisz_do_pliku)

    def szyfruj_tekst(self):
        tekst = self.ui.txtTekst.toPlainText()
        klucz = int(self.ui.txtKlucz.toPlainText() or 0)
        self.ui.lblZaszyfrowany.setText(SzyfrCezara.szyfruj(tekst, klucz))

    def zapisz_do_pliku(self):
        zaszyfrowany = self.ui.lblZaszyfrowany.text()
        if zaszyfrowany:
            nazwa_pliku, _ = QFileDialog.getSaveFileName(
                self, "Zapisz szyfr w pliku", "", "Pliki tekstowe (*.txt)"
            )
            if nazwa_pliku:
                with open(nazwa_pliku, "w", encoding="utf-8") as plik:
                    plik.write(zaszyfrowany)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Okno()
    window.show()
    sys.exit(app.exec())
