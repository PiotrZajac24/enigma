from src.enigma_settings import Rotor, StaticRotor, ReverseRotor, ConnectedRotors, Settings, str_links, LETTERS
from src.enigma_machine import Enigma
from src.enigma_exceptions import SettingsPathNotFoundError, EnigmaRotorDataError
import pytest
import os

directory = "pliki_testowe"

letters_a = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
letters_b = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
letters_c = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

entrance_links = "QW HS ZX ER DF CV JK"
reverse_links = "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"


def prepare_settings():
    rotors = {'1': Rotor(letters_a, 'R'), '2': Rotor(letters_b, 'F'), '3': Rotor(letters_c, 'W')}
    order = ['3', '1', '2']
    code = 'FLG'
    connected = ConnectedRotors(3, rotors, order, code)
    entrance = StaticRotor(entrance_links)
    reverse = ReverseRotor(reverse_links)
    settings = Settings(connected, entrance, reverse)
    return settings


def test_create_settings():
    settings = prepare_settings()
    assert str(settings.entrance_rotor()).rstrip() == "CV DF ER HS JK QW XZ"
    assert str(settings.reverse_rotor()).rstrip() == "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
    assert settings.order() == "3 1 2"
    assert settings.initial_code() == "FLG"
    settings.connected_rotors().dependent_rotation()
    assert settings.connected_rotors().current_code() == "FLH"
    assert settings.connected_rotors()('1').letter_order() == letters_a


def test_check_text_only_letters():
    assert Settings.check_text("ANVDAFSGSGSasda")


def test_check_text_correct():
    assert Settings.check_text("AbCdEfGhIjKlMnOpQrStUvWxYz ,.!?:;\n")


def test_check_text_incorrect():
    assert not Settings.check_text(f"AbCd%EfGh@")


def test_encrypt_letter_complete():
    settings = prepare_settings()

    for letter in LETTERS.values():
        encrypted = settings._encrypt_letter_complete(letter)
        settings.connected_rotors().reset_positions()
        assert settings._encrypt_letter_complete(encrypted) == letter
        settings.connected_rotors().reset_positions()


def test_encrypt_text():
    settings = prepare_settings()

    text = "Projekt z PIPR"
    encrypted = settings.encrypt_text(text, reset=True)
    assert settings.connected_rotors().current_code() != settings.initial_code()
    assert settings.encrypt_text(encrypted, reset=True) == text.upper()


def test_order():
    settings = prepare_settings()
    settings.connected_rotors().set_order(['3', '2', '1'])
    assert settings.order() == "3 2 1"
    settings.connected_rotors().set_order(['1', '3', '2'])
    assert settings.order() == "1 3 2"


def test_initial_code():
    settings = prepare_settings()
    assert settings.initial_code() == "FLG"
    settings.connected_rotors().set_initial_code("BFA", reset=True)
    assert settings.initial_code() == "BFA"
    assert settings.current_code() == "BFA"
    settings.connected_rotors().set_initial_code("JRI", reset=False)
    assert settings.initial_code() == "JRI"
    assert settings.current_code() == "BFA"


def test_number_of_rotors():
    settings = prepare_settings()
    assert settings.number_of_rotors() == 3


def test_enigma_load_from_json_incorrect_path():
    machine = Enigma()
    with pytest.raises(SettingsPathNotFoundError):
        machine.load_from_json(os.path.join(directory, 'incorrect_path.json'))


def test_enigma_load_from_json_incorrect_settings():
    machine = Enigma()
    with pytest.raises(EnigmaRotorDataError):
        machine.load_from_json(os.path.join(directory, 'settings_incorrect_rotors.json'))


def test_enigma_load_from_json_correct():
    machine = Enigma()
    assert machine.potential_settings is None
    machine.set_settings()
    assert machine.settings is None
    machine.load_from_json(os.path.join(directory, 'correct_settings_and_text.json'))
    assert machine.potential_settings
    machine.set_settings()
    assert machine.settings.initial_code() == "RDVROGBCLT"
    assert machine.settings.order() == "10 6 8 3 2 5 9 7 1 4"
    assert str(machine.settings.reverse_rotor()).rstrip() == "AI BK CM DQ EJ FY GU HW LZ NV OT PR SX"
    assert str(machine.settings.entrance_rotor()).rstrip() == "AD BK GY HN JW MT PR SV"
    assert machine.settings.connected_rotors().number_of_rotors() == 10


def test_enigma_reset_settings():
    machine = Enigma()
    machine.load_from_json(os.path.join(directory, 'correct_settings_and_text.json'))
    machine.set_settings()
    assert machine.settings.initial_code() == "RDVROGBCLT"
    assert machine.settings.order() == "10 6 8 3 2 5 9 7 1 4"
    assert str(machine.settings.reverse_rotor()).rstrip() == "AI BK CM DQ EJ FY GU HW LZ NV OT PR SX"
    assert str(machine.settings.entrance_rotor()).rstrip() == "AD BK GY HN JW MT PR SV"
    assert machine.settings.connected_rotors().number_of_rotors() == 10
    machine.reset_settings()
    assert machine.settings is None


def test_enigma_str():
    machine = Enigma()
    assert str(machine) == "Maszyna nie jest jeszcze skonfigurowana."
    machine.load_from_json(os.path.join(directory, 'correct_settings_and_text.json'))
    machine.set_settings()
    assert str(machine) == """Połączenia na łącznicy: AD BK GY HN JW MT PR SV
Wirnik odwracający: AI BK CM DQ EJ FY GU HW LZ NV OT PR SX
Kod początkowy: RDVROGBCLT
Kolejność wirników: 10, 6, 8, 3, 2, 5, 9, 7, 1, 4
1: UCASKHRJMQXFZOEWBDYNGTLPVI P
2: YSWJQUHMXEBVZGIDNORATLPKCF S
3: FBAMGJOVNPCSTXHZQUYWLDEIKR W
4: PADHGUQKIFMXEWTSOVYBNCZLJR K
5: UJBPSMKDCGAQTRHWZEIVLOFXNY D
6: UNGVLTCQFOHDIBSXAPWZERMKYJ Z
7: QXRWMASVUTJIYFGDHNOKCLBEZP T
8: VTROYBANZKJDEHWMUFIQLCSGXP D
9: LAVJSDWMNBFZYQRCUTEPXOGHKI K
10: ZJUGSTPBLEMWRYVKXFNICHAOQD S
"""