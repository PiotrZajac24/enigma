from src.enigma_settings import ConnectedRotors, Rotor, LETTERS
from src.enigma_exceptions import OrderKeysError, CodeTypeError, OrderKeysError, NoCodeError, EnigmaRotorDataError
from src.enigma_exceptions import CodeTypeError, OrderKeysError, KeyLetterError, OrderLengthError
from src.enigma_exceptions import OrderRepeatedKeysError, CodeKeysError, CodeLengthError
import pytest

letters_a = ''.join(["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P",
                     "A", "I", "B", "R", "C", "J"])
letters_b = ''.join(["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N",
                     "P", "Y", "F", "V", "O", "E"])
letters_c = ''.join(["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A",
                     "K", "M", "U", "S", "Q", "O"])
letters_d = "VDZUOAHPMYFCQLRGXISNTEJBWK"


def test_check_number_of_rotors():

    assert ConnectedRotors.check_number_of_rotors(9)
    with pytest.raises(TypeError):
        ConnectedRotors.check_number_of_rotors("AAA")
    with pytest.raises(TypeError):
        ConnectedRotors.check_number_of_rotors([3])


def test_check_order():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.check_order(['1', '2', '3'])
    with pytest.raises(OrderKeysError):
        connected.check_order(['1', '4', '3'])
    with pytest.raises(OrderLengthError):
        connected.check_order(['1', '2', '3', '2'])
    with pytest.raises(OrderRepeatedKeysError):
        connected.check_order(['1', '2', '2'])


def test_check_code():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.check_code("BPL")
    assert connected.check_code("ABf")
    with pytest.raises(CodeTypeError):
        connected.check_code(["ABG"])
    with pytest.raises(CodeKeysError):
        connected.check_code("AB6")
    with pytest.raises(CodeLengthError):
        connected.check_code("ABGA")


def test_create_connected_rotors():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert (
            connected.ordered_rotors()[0].letter_order() == letters_b and
            connected.ordered_rotors()[1].letter_order() == letters_a and
            connected.ordered_rotors()[2].letter_order() == letters_c
    )
    assert connected.current_code() == "FLG"


def test_create_connected_rotors_invalid_order():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "4", "1"]
    initial_code = "FLG"
    with pytest.raises(OrderKeysError):
        ConnectedRotors(3, rotors, order, initial_code)


def test_create_connected_rotors_without_code():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    with pytest.raises(NoCodeError):
        ConnectedRotors(3, rotors, order)


def test_connected_rotors_invalid_indices():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W"),
              "5": Rotor(letters_d, "A")}
    order = ["3", "5", "1", "2"]
    initial_code = "FLGR"
    with pytest.raises(EnigmaRotorDataError):
        _ = ConnectedRotors(4, rotors, order, initial_code)


def test_connected_rotors_current_code_and_dependant_rotation():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.current_code() == "FLG"
    connected.dependent_rotation()
    assert connected.current_code() == "FLH"
    for _ in range(27):
        connected.dependent_rotation()
    assert connected.current_code() == "FMI"


def test_get_rotor_position():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.get_rotor_position(0) == 6
    assert connected.get_rotor_position(1) == 11
    assert connected.get_rotor_position(2) == 5
    connected.set_order(['1', '2', '3'])
    assert connected.get_rotor_position(0) == 6
    assert connected.get_rotor_position(1) == 11
    assert connected.get_rotor_position(2) == 5
    connected.set_code("HSV")
    assert connected.get_rotor_position(0) == 21
    assert connected.get_rotor_position(1) == 18
    assert connected.get_rotor_position(2) == 7
    with pytest.raises(IndexError):
        connected.get_rotor_position('1')
    with pytest.raises(IndexError):
        connected.get_rotor_position(3)


def test_connected_rotors_reset_positions():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.current_code() == "FLG"
    for _ in range(3):
        connected.dependent_rotation()
    assert connected.current_code() == "FLJ"
    connected.reset_positions()
    assert connected.current_code() == "FLG"


def test_connected_rotors_set_code():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(CodeKeysError):
        connected.set_code("123")


def test_connected_rotors_set_code_too_long():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(CodeLengthError):
        connected.set_code("ABFDA")


def test_connected_rotors_set_code_wrong_type():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(CodeTypeError):
        connected.set_code(["ABF"])


def test_connected_rotors_set_order_wrong():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(OrderKeysError):
        connected.set_order(["5", "4", "3"])


def test_connected_rotors_set_order_valid():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    connected.set_order(["2", "1", "3"])
    assert connected.order() == ["2", "1", "3"]
    assert (
            connected.ordered_rotors()[0].letter_order() == letters_c and
            connected.ordered_rotors()[1].letter_order() == letters_a and
            connected.ordered_rotors()[2].letter_order() == letters_b
    )
    assert connected.current_code() == "FLG"


def test_ordered_rotors_and_update_rotor_order():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected.ordered_rotors() == {0: rotors['2'], 1: rotors['1'], 2: rotors['3']}
    connected.set_order(["1", "2", "3"])
    assert connected.ordered_rotors() == {0: rotors['3'], 1: rotors['2'], 2: rotors['1']}


def test_set_code_and_reset_positions():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    for _ in range(3):
        connected.dependent_rotation()
    assert connected.current_code() == "FLJ"
    connected.reset_positions()
    assert connected.current_code() == "FLG"
    connected.set_code("ABC")
    assert connected.current_code() == "ABC"
    for _ in range(3):
        connected.dependent_rotation()
    assert connected.current_code() == "ACF"
    connected.reset_positions()
    assert connected.current_code() == "ABC"


def test_connected_rotors_call():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert connected('1').letter_order() == letters_a
    assert connected('2').letter_order() == letters_b
    assert connected('3').letter_order() == letters_c
    assert connected('1').additional_rotation() == 'R'
    assert connected('2').additional_rotation() == 'F'
    assert connected('3').additional_rotation() == 'W'


def test_connected_rotors_call_incorrect():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(KeyError):
        _ = connected('4')
    with pytest.raises(KeyError):
        _ = connected(2)


def test_connected_rotors_str():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert str(connected) == f"""Kod początkowy: FLG
Kolejność wirników: 3, 1, 2
1: {letters_a} R
2: {letters_b} F
3: {letters_c} W
"""


def test_connected_rotors_len():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    assert len(connected) == 3


def test_encrypt_letter():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    # testowane jest szyfrowanie liter otrzymanych ze statycznych wirników przez ruchome wirniki (jeden z etapów),
    # więc wirniki nie obracają się przed szyfrowaniem litery - operacja odbywa się zatem dla kodu FLG, a nie FLH
    assert connected.encrypt_letter("S") == "T"
    assert connected.encrypt_letter("s") == "T"
    connected.dependent_rotation()
    assert connected.current_code() == "FLH"
    for _ in range(1000):
        connected.dependent_rotation()
        for letter in LETTERS.values():
            encrypted = connected.encrypt_letter(letter)  # zamiana od wirnika po prawej
            assert connected.encrypt_letter(encrypted, True) == letter  # zamiana od wirnika po lewej


def test_encrypt_letter_incorrect():
    rotors = {"1": Rotor(letters_a, "R"), "2": Rotor(letters_b, "F"), "3": Rotor(letters_c, "W")}
    order = ["3", "1", "2"]
    initial_code = "FLG"
    connected = ConnectedRotors(3, rotors, order, initial_code)
    with pytest.raises(KeyLetterError):
        connected.encrypt_letter("!")


