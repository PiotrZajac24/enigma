class InvalidTextError(Exception):
    """
    Sygnalizuje, że w danym tekście znajdują się znaki, które nie są dozwolone.
    """
    def __init__(self, message="Tekst zawiera niewłaściwe znaki."):
        self.message = message

    def __str__(self):
        return self.message


class InvalidOrderError(Exception):
    """
    Sygnalizuje, że podana kolejność wirników jest nieprawidłowa.
    """

    def __init__(self, message="Podana kolejność zawiera nieokreślone wirniki."):
        self.message = message

    def __str__(self):
        return self.message


class InvalidCodeError(Exception):
    """
    Sygnalizuje, że w danym kodzie są nieprawidłowe znaki.
    """
    def __init__(self, message="Podany kod zawiera nieprawidłowe znaki."):
        self.message = message

    def __str__(self):
        return self.message


class EnigmaRotorDataError(Exception):

    def __init__(self, data, message="Plik z ustawieniami nie zawiera informacji o wszystkich wirnikach."):
        self.message = message
        self.data = data

    def __str__(self):
        return self.message.format(self.data)


class PositionError(Exception):
    """
    """

    def __init__(self, message="Podana pozycja wirnika jest nieprawidłowa."):
        self.message = message

    def __str__(self):
        return self.message


class NoCodeError(Exception):
    """
    Sygnalizuje, że nie został podany kod, według którego ustawione są wirniki.
    """
    def __init__(self, message="Nie podano kodu."):
        self.message = message

    def __str__(self):
        return self.message


class CodeTypeError(Exception):
    """
    Sygnalizuje, że podany kod ma niepoprawny typ.
    """

    def __init__(self, message="Podany kod jest niewłaściwy."):
        self.message = message

    def __str__(self):
        return self.message


class CodeLengthError(Exception):
    """
    Sygnalizuje, że podany kod, ma nieprawidłową długość (różną od liczby użytych wirników).
    """

    def __init__(self, message="Podany kod posiada nieprawidłową długość."):
        self.message = message

    def __str__(self):
        return self.message


class CodeKeysError(Exception):
    """
    Sygnalizuje, że podany kod, zawiera nieprawidłowe znaki.
    """
    def __init__(self, message="Podany kod posiada nieprawidłowe znaki."):
        self.message = message

    def __str__(self):
        return self.message


class NoOrderError(Exception):
    """
    Sygnalizuje, że nie została podana kolejność wirników.
    """
    def __init__(self, message="Nie podano kolejności wirników."):
        self.message = message

    def __str__(self):
        return self.message


class OrderRepeatedKeysError(Exception):
    """
    Sygnalizuje, że w kolejności są powtórzone numery wirników.
    """

    def __init__(self, message="Podana kolejność zawiera powtórzone wirniki."):
        self.message = message

    def __str__(self):
        return self.message


class OrderLengthError(Exception):
    """
    Sygnalizuje, że kolejność wirników ma nieprawidłową długość.
    """

    def __init__(self, message="Podana kolejność wirników ma nieprawidłową długość."):
        self.message = message

    def __str__(self):
        return self.message


class OrderKeysError(Exception):
    """
    Sygnalizuje, że kolejność zawiera nieprawidłowe numery wirników.
    """

    def __init__(self, message="Podana kolejność wirników zawiera niewłaściwe znaki."):
        self.message = message

    def __str__(self):
        return self.message


class OrderAndCodeLengthError(Exception):
    """
    Sygnalizuje, że kolejność wirników i kod mają różną długość.
    """

    def __init__(self, message="Długość kolejności wirników i kodu się różnią."):
        self.message = message

    def __str__(self):
        return self.message


class LetterOrderKeysError(Exception):
    """
    Sygnalizuje, że kolejność liter zawiera nieprawidłowe znaki.
    """

    def __init__(self, message="Kolejność liter zawiera nieprawidłowe znaki."):
        self.message = message

    def __str__(self):
        return self.message


class NoLetterOrderError(Exception):
    """
    Sygnalizuje, że nie podano kolejności liter.
    """

    def __init__(self, message="Nie podano kolejności liter."):
        self.message = message

    def __str__(self):
        return self.message


class LetterOrderLengthError(Exception):
    """
    Sygnalizuje, że kolejność liter ma nieprawidłową długość.
    """

    def __init__(self, message="Kolejnosć liter ma nieprawidłową długość."):
        self.message = message

    def __str__(self):
        return self.message


class RepeatedLettersError(Exception):
    """
    Sygnalizuje, że podany ciąg zawiera powtórzone litery.
    """

    def __init__(self, message="Podana kolejność liter zawiera powtórzone znaki."):
        self.message = message

    def __str__(self):
        return self.message


class NumberOfLinksError(Exception):
    pass


class AdditionalRotationError(Exception):
    """
    Sygnalizuje, nie została podana litera z alfabetu.
    """

    def __init__(self, message="Nieprawidłowy znak dla dodatkowego obrotu wirnika."):
        self.message = message

    def __str__(self):
        return self.message


class LinkPairsError(Exception):
    """
    Sygnalizuje, że podane połączenia liter nie są parami różnych liter.
    """

    def __init__(self, message="Podane połączenia powinny być parami różnych liter."):
        self.message = message

    def __str__(self):
        return self.message


class LinkKeysError(Exception):
    """
    Sygnalizuje, że w podanych połączeniach znajduja się nieprawidłowe znaki.
    """

    def __init__(self, message="Podane połączenia zawierają nieprawidłowe znaki."):
        # self.which = which
        self.message = message

    def __str__(self):
        return self.message


class LinksRepeatedKeysError(Exception):
    """
    Sygnalizuje, że w podanych połączeniach znajduja się powtórzone znaki.
    """

    def __init__(self, message="W podanych parach, litery powtarzają się."):
        self.message = message

    def __str__(self):
        return self.message


class ReverseLinksError(Exception):
    """
    Sygnalizuje, że na wirniku odwracającym jest za mało połączeń.
    """

    def __init__(self, message="Nie podano wystarczająco dużo par liter dla wirnika odwracającego."):
        self.message = message

    def __str__(self):
        return self.message


class KeyLetterError(Exception):
    """
    Sygnalizuje, że podany znak nie może zostać zaszyfrowany.
    """

    def __init__(self, message="Podany znak nie jest literą."):
        self.message = message

    def __str__(self):
        return self.message


class NumberOfRotorsError(Exception):
    """
    Sygnalizuje, że podano nieprawidłową ilość wirników.
    """

    def __init__(self, message="Powinien być co najmniej jeden wirnik."):
        self.message = message

    def __str__(self):
        return self.message


class SettingsPathNotFoundError(Exception):
    pass


class SettingsPathPermissionError(Exception):
    pass


class SettingsPathIsdirectoryError(Exception):
    pass


class PathExtensionError(Exception):
    """
    Sygnalizuje, że nie można wczytać pliku z ustawieniami, jeśli nie jest to plik z rozszerzeniem .json.
    """

    def __init__(self, extension):
        super().__init__()
        self.extension = extension

    def __str__(self):
        return f"Nie można wczytać ustawień z pliku z rozszerzeniem .{self.extension}. " \
               f"Dostepne rozszerzenie pliku to .json"


class JsonTextError(Exception):
    """
    Sygnalizuje, że w pliku .json nie ma tekstu do wczytania.
    """

    def __init__(self, message="W wybranym pliku .json nie ma tekstu do wczytania."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class EmptyTextError(Exception):
    """
    Sygnalizuje, że wczytany tekst jest pusty.
    """

    def __init__(self, message="Tekst jest pusty."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class DataError(Exception):
    """
    Sygnalizuje, że nie można zapisać ustawień i tekstu do pliku, ponieważ wymagane pola nie są wypełnione.
    """

    def __init__(self, message="Nie podano wystarczjąco danych."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class EnigmaSettingsError(Exception):
    """
    Sygnalizuje, że maszyna Enigma nie została skonfigurowana i nie można zaszyfrować/odszyfrować tekstu.
    """
    def __init__(self, message="Maszyna nie jest jeszcze skonfigurowana."):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message
