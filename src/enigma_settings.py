from random import sample, choice
from src.enigma_exceptions import *


LETTERS = {index: letter for index, letter in enumerate([chr(i) for i in range(65, 91)])}


class Settings:
    """
    Klasa przechowująca ustawienia maszyny. Pozwala odwołać się do wirnika wejściowego, odwracającego oraz połączonych
    wirników. Główną funkcją jest szyfrowanie tekstu.
    """

    def __init__(self, connected_rotors, static_rotor, reverse_rotor):
        self._connected_rotors = connected_rotors
        self._entrance_rotor = static_rotor
        self._reverse_rotor = reverse_rotor

    def number_of_rotors(self):
        """
        Zwraca ilość wirników.
        """
        return len(self.connected_rotors())

    def connected_rotors(self):
        """
        Pozwala odwołać się do połączonych wirników.

        :return: połączne wirniki
        :rtype: ConnectedRotors
        """
        return self._connected_rotors

    def entrance_rotor(self):
        """
        Pozwala odwołać się do wirnika wejściowego.

        :return: wirnik wejściowy
        :rtype: StaticRotor
        """
        return self._entrance_rotor

    def reverse_rotor(self):
        """
        Pozwala odwołać się do wirnika odwracającego.

        :return: wirnik odwracający
        :rtype: ReverseRotor
        """
        return self._reverse_rotor

    def initial_code(self):
        """
        Pozwala odwołać do początkowego kodu według, którego ustawione są wirniki.

        :return: kod początkowy
        :rtype: str
        """
        return self.connected_rotors().initial_code()

    def current_code(self):
        """
        Pozwala odwołać do aktualnego kodu według, któ©ego ustawione są wirniki.

        :return: kod początkowy
        :rtype: str
        """
        return self.connected_rotors().current_code()

    def order(self):
        """
        Zwraca aktualną kolejność wirników.

        :return: kolejność wirników
        :rtype: str
        """
        order = ""
        for key in self.connected_rotors().order():
            order += key + " "
        return order.rstrip()

    def encrypt_text(self, text, reset=True):
        """
        Szyfruje dany teskt, według ustawień maszyny. Pozwala określić, czy po zaszyfrowaniu
        tekstu wirniki mają zostać ustawione w początkowej pozcyji.Szyfrowane są tylko litery
        alfabetu (A-Z), a inne dozwolone znaki nie zmieniają się. Obrót wirników następuje tylko,
        gdy szyfrowana jest litera.

        :param text: tekst do zaszyfrowania
        :type text: str
        :param reset: określa czy po zaszyfrowaniu tesktu, ustawienie wirników ma zostać zresetowane
        :type reset: bool
        :return: zaszyfrowany tekst
        :rtype: str
        """
        if reset:
            self.connected_rotors().reset_positions()
        encrypted_text = ''
        text = text.upper()
        if not self.check_text(text):
            raise InvalidTextError

        for character in text:
            if character not in [' ', ',', '.', '!', '?', "'" "\n"]:
                encrypted_letter = self._encrypt_letter_complete(character)
                encrypted_text += encrypted_letter
            else:
                encrypted_text += character

        return encrypted_text

    def _encrypt_letter_complete(self, letter):
        """
        Szyfruje literę podaną na wejściu według ustawień maszyny. Szyfrowanie składa się z kliku kroków.
        Przed zaszyfrowaniem następuje zależny obrót wirników (zawsze obróci się pierwszy wirnik, a obrót kolejnych
        zależy od tego czy poprzedzający je wirnik znajdzie się w odpowiedniej pozycji).
        Później sprawdzane są połączenia na wejściowym wirniku i następuje podmiana. Potem otrzymana litera jest
        przekazywana dalej przez kolejne wirniki, aż do osiągniecia wirnika odwracająecgo, gdzie zostanie zamieniona
        na odpowiednią literę według połączeń. Następnie proces odbywa się w drugą stronę aż do osiągnięcia wirnika
        wejściowego i zamiany przez połącznie na łącznicy.

        :param letter: litera do zaszyfrowania
        :type letter: str
        :return: zaszyfrowana litera
        :rtype: str
        """

        # obrót wirników po wciśnięciu klawisza z literą
        self.connected_rotors().dependent_rotation()
        # zamiana szyfrowanej litery z literą połączoną z nia na łącznicy
        from_entrance = self.entrance_rotor().swap_letter_from_links(letter)
        # zaszyfrowanie litery przez wirniki
        from_rotors = self.connected_rotors().encrypt_letter(from_entrance)
        # zaszyfrowanie przez wirnik odwracający
        from_reverse = self.reverse_rotor().swap_letter(
            from_rotors,
            self.connected_rotors().get_rotor_position(len(self.connected_rotors())-1)
        )
        # podmiana litery przez wirnik odwracający
        reverse_swap = self.reverse_rotor().swap_letter_from_links(from_reverse)
        # zaszyfrowanie litery przez ostatni ruchomy wirnik
        swap_after_reverse = self.reverse_rotor().swap_letter(
            reverse_swap,
            self.connected_rotors().get_rotor_position(len(self.connected_rotors())-1),
            True)
        #  litery przez ruchome wirniki w drugą stronę
        from_reversed_rotors = self.connected_rotors().encrypt_letter(swap_after_reverse, reverse=True)
        # zamiana szyfrowanej litery z literą połączoną z nia na łącznicy
        encrypted_letter = self.entrance_rotor().swap_letter_from_links(from_reversed_rotors)
        return encrypted_letter

    @staticmethod
    def check_text(text):
        """
        Sprawdza czy dany teskt będzie mógł zostać zaszyfrowany. Dozwolone znaki to litery alfabetu (A-Z)
        oraz te należące do zbioru {' ', ',', '.', '!', "?", ":", ";", "\n"}.

        :param text: tekst do sprawdzenia
        :type text: str
        :return: True, jeśli tekst zawiera dozwolone znaki, False w przeciwnym wypadku.
        :rtype: bool
        """
        text = text.upper()
        for character in text:
            if character not in list(LETTERS.values())+[' ', ',', '.', '!', "?", ":", ";", "'", "\n"]:
                return False
        return True


class ConnectedRotors:
    """
    Klasa łącząca wiele wirników, dzięki czemu pozwala na zależny obrót wirników oraz szyfrowanie liter przechodząc
    przez kilka wirników.

    :param number_of_rotors: ilość wirników, które będą wykorzystane w szyfrowaniu
    :type number_of_rotors: int
    :param rotors: słownik zawierający indeksy oraz odpowiadające im wirniki
    :type rotors: dict
    :param order: kolejność w jakiej mają być ustawione wirniki (od lewej do prawje strony)
    :type order: list
    :param initial_code: kod początkowy określający w jakich pozycjach mają znajdować się wirniki (składa się z liter
    alfabetu w ilości odpowiadającej ilości wirników używanych w szyfrowaniu)
    :type initial_code: str
    """

    def __init__(self, number_of_rotors, rotors, order, initial_code=None):
        if number_of_rotors < 1:
            raise NumberOfRotorsError
        else:
            self._number_of_rotors = number_of_rotors
        self._rotors = rotors
        if len(set(list(rotors.keys())).difference(set([str(i) for i in range(1, number_of_rotors+1)]))) > 0:
            raise EnigmaRotorDataError("Missing rotor index")
        if not all([key in self.rotors().keys() for key in order]):
            raise OrderKeysError
        if initial_code and self.check_code(initial_code):
            self._initial_code = initial_code
        else:
            raise NoCodeError
        if len(order) != len(initial_code):
            raise OrderAndCodeLengthError
        self._order = order
        self.set_order(self.order())
        self._number_of_rotors = len(self.rotors())
        self._ordered_rotors = self._update_rotor_order()

    def number_of_rotors(self):
        """
        :return: ilość używanych wirników
        :rtype: int
        """
        return self._number_of_rotors

    def rotors(self):
        """
        :return: słownik zawierający wirniki jako wartości oraz ich indeksy jako klucze
        :rtype: dict
        """
        return self._rotors

    def initial_code(self):
        """
        :return: kod początkowy
        :rtype: str
        """
        return self._initial_code

    def order(self):
        """
        :return: kolejność wirników (lista zawierająca indeksy wirników w odpowiedniej kolejności)
        :rtype: list
        """
        return self._order

    def ordered_rotors(self):
        """
        :return: słownik zawierający wirniki ustawione w odpowiedniej kolejnośći
        :rtype: dict
        """
        return self._ordered_rotors

    def set_initial_code(self, code, reset=False):
        """
        Zmienia początkowy kod, jeśli podany jest prawidłowy oraz ustawia wirniki w odpowiednich pozycjach.

        :param code: kod, według którego mają być ustawione wirniki
        :type code: str
        :param reset: określa, czy wirniki mają być ustawione w pozycjach zgodnych z kodem początkowym.
        :type reset: bool
        """
        if not self.check_code(code):
            raise InvalidCodeError
        self._initial_code = code
        if reset:
            self.reset_positions()

    def reset_positions(self):
        """
        Ustawia wirniki w pozycjach odpowiadających kodowi początkowemu.
        """
        for i, rotor in self.ordered_rotors().items():
            letter = self._initial_code[-i-1].upper()
            rotor.set_position((ord(letter) - 65) % len(LETTERS.values()))

    def set_order(self, new_order):
        """
        Zmienia kolejność wirników oraz ustawia je w pozycji odpowiadającej kodowi początkowemu.

        :param new_order: lista zawierająca ustawione w kolejności indeksy wirników.
        :type new_order: list
        """
        if not self.check_order(new_order):
            raise InvalidOrderError
        self._order = new_order
        self._update_rotor_order()
        self.reset_positions()

    def set_code(self, code):
        """
        Zmienia początkowy kod, jeśli podany jest prawidłowy oraz ustawia wirniki w odpowiednich pozycjach.

        :param code: kod, według którego mają być ustawione wirniki
        :type code: str
        """
        if not self.check_code(code):
            raise InvalidCodeError
        self._initial_code = code
        self.reset_positions()

    def _update_rotor_order(self):
        """
        Aktualizuje kolejność wirników.

        :return: słownik zawierający wirniki ustawione w odpowiedniej kolejności
        :rtype: dict
        """
        ordered = {i: self.rotors()[key] for i, key in enumerate(self.order()[::-1])}
        self._ordered_rotors = ordered
        self.reset_positions()
        return ordered

    def dependent_rotation(self):
        """
        Symuluje zależny obrót wirników, uwzględniając dodatkowe obroty powodowane przez ustawienie
        wirników na pozycjach wymuszających rotację wirnika znajdującego się po lewej stronie.

        :return: kod odpowiadający pozycjom wirników po obrocie
        :rtype: str
        """
        right_rotation = True
        for rotor in self.ordered_rotors().values():
            if right_rotation:
                rotor.rotate()
                if LETTERS[rotor.position()] == rotor.additional_rotation():
                    continue
                else:
                    break
        return ''.join([LETTERS[rotor.position()] for rotor in self.ordered_rotors().values()][::-1])

    def encrypt_letter(self, letter, reverse=False):
        """
        Szyfruje literę według zasad działania Enigmy. Na wejściu dostaje literę otrzymaną z zamiany w wirniku
        odwracającym lub wejściowym.

        :param letter: litera do zaszyfrowania przez połączone wirniki
        :type letter: str
        :param reverse: określa kierunek, w którym zamieniane są litery
        :type reverse: bool
        :return: zaszyfrowana przez połączone wirniki litera
        :rtype: str
        """
        letter = letter.upper()
        letters = list(self.ordered_rotors().items()) if not reverse else list(self.ordered_rotors().items())[::-1]

        for i, rotor in letters:

            letter = rotor.swap_letter(letter, reverse=reverse) if i == 0 else \
                rotor.swap_letter(letter, self.get_rotor_position(i-1), reverse=reverse)
        return letter

    def get_rotor_position(self, index):
        """
        Zwraca aktualną pozycję wirnika o danym w indeksie(w aktualnym ustawieniu wirników).

        :param index: indeks wirnika ze słownika zawierającego wirniki ustawione w danej kolejności
        :type index: int
        :return: pozycja wirnika
        :rtype: int
        """
        if index not in self.ordered_rotors().keys():
            raise IndexError
        else:
            return self.ordered_rotors()[index].position()

    def current_code(self):
        """
        :return: aktualny kod odpowiadający pozycjom wirników ustawionych w określonej kolejności
        :rtype: str
        """
        return ''.join([LETTERS[rotor.position()] for rotor in list(self.ordered_rotors().values())[::-1]])

    def check_code(self, new_code):
        """
        Spradza czy kod spełnia określone warunki - długość równa ilości wirników oraz wszystkie znaki znajdują
        się w alfabecie.

        :param new_code: kod, według którego będą ustawione wirniki
        :type new_code: str
        :return: True, jeśli kod jest prawidłowy
        :rtype: bool
        """
        if not isinstance(new_code, str):
            raise CodeTypeError
        new_code = new_code.upper()
        if len(new_code) > self.number_of_rotors():
            raise CodeLengthError
        if not all([letter in LETTERS.values() for letter in new_code]):
            raise CodeKeysError
        return len(new_code) <= self.number_of_rotors() and all([letter in LETTERS.values() for letter in new_code])

    def check_order(self, new_order):
        """
        Spradza czy kolejność spełnia określone warunki - długość równa ilości wirników oraz wszystkie
        numery odpowiadają jakiemuś wirnikowi.

        :param new_order: kolejność wirników
        :type new_order: list
        :return: True, jeśli kolejność jest prawidłowa
        :rtype: bool
        """
        if not new_order:
            raise NoOrderError
        if len(new_order) > self.number_of_rotors():
            raise OrderLengthError
        if not all([val in self.rotors().keys() for val in new_order]):
            raise OrderKeysError
        if any([new_order.count(val) != 1 for val in new_order]):
            raise OrderRepeatedKeysError
        return all([val in self.rotors().keys() for val in new_order])

    def __len__(self):
        """
        :return: ilość aktualnie wykorzystywanych wirników
        """
        return len(self.ordered_rotors())

    def __str__(self):
        """
        Zwraca opis połączonych wirników, zawierający informacje o kodzie początkowym, ustawieniu wirników,
        oraz informacje o kolejnośći liter oraz dodatkowych obrotach wirników.

        :return: opis połączonych wirników
        :rtype: str
        """
        description = ""
        description += f"Kod początkowy: {self.initial_code()}\n"
        description += f"Kolejność wirników: {str([int(i) for i in self.order()])[1:-1]}\n"
        for i, rotor in self.rotors().items():
            description += f"{i}: {rotor.letter_order()} {rotor.additional_rotation()}\n"
        return description

    def __call__(self, key):
        """
        Pozwala odwołać się do wirnika według indeksu z wejściowego słownika.

        :param key: indeks wirnika w wejściowym słowniku zawierającym wirniki
        :type key: str
        :return: wirnik odpowiadający indeksowi
        :rtype: Rotor
        """
        return self.rotors()[key]

    def random_code(self):
        return ''.join([choice(list(LETTERS.values())) for _ in range(self.number_of_rotors())])

    def random_order(self):
        # print(self.rotors().keys())
        return ' '.join(sample(self.rotors().keys(), self.number_of_rotors())).rstrip()

    @staticmethod
    def check_number_of_rotors(number_of_rotors):
        """
        Sprawdza czy dana ilość wirników jest prawidłowa.

        :param number_of_rotors: ilość wirników
        :type number_of_rotors: int
        :return: True, jeśli ilość wirników jest prawidłowa
        :rtype: bool
        """
        if not isinstance(number_of_rotors, int):
            raise TypeError("Number of rotors must be an integer")
        elif number_of_rotors < 0:
            raise NumberOfRotorsError
        return True


class Rotor:
    """
    Klasa odpowiadająca wirnikowi, zawierająca kolejność liter od której zależy szyfrowanie i literę określającę,
    kiedy obraca się wirnik po lewej stronie.

    :param letter_order: napis zawierający litery z alfabetu ustawione w kolejności od której zależeć będzie szyfrowanie
    :type letter_order: str
    :param additional_rotation: litera, po której osiągnięciu na wirniku, obraca się wirnik po lewej stronie
    :type additional_rotation: str
    :param position: pozycja(obrót), w której jest ustawiony wirnik
    :type position: int
    """
    def __init__(self, letter_order, additional_rotation=None, position=0):
        if self.check_letters(letter_order):
            self._letter_order = letter_order.upper()
        self._indexed_swaps = {index: (letter, swapped) for index, (letter, swapped) in
                               enumerate(zip(LETTERS.values(), list(self.letter_order())))}
        self._position = position % len(LETTERS)

        if additional_rotation and additional_rotation.upper() not in LETTERS.values():
            raise AdditionalRotationError
        else:
            self._additional_rotation = additional_rotation.upper() if additional_rotation else "A"

    def letter_order(self):
        """
        Napis zawierający litery od A-Z.

        :return: kolejność liter
        :rtype: str
        """
        return self._letter_order

    def position(self):
        """
        :return: aktualna pozycja wirnika
        :rtype: int
        """
        return self._position

    def additional_rotation(self):
        """
        :return: litera(pozycja na wirnku), dla której wirnik po lewej stronie obróci się o jedną pozycję
        :rtype: str
        """
        return self._additional_rotation

    def indexed_swaps(self):
        """
        :return: słownik zawierający indeksy jako klucze oraz pary zamieniancych ze sobą liter
        :rtype: dict
        """
        return self._indexed_swaps

    def swaps(self):
        """
        :return: słownik zawierający litery z alfabetu jako klucze, a jako wartości litery,
        na które są zamieniane
        :rtype: dict
        """
        return {key: value for key, value in list(self._indexed_swaps.values())}

    def current_order(self):
        """
        Zwraca aktualną kolejność liter (za pierwsze miejsce przyjmuje literę z kodu na której znajduje się wirnik).

        :return: kolejność liter
        :rtype: dict
        """
        return self._update_order()

    def current_keys_ordered(self):
        """
        :return: aktualna kolejność liter alfabetu
        :rtype: list
        """
        return [x[0] for x in self.current_order().values()]

    def current_swaps_ordered(self):
        """
        :return: aktualna kolejność szyfrowanych liter
        :rtype: list
        """
        return [x[1] for x in self.current_order().values()]

    def set_position(self, number):
        """
        Ustawia pozycję wirnika.

        :param number: pozycja na której ma zostać ustawiony wirnik
        :type number: int
        """
        if isinstance(number, int):
            self._position = number % len(LETTERS)
        else:
            raise PositionError

    def set_letter_order(self, new_letter_order):
        """
        Pozwala ustawić kolejność, według której szyfruje dany wirnik.

        :param new_letter_order: litera z alfabetu
        :type new_letter_order: str
        """
        if self.check_letters(new_letter_order):
            self._letter_order = new_letter_order
            self._indexed_swaps = {index: (letter, swapped) for index, (letter, swapped) in
                                   enumerate(zip(LETTERS.values(), list(self.letter_order())))}

    def set_additional_rotation(self, letter):
        """
        Pozwala ustawić literę, dla której obróci się wirnik znajdujący się po lewej stronie.

        :param letter: litera z alfabetu
        :type letter: str
        """
        if letter.upper() in LETTERS.values():
            self._additional_rotation = letter.upper()
        else:
            raise AdditionalRotationError

    def swap_letter(self, letter, shift=0, reverse=False):
        """
        Zamienia literę według ustawienia liter w danym wirniku oraz przesunięciu sąsiedniego wirnika
        (jeden z kroków szyfrowania litery)

        :param letter: litera do zamiany
        :type letter: str
        :param shift: przesunięcie(ilość kroków od pozycji początkowej) wirnika, z którego zamieniana jest litera
        :type shift: int
        :param reverse: określa kierunek, w którym zamieniane są litery (dla False w kierunku wirnika odwracajęcego,
        a dla True w kierunku wirnika wejściowego)
        :type reverse: bool
        :return: zamieniona litera
        :rtype: str
        """
        letter = letter.upper()
        if letter not in LETTERS.values():
            raise KeyLetterError
        if not reverse:
            index = (list(LETTERS.values()).index(letter) + self.position() - shift) % 26
            return self.letter_order()[index]
        else:
            index = (self.letter_order().index(letter) - self.position() + shift) % 26
            return list(LETTERS.values())[index]

    def rotate(self):
        """
        Symuluje obrót wirnika w prawo - zwiększa pozycję wirnika o 1, jeśli przekroczy zakres wraca do pozycji 0
        """
        self._position = (self.position() + 1) % len(self)

    def _update_order(self):
        """
        Funkcja używana do zaktualizowania kolejności liter po obrocie wirnika.

        :return: aktualną kolejność zamienianych liter wraz z indeksami
        :rtype: dict
        """
        swaps = list(self.indexed_swaps().values())
        return {index: value for index, value in enumerate(swaps[self.position():] +
                                                           swaps[:self.position()])}

    def __len__(self):
        """
        Zwraca ilość pozycji wirnika.

        :return: długość listy zawierającej litery ustawione w kolejności
        :rtype: int
        """
        return len(self._letter_order)

    @staticmethod
    def random_letter_order():
        """
        :return: losowa kolejność liter
        :rtype: str
        """
        return ''.join(full_sample(list(LETTERS.values())))

    @staticmethod
    def random_rotation():
        """
        :return: losowa litera, dla której ma obracać się wirnik po lewej stronie
        :rtype: str
        """
        return choice(list(LETTERS.values()))

    @staticmethod
    def check_letters(letters):
        """
        Sprawdza podana kolejność liter zawiera wszystkie litery z alfabetu (A-Z) i żadna z nich się nie powtarza.

        :param letters: napis zawierająca litery w kolejności
        :type letters: str
        :return: zwraca True jeśli lista zawiera wszystkie litery z alfabetu
        :rtype: bool
        """
        length = len(LETTERS.values())
        letters = letters.strip().upper()
        if not letters:
            raise NoLetterOrderError
        if any([letter not in LETTERS.values() for letter in letters]):
            raise LetterOrderKeysError
        if len(letters.strip()) != length:
            raise LetterOrderLengthError
        if not len(set(letters)) == length:
            raise RepeatedLettersError
        return len(set(letters)) == length and all([letter in LETTERS.values() for letter in letters])


class StaticRotor:
    """
    Klasa odpowiadająca połączeniom na łącznicy, który zawiera określone połączenia między literami.
    (zasada działania podobna do tego jak działałby wirnik, który nie obraca się - stąd taka nazwa klasy)

    :param links: napis zawierający pary połączonych liter
    :type links: str
    """
    def __init__(self, links):
        if self.check_links(links):
            self._links = self._transform_links(links)
        self._number_of_links = self.count_links()
        self._set_letter_order()

    def links(self):
        """
        :return: słownik zawierający pary połączonych liter
        :rtype: dict
        """
        return self._links

    def number_of_links(self):
        """
        :return: ilość par liter
        :rtype: int
        """
        return self._number_of_links

    def letter_order(self):
        """
        Zwraca listę z kolejnością liter zgodną z połączeniami na łącznicy.

        :return: kolejność liter
        :rtype: list
        """
        return self._letter_order

    def _set_letter_order(self):
        """
        Ustawia kolejność w zależności od podanych par połączonych liter.

        :return: kolejność liter odpowiadająca połączonym parom
        :rtype: list
        """
        self._letter_order = [self.links()[key] for key in sorted(self.links().keys())]

    def count_links(self):
        """
        Zwraca ilość aktualnych par połączonych liter.

        :return: ilość połączeń par liter
        :rtype: int
        """
        return len([True for key, value in self.links().items() if key != value])//2 if self.links() else 0

    def swap_letter_from_links(self, letter):
        """
        Podmienia daną literę na tę, z którą jest w parze.

        :param letter: litera do zamiany
        :type letter: str
        :return: zamieniona litera
        :rtype: str
        """
        letter = letter.upper()
        if letter in self.links().keys():
            return self.links()[letter]
        else:
            raise KeyLetterError

    # def set_new_links_given_order(self, letter_order=None):
    #     """
    #     Ustawia nowe pary połączonych liter na podstawie danej kolejności liter.
    #
    #     :param letter_order: Kolejność liter
    #     :type letter_order: list
    #     """
    #     if self.reverse_check() and (not letter_order
    #                                  or (letter_order and not self.check_links(letter_order, self.reverse_check()))):
    #         raise ReverseLinksError
    #     elif not self.reverse_check() and not self.check_links(letter_order, self.reverse_check()):
    #         raise LinksError
    #     else:
    #         self._links = {key: value for key, value in zip(LETTERS.values(), letter_order)}
    #         self._number_of_links = self.count_links()

    # def set_new_links_random(self, expected_links=None):
    #     """
    #     Ustawia daną ilość losowych par połącząnych liter.
    #
    #     :param expected_links: ilość oczekiwanych par
    #     :type expected_links: int
    #     """
    #     if self.reverse_check() and expected_links:
    #         raise ReverseLinksError
    #     elif not self.reverse_check() and (not expected_links or not 0 <= expected_links < len(LETTERS.items())//2):
    #         raise NumberOfLinksError
    #     self._number_of_links = expected_links if not self.reverse_check() else len(LETTERS.items())//2
    #     self._links = self.random_keyboard_links(expected_links)

    def __str__(self):
        """
        :return: napis zawierający połączone pary liter
        :rtype: str
        """
        return str_links(self.links())

    @staticmethod
    def random_keyboard_links(number_of_links):
        """
        Zwraca losowe połączenia liter w określonej ilości.

        :param number_of_links: ilość oczekiwanych par liter
        :type number_of_links: int
        :return: słownik, w którym kluczami są litery, a wartościami litery na które zamieniane są klucze
        :rtype: dict
        """
        letters = set(LETTERS.values())
        if number_of_links > len(letters)//2 or number_of_links < 0:
            raise NumberOfLinksError
        first_set = set(sample(letters, number_of_links))
        second_set = set(sample(letters.difference(first_set), number_of_links))
        third_set = list(letters.difference(first_set.union(second_set)))
        letter_map = {}
        for first_letter, second_letter in zip(full_sample(list(first_set)), full_sample(list(second_set))):
            letter_map[first_letter] = second_letter
            letter_map[second_letter] = first_letter
        if third_set:
            for letter in third_set:
                letter_map[letter] = letter

        letter_map = {key: letter_map[key] for key in sorted(letter_map.values())}
        return letter_map

    @staticmethod
    def check_links(new_links):
        """
        Sprawdza czy napis z parami połączonych liter spełnia określone warunki.

        :param new_links: napis zawierający połączone ze sobą pary liter
        :type new_links: str
        :return: Zwraca True, jeśli wszystkie warunki połączeń par liter zostaną spełnione
        :rtype: bool
        """
        alphabet_letters = LETTERS.values()
        links = new_links.upper().split()
        links_letters = list(''.join(links))

        if not all([letter in alphabet_letters for letter in links_letters]):
            raise LinkKeysError()
        if not all([len(x) == 2 and x[0] != x[-1] for x in links]):
            raise LinkPairsError()
        if not all([links_letters.count(letter) == 1 for letter in links_letters]):
            raise LinksRepeatedKeysError()
        return True

    @staticmethod
    def _transform_links(new_links):
        """
        Przekształca napis zawierający pary połączonych liter na słownik.

        :param new_links: napis zawierający połączone ze sobą pary liter
        :type new_links: str
        :return: słownik, w którym kluczami są litery, a wartościami litery na które zamieniane są klucze
        :rtype: dict
        """

        links = {}
        alphabet_letters = set(LETTERS.values())
        links_letters = new_links.split()
        for link in links_letters:
            a, b = link[0], link[-1]
            links[a] = b
            links[b] = a
        links_letters = set((list(''.join(links_letters))))
        letters_left = alphabet_letters.difference(links_letters)
        for remaining in letters_left:
            links[remaining] = remaining
        return links

    @staticmethod
    def check_number_of_links(number):
        """
        Sprawdza czy ilość par jest prawidłowa.

        :param number: ilość par połączonych liter
        :type number: int
        :return: prawda lub w fałsz w zależności od tego czy liczba znajduje się w przedziale
        :rtype: bool
        """
        return 0 <= number <= len(LETTERS.values())//2


class ReverseRotor(StaticRotor):
    """
    Klasa odpowiadająca wirnikowi odwracającemu, który zawiera określone połączenia między literami.
    Dziedzicy po klasie StaticRotor, przy czym różni się tym, że wszystkie litery muszą się łączyć z inną literą.

    :param links: napis zawierający pary połączonych liter
    :type links: str
    """
    def __init__(self, links):
        super().__init__(links)
        if self.number_of_links() != len(LETTERS.values())//2:
            raise ReverseLinksError

    def swap_letter(self, letter, shift=0, reverse=False):
        """
        Zamienia literę według ustawienia liter w sąsiadującym wirniku oraz jego przesunięciu
        (jeden z kroków szyfrowania litery)

        :param letter: litera do zamiany
        :type letter: str
        :param shift: przesunięcie(ilość kroków od pozycji początkowej) wirnika, z którego zamieniana jest litera
        :type shift: int
        :param reverse: określa kierunek, w którym zamieniane są litery (dla False w kierunku wirnika odwracajęcego,
        a dla True w kierunku wirnika wejściowego)
        :type reverse: bool
        :return: zamieniona litera
        :rtype: str
        """

        letter = letter.upper()
        if letter not in LETTERS.values():
            raise KeyLetterError
        if not reverse:
            index = (list(LETTERS.values()).index(letter) - shift) % 26
            return self.letter_order()[index]
        else:
            index = (self.letter_order().index(letter) + shift) % 26
            return list(LETTERS.values())[index]

    @staticmethod
    def check_reverse_links(new_links):
        if not len(new_links.split()) == len(LETTERS.values())//2:
            raise ReverseLinksError
        return StaticRotor.check_links(new_links)


def str_links(links):
    """
    Zamienia słownik z parami połączonych liter na napis.

    :param links: Słownik, w którym kluczami są litery, a wartościami litery na które zamieniane są klucze
    :type links: dict
    :return: napis opisujący połącznia między literami
    :rtype: str
    """
    links_str = ""
    letters_to_use = list(LETTERS.values())
    for key in sorted(links.keys()):
        val = links[key]
        if key in letters_to_use and val in letters_to_use:
            if key != links[key]:
                links_str += f"{key}{links[key]} "
                letters_to_use.remove(key)
                letters_to_use.remove(val)
            else:
                letters_to_use.remove(key)

    return links_str.rstrip() + "\n"


def full_sample(letters):
    """
    Zwraca listę ustawionych losowo liter z alfabetu.
    :param letters: Lista składająca się z liter z alfabetu.
    :type letters: list
    :return: Lista liter z alfabetu ustawionych w losowej kolejności.
    :rtype: list
    """
    return sample(letters, len(letters))


if __name__ == "__main__":
    pass
