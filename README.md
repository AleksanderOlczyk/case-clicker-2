# Case Clicker 2 Automation Tool

Ten projekt to narzędzie automatyzacji dla gry Case Clicker 2, napisane w Pythonie. Używa bibliotek `pyautogui` i `win32api` do symulacji ruchów myszy i kliknięć, a także do wykrywania obiektów na ekranie.

## Funkcje

1. **Automatyczne klikanie**: Narzędzie symuluje kliknięcia myszy z określoną prędkością i losowym przesunięciem, aby naśladować działanie człowieka.
2. **Wykrywanie obiektów**: Narzędzie potrafi wykrywać różne obiekty na ekranie, takie jak boostery i torby z pieniędzmi, i automatycznie kierować kursor do nich.
3. **Płynne ruchy myszy**: Narzędzie symuluje płynne ruchy myszy, zamiast teleportować kursor bezpośrednio do celu. Dodatkowo, ruchy myszy są nieco losowe, aby naśladować naturalne ruchy człowieka.
4. **Wielowątkowość**: Narzędzie korzysta z wielowątkowości do jednoczesnego wykonywania różnych zadań, takich jak klikanie, wykrywanie obiektów i sprawdzanie, czy menu zarabiania jest aktywne.

## Struktura kodu

Projekt składa się z kilku plików:

- `main.py`: Główny plik, który uruchamia wszystkie wątki.
- `clicking.py`: Zawiera funkcje do symulacji kliknięć myszy i ruchów.
- `detection.py`: Zawiera funkcje do wykrywania obiektów na ekranie.
- `SmoothCursor.py`: Zawiera klasę `SmoothCursor`, która symuluje płynne ruchy myszy.
- `constants.py`: Zawiera globalne zmienne używane w całym projekcie.
- `utils.py`: Zawiera pomocnicze funkcje, takie jak sprawdzanie, czy menu zarabiania jest aktywne.

## Jak używać

Uruchom plik `main.py` i pozwól narzędziu automatycznie grać w Case Clicker 2 za Ciebie. Możesz zatrzymać i wznowić narzędzie, naciskając odpowiednie klawisze (domyślnie 'o' i 'p').