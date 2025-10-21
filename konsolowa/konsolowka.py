def szyfruj(tekst, klucz):
    wynik = ""
    klucz = klucz % 26
    for znak in tekst:
        if znak == " ":
            wynik += " "
        elif "a" <= znak <= "z":
            kod = ord(znak) - 97
            kod = (kod + klucz) % 26
            wynik += chr(kod + 97)
        else:
            wynik += znak
    return wynik


def main():
    print("Szyfr Cezara - Filip Pawłowski 5Tp\n")
    tekst = input("Podaj tekst jawny: ")
    try:
        klucz = int(input("Podaj klucz szyfrowania: "))
    except:
        klucz = 0
    print("\nTekst zaszyfrowany:")
    print(szyfruj(tekst, klucz))


if __name__ == "__main__":
    main()
