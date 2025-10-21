# Projekt Szyfrowania - Filip Pawłowski 5Tp

## Opis projektu
Projekt zawiera implementację szyfru Cezara w dwóch wersjach:
- **Aplikacja konsolowa** - prosta wersja tekstowa
- **Aplikacja desktopowa** - interfejs graficzny z wykorzystaniem PyQt6

## Struktura projektu
```
inf04/
├── desktopowa/
│   ├── main.py          # Główny plik aplikacji desktopowej
│   ├── layout.py        # Wygenerowany kod interfejsu
│   └── layout.ui        # Plik UI Qt Designer
├── konsolowa/
│   └── konsolowka.py    # Aplikacja konsolowa
└── README.md           # Ten plik
```

## Wymagania
- Python 3.x
- PyQt6 (dla aplikacji desktopowej)

## Instalacja
```bash
pip install PyQt6
```

## Uruchomienie

### Aplikacja konsolowa
```bash
python konsolowa/konsolowka.py
```

### Aplikacja desktopowa
```bash
python desktopowa/main.py
```

## Funkcjonalności
- Szyfrowanie tekstu szyfrem Cezara
- Możliwość ustawienia klucza szyfrowania
- Zapis zaszyfrowanego tekstu do pliku (aplikacja desktopowa)
- Intuicyjny interfejs graficzny

## Autor
Filip Pawłowski - 5Tp
