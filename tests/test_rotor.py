from src.enigma_settings import Rotor, LETTERS
from src.enigma_exceptions import NoLetterOrderError, LetterOrderLengthError, LetterOrderKeysError
from src.enigma_exceptions import KeyLetterError, RepeatedLettersError, AdditionalRotationError, PositionError
import pytest


def test_rotor_check_letters_empty():
    set_of_letters = ""
    with pytest.raises(NoLetterOrderError):
        Rotor.check_letters(set_of_letters)


def test_rotor_check_letters_invalid_length():
    set_of_letters = ''.join(["A", "C", "D", "F"])
    with pytest.raises(LetterOrderLengthError):
        Rotor.check_letters(set_of_letters)


def test_rotor_check_letters_invalid_keys():
    set_of_letters = ''.join(["B", "D", "@", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W",
                              "G", "A", "K", "M", "U", "S", "Q", "O"])
    with pytest.raises(LetterOrderKeysError):
        Rotor.check_letters(set_of_letters)


def test_rotor_check_letters_repeated_characters():
    letters = ''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'P', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J', 'W',
                       'V', 'S', 'I', 'T', 'B', 'X', 'G'])
    with pytest.raises(RepeatedLettersError):
        Rotor.check_letters(letters)


def test_rotor_check_letters_correct():
    letters = ''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J', 'W',
                       'V', 'S', 'I', 'T', 'B', 'X', 'L'])
    assert Rotor.check_letters(letters)


def test_create_rotor_empty():
    with pytest.raises(NoLetterOrderError):
        Rotor("")


def test_create_rotor_letters_invalid_length():
    set_of_letters = ''.join(["A", "C", "D", "F"])
    with pytest.raises(LetterOrderLengthError):
        Rotor(set_of_letters)


def test_create_rotor_additional_rotation_empty():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']))
    assert rotor.additional_rotation() == "A"


def test_create_rotor_invalid_characters():
    with pytest.raises(LetterOrderKeysError):
        Rotor(''.join(["B", "D", "@", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G",
                       "A", "K", "M", "U", "S", "Q", "O"]))


def test_create_rotor_repeated_characters():
    with pytest.raises(RepeatedLettersError):
        Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'P', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J', 'W',
                       'V', 'S', 'I', 'T', 'B', 'X', 'G']))


def test_rotor_len():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']))
    assert len(rotor) == 26


def test_create_rotor_no_position():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "B")
    assert rotor.position() == 0
    assert rotor.additional_rotation() == "B"


def test_create_rotor_no_additional_rotation():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']))
    assert rotor.position() == 0
    assert rotor.additional_rotation() == "A"


def test_create_rotor_invalid_additional_rotation():
    with pytest.raises(AdditionalRotationError):
        Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J', 'W',
                       'V', 'S', 'I', 'T', 'B', 'X', 'L']), "!")


def test_create_rotor_invalid_position():
    with pytest.raises(TypeError):
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "F", [24, 1])


def test_rotor_rotate():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "C")
    assert rotor.position() == 0
    for _ in range(4):
        rotor.rotate()
    assert rotor.position() == 4


def test_position_and_rotate():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "F", 24)
    assert rotor.position() == 24
    for _ in range(4):
        rotor.rotate()
    assert rotor.position() == 2


def test_position_negative():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "G", -3)
    assert rotor.position() == 23
    for _ in range(4):
        rotor.rotate()
    assert rotor.position() == 1


def test_position_oversize():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "G", 250)
    assert rotor.position() == 16
    for _ in range(4):
        rotor.rotate()
    assert rotor.position() == 20


def test_set_additional_rotation():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "B", 24)
    assert rotor.position() == 24
    assert rotor.additional_rotation() == "B"
    rotor.set_additional_rotation("L")
    assert rotor.additional_rotation() == "L"


def test_set_additional_rotation_invalid():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "G", 24)
    assert rotor.position() == 24
    assert rotor.additional_rotation() == "G"
    with pytest.raises(AdditionalRotationError):
        rotor.set_additional_rotation("!")


def test_set_additional_rotation_correct_and_incorrect():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "A", 20)
    assert rotor.position() == 20
    assert rotor.additional_rotation() == "A"
    rotor.set_additional_rotation("B")
    assert rotor.additional_rotation() == "B"
    with pytest.raises(AdditionalRotationError):
        rotor.set_additional_rotation("1")


def test_indexed_swaps_and_current_order():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "J", 24)
    swaps = {0: ('A', 'G'), 1: ('B', 'C'), 2: ('C', 'Q'), 3: ('D', 'R'), 4: ('E', 'E'),
             5: ('F', 'P'), 6: ('G', 'N'), 7: ('H', 'O'), 8: ('I', 'K'), 9: ('J', 'M'),
             10: ('K', 'U'), 11: ('L', 'A'), 12: ('M', 'F'), 13: ('N', 'Y'), 14: ('O', 'Z'),
             15: ('P', 'H'), 16: ('Q', 'D'), 17: ('R', 'J'), 18: ('S', 'W'), 19: ('T', 'V'),
             20: ('U', 'S'), 21: ('V', 'I'), 22: ('W', 'T'), 23: ('X', 'B'), 24: ('Y', 'X'),
             25: ('Z', 'L')}

    assert rotor.indexed_swaps() == swaps
    assert rotor.indexed_swaps() != rotor.current_order()

    for _ in range(2):
        rotor.rotate()

    assert rotor.indexed_swaps() == rotor.current_order()


def test_rotor_current_order():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "D")

    for _ in range(2):
        rotor.rotate()

    assert rotor.current_order() == {0: ('C', 'Q'), 1: ('D', 'R'), 2: ('E', 'E'), 3: ('F', 'P'), 4: ('G', 'N'),
                                     5: ('H', 'O'), 6: ('I', 'K'), 7: ('J', 'M'), 8: ('K', 'U'), 9: ('L', 'A'),
                                     10: ('M', 'F'), 11: ('N', 'Y'), 12: ('O', 'Z'), 13: ('P', 'H'), 14: ('Q', 'D'),
                                     15: ('R', 'J'), 16: ('S', 'W'), 17: ('T', 'V'), 18: ('U', 'S'), 19: ('V', 'I'),
                                     20: ('W', 'T'), 21: ('X', 'B'), 22: ('Y', 'X'), 23: ('Z', 'L'), 24: ('A', 'G'),
                                     25: ('B', 'C')}


def test_current_keys_and_swapped_letters_order():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "J", 2)

    assert rotor.current_order() == {0: ('C', 'Q'), 1: ('D', 'R'), 2: ('E', 'E'), 3: ('F', 'P'), 4: ('G', 'N'),
                                     5: ('H', 'O'), 6: ('I', 'K'), 7: ('J', 'M'), 8: ('K', 'U'), 9: ('L', 'A'),
                                     10: ('M', 'F'), 11: ('N', 'Y'), 12: ('O', 'Z'), 13: ('P', 'H'), 14: ('Q', 'D'),
                                     15: ('R', 'J'), 16: ('S', 'W'), 17: ('T', 'V'), 18: ('U', 'S'), 19: ('V', 'I'),
                                     20: ('W', 'T'), 21: ('X', 'B'), 22: ('Y', 'X'), 23: ('Z', 'L'), 24: ('A', 'G'),
                                     25: ('B', 'C')}

    assert rotor.current_keys_ordered() == ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B']
    assert rotor.current_swaps_ordered() == ['Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H',
                                             'D', 'J', 'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L', 'G', 'C']


def test_rotate_and_current_order():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "V", 23)
    assert rotor.current_order() == {0: ('X', 'B'), 1: ('Y', 'X'), 2: ('Z', 'L'), 3: ('A', 'G'), 4: ('B', 'C'),
                                     5: ('C', 'Q'), 6: ('D', 'R'), 7: ('E', 'E'), 8: ('F', 'P'), 9: ('G', 'N'),
                                     10: ('H', 'O'), 11: ('I', 'K'), 12: ('J', 'M'), 13: ('K', 'U'), 14: ('L', 'A'),
                                     15: ('M', 'F'), 16: ('N', 'Y'), 17: ('O', 'Z'), 18: ('P', 'H'), 19: ('Q', 'D'),
                                     20: ('R', 'J'), 21: ('S', 'W'), 22: ('T', 'V'), 23: ('U', 'S'), 24: ('V', 'I'),
                                     25: ('W', 'T')}
    for _ in range(3):
        rotor.rotate()
    assert rotor.position() == 0
    assert rotor.current_order() == {0: ('A', 'G'), 1: ('B', 'C'), 2: ('C', 'Q'), 3: ('D', 'R'), 4: ('E', 'E'),
                                     5: ('F', 'P'), 6: ('G', 'N'), 7: ('H', 'O'), 8: ('I', 'K'), 9: ('J', 'M'),
                                     10: ('K', 'U'), 11: ('L', 'A'), 12: ('M', 'F'), 13: ('N', 'Y'), 14: ('O', 'Z'),
                                     15: ('P', 'H'), 16: ('Q', 'D'), 17: ('R', 'J'), 18: ('S', 'W'), 19: ('T', 'V'),
                                     20: ('U', 'S'), 21: ('V', 'I'), 22: ('W', 'T'), 23: ('X', 'B'), 24: ('Y', 'X'),
                                     25: ('Z', 'L')}


def test_swap_letter_single_rotor():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "H", 24)
    assert rotor.current_order() == {0: ('Y', 'X'), 1: ('Z', 'L'), 2: ('A', 'G'), 3: ('B', 'C'), 4: ('C', 'Q'),
                                     5: ('D', 'R'), 6: ('E', 'E'), 7: ('F', 'P'), 8: ('G', 'N'), 9: ('H', 'O'),
                                     10: ('I', 'K'), 11: ('J', 'M'), 12: ('K', 'U'), 13: ('L', 'A'), 14: ('M', 'F'),
                                     15: ('N', 'Y'), 16: ('O', 'Z'), 17: ('P', 'H'), 18: ('Q', 'D'), 19: ('R', 'J'),
                                     20: ('S', 'W'), 21: ('T', 'V'), 22: ('U', 'S'), 23: ('V', 'I'), 24: ('W', 'T'),
                                     25: ('X', 'B')}

    assert rotor.position() == 24
    new_letter = rotor.swap_letter("A", 0)
    assert new_letter == "X"
    new_letter = rotor.swap_letter("Y", 0)
    assert new_letter == "T"
    new_letter = rotor.swap_letter("L", 0)
    assert new_letter == "M"
    new_letter = rotor.swap_letter("L", 2)
    assert new_letter == "O"
    new_letter = rotor.swap_letter("a", 0)
    assert new_letter == "X"
    new_letter = rotor.swap_letter("y", 0)
    assert new_letter == "T"
    new_letter = rotor.swap_letter("l", 0)
    assert new_letter == "M"
    new_letter = rotor.swap_letter("l", 2)
    assert new_letter == "O"


def test_swap_letter_single_rotor_2():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "Z", 12)

    assert rotor.position() == 12
    new_letter = rotor.swap_letter("A", 6)
    assert new_letter == "N"
    new_letter = rotor.swap_letter("Y", 13)
    assert new_letter == "B"
    new_letter = rotor.swap_letter("L", 0)
    assert new_letter == "B"
    new_letter = rotor.swap_letter("L", 14)
    assert new_letter == "M"
    new_letter = rotor.swap_letter("a", 6)
    assert new_letter == "N"
    new_letter = rotor.swap_letter("y", 13)
    assert new_letter == "B"
    new_letter = rotor.swap_letter("l", 0)
    assert new_letter == "B"
    new_letter = rotor.swap_letter("l", 14)
    assert new_letter == "M"


def test_swap_letter_single_rotor_incorrect():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "Z", 12)
    with pytest.raises(KeyLetterError):
        assert rotor.swap_letter("1", 0)


def test_set_letter_order_incorrect():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']))
    with pytest.raises(LetterOrderLengthError):
        rotor.set_letter_order("ABCDEF")
    with pytest.raises(LetterOrderKeysError):
        rotor.set_letter_order("ABCDEFGHIJKLMNOPQRSTUVWXY@")
    with pytest.raises(RepeatedLettersError):
        rotor.set_letter_order("ABCDEFGHIJKLMNOPQRSTUVWXYA")


def test_set_letter_order():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']))
    rotor.set_letter_order("KLCSINGDMAUBQHPXTWZYJFVROE")
    assert rotor.letter_order() == "KLCSINGDMAUBQHPXTWZYJFVROE"


def test_rotor_set_position_correct():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "Z", 12)
    rotor.set_position(12)
    assert rotor.position() == 12
    rotor.set_position(28)
    assert rotor.position() == 2
    rotor.set_position(-2)
    assert rotor.position() == 24


def test_rotor_set_position_float():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "Z", 12)
    with pytest.raises(PositionError):
        rotor.set_position(23.3232)


def test_rotor_set_position_str():
    rotor = Rotor(''.join(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D', 'J',
                           'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L']), "Z", 12)
    with pytest.raises(PositionError):
        rotor.set_position("AAA")


def test_random_letter_order():
    pass


def test_random_rotation():
    pass