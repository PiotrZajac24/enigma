from src.io_enigma import read_from_json, read_text_from_file, write_to_file, read_text_from_json
from src.enigma_exceptions import InvalidTextError, JsonTextError, OrderKeysError, LetterOrderLengthError,CodeKeysError, AdditionalRotationError
from src.enigma_exceptions import EnigmaRotorDataError, OrderAndCodeLengthError, OrderRepeatedKeysError
import pytest
import os
directory = 'pliki_testowe'


def test_read_text_from_file_correct():
    with open(os.path.join(directory, 'correct_text.txt'), 'r') as file_handle:
        text = read_text_from_file(file_handle)
    assert text == "Tekst do wczytania"


def test_read_text_from_file_incorrect():
    with pytest.raises(InvalidTextError):
        with open(os.path.join(directory, 'incorrect_text.txt'), 'r') as file_handle:
            _ = read_text_from_file(file_handle)


def test_read_text_from_json():
    with open(os.path.join(directory,'correct_settings_and_text.json'), 'r') as file_handle:
        text = read_text_from_json(file_handle)
    assert text == "JYINCZG V VKVF"


def test_read_text_from_json_empty():
    with pytest.raises(JsonTextError):
        with open(os.path.join(directory, 'correct_settings_no_text.json'), 'r') as file_handle:
            _ = read_text_from_json(file_handle)


def test_read_text_from_json_incorrect():
    with pytest.raises(InvalidTextError):
        with open(os.path.join(directory, 'correct_settings_incorrect_text.json'), 'r') as file_handle:
            _ = read_text_from_json(file_handle)


def test_read_settings_from_json():
    with open(os.path.join(directory, 'correct_settings_and_text.json'), 'r') as file_handle:
        settings = read_from_json(file_handle)
    assert settings.initial_code() == "RDVROGBCLT"
    assert settings.order() == "10 6 8 3 2 5 9 7 1 4"
    assert str(settings.reverse_rotor()).rstrip() == "AI BK CM DQ EJ FY GU HW LZ NV OT PR SX"
    assert str(settings.entrance_rotor()).rstrip() == "AD BK GY HN JW MT PR SV"
    assert settings.connected_rotors().number_of_rotors() == 10


def test_read_settings_from_json_incorrect_order():
    with pytest.raises(OrderKeysError):
        with open(os.path.join(directory, 'settings_incorrect_order.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_code():
    with pytest.raises(CodeKeysError):
        with open(os.path.join(directory, 'settings_incorrect_code.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_letter_order():
    with pytest.raises(LetterOrderLengthError):
        with open(os.path.join(directory, 'settings_incorrect_letter_order.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_additional_rotation():
    with pytest.raises(AdditionalRotationError):
        with open(os.path.join(directory, 'settings_incorrect_additional_rotation.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_entrance_swaps():
    with pytest.raises(AdditionalRotationError):
        with open(os.path.join(directory, 'settings_incorrect_additional_rotation.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_reverse_swaps():
    with pytest.raises(AdditionalRotationError):
        with open(os.path.join(directory, 'settings_incorrect_additional_rotation.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_incorrect_rotor_keys():
    with pytest.raises(EnigmaRotorDataError):
        with open(os.path.join(directory, 'settings_incorrect_rotors.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_different_code_and_order_length():
    with pytest.raises(OrderAndCodeLengthError):
        with open(os.path.join(directory,'settings_incorrect_order_and_code_length.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_from_json_order_repeated_rotors():
    with pytest.raises(OrderRepeatedKeysError):
        with open(os.path.join(directory, 'settings_order_repeat.json'), 'r') as file_handle:
            _ = read_from_json(file_handle)


def test_read_settings_correct():
    with open(os.path.join(directory, 'correct_settings.json'), 'r') as file_handle:
        settings = read_from_json(file_handle)
    assert len(settings.connected_rotors()) == 100
    assert str(settings.reverse_rotor()).rstrip() == "AI BR CN DK EZ FY GU HM JV LS OQ PX TW"
    assert str(settings.entrance_rotor()).rstrip() == "AF BV CZ EX GH IS PW UY"
    assert settings.connected_rotors()('5').letter_order() == "IAUKMRSDOXCBLQGJYZPTNEWFHV"
    assert settings.connected_rotors()('51').additional_rotation() == "H"
    assert settings.order() == "86 79 58 60 88 35 2 81 19 8 20 66 21 24 57 61 77 94 76 3 85 28 25 49 12 31 87 95 50" \
                               " 98 72 13 37 71 27 6 63 93 32 26 47 65 9 18 7 89 39 45 17 62 52 64 30 38 97 11 46 73" \
                               " 74 23 22 55 44 83 53 40 33 92 90 36 59 5 14 84 68 56 42 48 67 41 10 75 34 100 80 4 15"\
                               " 16 78 91 69 29 82 99 43 96 54 1 70 51"
    assert settings.initial_code() == "IQQVTGJEKOSUKQOGFONZCBENQNBQLSLQMXWCSTJNMRBBTDTEJAXAHABQWXLXCQKRNARASZBWIEZJO" \
                                      "IPYCZUPBKRKUWGLRPKRPSJP"


