from src.enigma_settings import *
from src.enigma_exceptions import *
import json


def read_text_from_json(file_handle):
    """
    Jeśli dane w pliku są poprawne, zwraca tekst do zaszyfrowania/odszyfrowania.

    :param file_handle: uchwyt do pliku
    :return: ustawienia maszyny
    :rtype: Settings
    """
    data = json.load(file_handle)
    if "text" in data.keys():
        text = data["text"]
        if Settings.check_text(text):
            return text
        else:
            raise InvalidTextError
    else:
        raise JsonTextError


def read_text_from_file(file_handle):
    """
    Jeśli dane w pliku są poprawne, zwraca tekst do zaszyfrowania/odszyfrowania.

    :param file_handle: uchwyt do pliku
    :return: ustawienia maszyny
    :rtype: Settings
    """

    data = ''.join(file_handle.readlines())
    if Settings.check_text(data):
        return data
    else:
        raise InvalidTextError


def read_from_json(file_handle):
    """
    Jeśli dane w pliku są poprawne, zwraca potencajlne ustawienia maszyny.

    :param file_handle: uchwyt do pliku
    # :param load_text: określa czy razem z ustawieniami ma zostać wczytany tekst do zaszyfrowania/odszyfrowania
    # :type load_text: bool
    :return: ustawienia maszyny
    :rtype: Settings
    """
    data = json.load(file_handle)
    try:
        number_of_rotors = data["number_of_rotors"]
        first_rotor_swaps = data["first_rotor_swaps"]
        reverse_rotor_swaps = data["reverse_rotor_swaps"]
        order = data["order"].split()
        initial_code = data["initial_code"]
        rotors = data["rotors"]
        # potential_keys = [str(i) for i in range(1, number_of_rotors+1)]
        first_rotor = StaticRotor(first_rotor_swaps)
        reverse_rotor = ReverseRotor(reverse_rotor_swaps)
        all_rotors = {index: Rotor(val["letter_order"], val["additional_rotation"]) for (index, val) in rotors.items()
                      if (val["letter_order"] and val["additional_rotation"])}
        # print(all_rotors.keys())
        connected_rotors = ConnectedRotors(number_of_rotors, all_rotors, order, initial_code)

        return Settings(connected_rotors, first_rotor, reverse_rotor)

    except Exception as e:
        raise e


def write_to_file(file_handle, settings, text=None):
    """
    Zapisuje aktualne ustawienia maszyny do pliku. Funkcja jest wykorzystywana w sytuacji, gdy maszyna jest poprawnie
    skonfigurowana.

    :param file_handle: uchwyt do pliku
    :param settings: aktualne ustawienia maszyny
    :type settings: Settings
    :param text: tekst do zaszyfrowania/odszyfrowania
    :type text: str
    """
    connected, reverse, entrance = settings.connected_rotors(), settings.reverse_rotor(), settings.entrance_rotor()

    number_of_rotors = connected.number_of_rotors()
    first_rotor_swaps = str(entrance).rstrip()
    reverse_rotor_swaps = str(reverse).rstrip()
    order = ' '.join(connected.order())
    initial_code = connected.initial_code()
    rotors = {}
    potential_keys = [str(i) for i in range(1, number_of_rotors+1)]
    for key in potential_keys:
        if key in connected.rotors():
            rotor = connected.rotors()[key]
            rotors[key] = {
                "letter_order": rotor.letter_order() if rotor.letter_order() else "",
                "additional_rotation": rotor.additional_rotation() if rotor.additional_rotation() else ""
            }
    enigma_settings = {
        "number_of_rotors": number_of_rotors,
        "first_rotor_swaps": first_rotor_swaps,
        "reverse_rotor_swaps": reverse_rotor_swaps,
        "order": order,
        "initial_code": initial_code,
        "rotors": rotors
    }
    if text is not None:
        enigma_settings["text"] = text

    json.dump(enigma_settings, file_handle, indent=4)


if __name__=="__main__":
    pass

