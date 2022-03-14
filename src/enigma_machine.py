from src.io_enigma import *
from src.enigma_exceptions import *
from os.path import splitext
from random import sample, choice


class Enigma:
    """
    Klasa tworząca instancję maszyny, pozwala zmieniać ustawienia Enigmy.
    """

    def __init__(self):
        self.settings = None
        self.potential_settings = None

    def load_from_json(self, new_path):
        """
        Wczytuje ustawienia z pliku.

        :param new_path: ścieżka do pliku z ustawieniami
        :type new_path: str
        """
        ext = splitext(new_path)[-1][1:]
        try:
            with open(new_path, 'r') as file_handle:
                if ext == "json":
                    data = read_from_json(file_handle)
                    self.potential_settings = data
                else:
                    raise PathExtensionError(ext)
        except FileNotFoundError:
            raise SettingsPathNotFoundError("Could not find settings file")
        except PermissionError:
            msg = "You do not have permission to open settings file"
            raise SettingsPathPermissionError(msg)
        except IsADirectoryError:
            raise SettingsPathIsdirectoryError("Can only work on files")

    def reset_settings(self):
        """
        Usuwa aktualne ustawienia maszyny.
        """
        self.settings = None

    def set_settings(self):
        """
        Zmienia ustawienia maszyny na te, które zostały wstępnie zaakceptowane.
        """
        if self.potential_settings:
            self.settings = self.potential_settings

    def set_potential_random_settings(self, number_of_rotors, number_of_entrance_links):
        """
        Zmienia potencjalne ustawienia maszyny na losowe.
        """
        self.potential_settings = self.random_settings(number_of_rotors, number_of_entrance_links)

    @staticmethod
    def random_settings(number_of_rotors, number_of_entrance_links):
        """
        Generuje losowe ustawienia maszyny.

        :return: losowe ustawienia
        :rtype: Settings
        """
        # number_of_rotors = randint(3, 100)
        potential_keys = [str(i) for i in range(1, number_of_rotors+1)]
        rotors = {index: Rotor(''.join(sample(list(LETTERS.values()), 26)), choice(list(LETTERS.values()))) for
                  index in potential_keys}
        initial_code = ''.join([choice(list(LETTERS.values())) for _ in range(number_of_rotors)])
        order = sample(potential_keys, number_of_rotors)
        entrance_links = str_links(StaticRotor.random_keyboard_links(number_of_entrance_links))
        reverse_links = str_links(StaticRotor.random_keyboard_links(13))
        connected_rotors = ConnectedRotors(number_of_rotors, rotors, order, initial_code)
        entrance_rotor = StaticRotor(entrance_links)
        reverse_rotor = ReverseRotor(reverse_links)
        settings = Settings(connected_rotors, entrance_rotor, reverse_rotor)
        return settings

    def __str__(self):
        """
        Zwraca napis opisujący aktualne ustawienia maszyny.

        :return: napis opisujący ustawienia maszyny
        :rtype: str
        """
        if self.settings:
            return "Połączenia na łącznicy: " + str(self.settings.entrance_rotor()) + \
                   "Wirnik odwracający: " + str(self.settings.reverse_rotor())+str(self.settings.connected_rotors())
        else:
            return "Maszyna nie jest jeszcze skonfigurowana."


if __name__ == "__main__":
    pass