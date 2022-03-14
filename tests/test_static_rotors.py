from src.enigma_settings import StaticRotor, ReverseRotor, str_links
from src.enigma_exceptions import KeyLetterError, LinksRepeatedKeysError, LinkPairsError, LinkKeysError, ReverseLinksError
import pytest
from random import randint


def test_create_static_rotor_incorrect():
    with pytest.raises(AttributeError):
        StaticRotor(['G', 'C', 'Q', 'R', 'E', 'P', 'N', 'O', 'K', 'M', 'U', 'A', 'F', 'Y', 'Z', 'H', 'D',
                     'J', 'W', 'V', 'S', 'I', 'T', 'B', 'X', 'L'])


def test_create_static_rotor():
    assert StaticRotor.check_links("QW HS ZX ER DF CV JK")
    static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
    assert static_rotor.count_links() == 7
    assert static_rotor.number_of_links() == 7
    assert static_rotor.links() == {'A': 'A', 'B': 'B', 'C': 'V', 'D': 'F', 'E': 'R', 'F': 'D', 'G': 'G', 'H': 'S',
                                    'I': 'I', 'J': 'K', 'K': 'J', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
                                    'Q': 'W', 'R': 'E', 'S': 'H', 'T': 'T', 'U': 'U', 'V': 'C', 'W': 'Q', 'X': 'Z',
                                    'Y': 'Y', 'Z': 'X'}


def test_check_number_of_links_correct_and_incorrect():
    for i in range(14):
        assert StaticRotor.check_number_of_links(i)
    assert not StaticRotor.check_number_of_links(14)
    assert not StaticRotor.check_number_of_links(-1)
    with pytest.raises(TypeError):
        StaticRotor.check_number_of_links("12")
    with pytest.raises(TypeError):
        StaticRotor.check_number_of_links([1])


def test_check_links_correct():
    assert StaticRotor.check_links("AB CZ DW GM HO JU KQ NY PT RS VX")
    assert StaticRotor.check_links("")
    assert StaticRotor.check_links("AW BY CF GT IU")
    assert StaticRotor.check_links("AN BE CS DR FY GP HX IU JQ KV LM OT WZ")


def test_check_links_incorrect():
    with pytest.raises(LinksRepeatedKeysError):
        StaticRotor.check_links("AB CZ DW GH HO JU KQ NY PT RS VX")
    with pytest.raises(LinkKeysError):
        StaticRotor.check_links("AB CZ DW GH HO JU KQ NY PT RS V@")
    with pytest.raises(LinkPairsError):
        StaticRotor.check_links("AB CZ DWB GH HO JU KQ NY PT RS VX")


def test_transform_links():
    links = StaticRotor._transform_links("QW HS ZX ER DF CV JK")
    assert links == {"A": "A", "B": "B", "C": "V", "D": "F", "E": "R", "F": "D", "G": "G", "H": "S",
                     "I": "I", "J": "K", "K": "J", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P",
                     "Q": "W", "R": "E", "S": "H", "T": "T", "U": "U", "V": "C", "W": "Q", "X": "Z",
                     "Y": "Y", "Z": "X"}


def test_random_keyboard_links():
    for _ in range(1000):
        assert StaticRotor.check_links(str_links(StaticRotor.random_keyboard_links(randint(0, 13))))
    for _ in range(1000):
        assert StaticRotor.check_links(str_links(StaticRotor.random_keyboard_links(13)))


def test_str_static_rotor():
    static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
    assert str(static_rotor).rstrip() == "CV DF ER HS JK QW XZ"


def test_static_rotor_letter_order():
    static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
    assert static_rotor.letter_order() == ['A', 'B', 'V', 'F', 'R', 'D', 'G', 'S', 'I', 'K', 'J', 'L', 'M', 'N', 'O',
                                           'P', 'W', 'E', 'H', 'T', 'U', 'C', 'Q', 'Z', 'Y', 'X']

# def test_static_rotor_set_new_links_given_links():
#     static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
#     first_links = {'A': 'A', 'B': 'B', 'C': 'V', 'D': 'F', 'E': 'R', 'F': 'D', 'G': 'G', 'H': 'S',
#                    'I': 'I', 'J': 'K', 'K': 'J', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
#                    'Q': 'W', 'R': 'E', 'S': 'H', 'T': 'T', 'U': 'U', 'V': 'C', 'W': 'Q', 'X': 'Z',
#                    'Y': 'Y', 'Z': 'X'}
#     assert static_rotor.links() == first_links
#     new_links = "FB ZD LJ PW AX"
#     assert StaticRotor.check_links(new_links, False)
#     static_rotor.set_new_links_given_order(new_links)
#     assert static_rotor.links() != first_links
#
#
# def test_static_rotor_set_new_links_given_links_incorrect():
#     static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
#     with pytest.raises(LinksRepeatedKeysError):
#         static_rotor.set_new_links_given_order("BV DF AF HD IJ MV LJ")


# def test_static_rotor_set_new_links_random_without_number():
#     static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
#     with pytest.raises(NumberOfLinksError):
#         static_rotor.set_new_links_random()
#
#
# def test_static_rotor_set_new_links_random_wrong_number():
#     static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
#     with pytest.raises(NumberOfLinksError):
#         static_rotor.set_new_links_random(124214)


# def test_static_rotor_set_new_links_random_correct():
#     static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
#     static_rotor.set_new_links_random(8)
#     assert static_rotor.number_of_links() == 8


def test_static_rotor_swap_letter_from_links():
    static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
    assert static_rotor.links() == {'A': 'A', 'B': 'B', 'C': 'V', 'D': 'F', 'E': 'R', 'F': 'D', 'G': 'G', 'H': 'S',
                                    'I': 'I', 'J': 'K', 'K': 'J', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
                                    'Q': 'W', 'R': 'E', 'S': 'H', 'T': 'T', 'U': 'U', 'V': 'C', 'W': 'Q', 'X': 'Z',
                                    'Y': 'Y', 'Z': 'X'}

    for key in static_rotor.links().keys():
        val = static_rotor.swap_letter_from_links(key)
        assert static_rotor.swap_letter_from_links(val) == key
        assert static_rotor.swap_letter_from_links(val.lower()) == key


def test_static_rotor_swap_letter_from_links_incorrect():
    static_rotor = StaticRotor("QW HS ZX ER DF CV JK")
    with pytest.raises(KeyLetterError):
        assert static_rotor.swap_letter_from_links("1")


#######################################################################################################################
def test_check_reverse_links_correct():
    assert ReverseRotor.check_reverse_links("AC BD EL FJ GX HR IU KS MO NZ PW QV TY")
    assert ReverseRotor.check_reverse_links("AX BI CL DV ET FN GW HU JS KO MP QR YZ")
    assert ReverseRotor.check_reverse_links("AJ BG CS DT EO FM HQ IY KW LX NV PZ RU")
    assert ReverseRotor.check_reverse_links("AS BP CX DT EF GM HQ IL JY KO NW RZ UV")


def test_check_reverse_links_incorrect():
    with pytest.raises(LinksRepeatedKeysError):
        ReverseRotor.check_reverse_links("AC AD EL FJ GX HR IU KS MO NZ PW QV TY")
    with pytest.raises(LinkKeysError):
        ReverseRotor.check_reverse_links("AC @D EL FJ GX HR IU KS MO NZ PW QV TY")
    with pytest.raises(LinkPairsError):
        ReverseRotor.check_reverse_links("AC GAD EL FJ GX HR IU KS MO NZ PW QV TY")
    with pytest.raises(LinkPairsError):
        ReverseRotor.check_links("AC D EL FJ GX HR IU KS MO NZ PW QV TY")
    assert ReverseRotor.check_reverse_links("AY BR EQ FS GL HD IP KN MO TZ VW CU JX")
    with pytest.raises(ReverseLinksError):
        ReverseRotor.check_reverse_links("AC BD EL FJ GX HR IU KS MO NZ PW QV")


def test_create_reverse_rotor_incorrect_links():
    with pytest.raises(LinksRepeatedKeysError):
        ReverseRotor("AZ BR CU DH EQ FS GL IP JX KN MO TZ VW")


def test_create_reverse_rotor_correct_links():
    reverse_rotor = ReverseRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW")
    assert reverse_rotor.count_links() == 13
    assert reverse_rotor.number_of_links() == 13

#
# def test_reverse_rotor_set_new_links_given_order_correct():
#     reverse_rotor = StaticRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW", reverse_check=True)
#
#     new_links = "AM BI CY DW ES FX GN HV JP KL OQ RZ UT"
#     reverse_rotor.set_new_links_given_order(new_links)
#
#
# def test_reverse_rotor_set_new_links_given_order_incorrect():
#     reverse_rotor = StaticRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW", reverse_check=True)
#
#     new_links = "AA BX CG DI EF HO ID JL KV MP NS QT RZ UY WW"
#     with pytest.raises(LinkPairsError):
#         reverse_rotor.set_new_links_given_order(new_links)
#
#
# def test_reverse_rotor_set_new_links_random_incorrect():
#     reverse_rotor = StaticRotor("AM BI CY DW ES FX GN HV JP KL OQ RZ UT", reverse_check=True)
#
#     with pytest.raises(ReverseLinksError):
#         reverse_rotor.set_new_links_random(8)
#
#
# def test_reverse_rotor_set_new_links_random():
#     reverse_rotor = StaticRotor("AM BI CY DW ES FX GN HV JP KL OQ RZ UT", reverse_check=True)
#
#     assert reverse_rotor.number_of_links() == 13
#     assert reverse_rotor.number_of_links() > 0
#     assert reverse_rotor.number_of_links() < 14
#     reverse_rotor.set_new_links_random()


def test_transform_links_reverse():
    links = ReverseRotor._transform_links("AY BR EQ FS GL HD IP KN MO TZ VW CU JX")
    assert links == {'A': 'Y', 'Y': 'A', 'B': 'R', 'R': 'B', 'E': 'Q', 'Q': 'E', 'F': 'S', 'S': 'F', 'G': 'L', 'L': 'G',
                     'H': 'D', 'D': 'H', 'I': 'P', 'P': 'I', 'K': 'N', 'N': 'K', 'M': 'O', 'O': 'M', 'T': 'Z', 'Z': 'T',
                     'V': 'W', 'W': 'V', 'C': 'U', 'U': 'C', 'J': 'X', 'X': 'J'}


def test_letter_order_reverse_rotor():
    reverse = ReverseRotor("AY BR EQ FS GL HD IP KN MO TZ VW CU JX")
    assert reverse.letter_order() == ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I',
                                      'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']


def test_reverse_rotor_swap_letter_from_links_incorrect():
    reverse_rotor = ReverseRotor("AM BI CY DW ES FX GN HV JP KL OQ RZ UT")
    with pytest.raises(KeyLetterError):
        assert reverse_rotor.swap_letter_from_links("1")


def test_reverse_rotor_swap_letter_from_links_correct():
    reverse_rotor = ReverseRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW")

    assert reverse_rotor.swap_letter_from_links("A") == "Y"
    assert reverse_rotor.swap_letter_from_links("Y") == "A"
    assert reverse_rotor.swap_letter_from_links("W") == "V"
    assert reverse_rotor.swap_letter_from_links("W") == "V"
    assert reverse_rotor.swap_letter_from_links("h") == "D"
    assert reverse_rotor.swap_letter_from_links("D") == "H"
    assert reverse_rotor.swap_letter_from_links("q") == "E"
    assert reverse_rotor.swap_letter_from_links("e") == "Q"
    for key in reverse_rotor.links().keys():
        val = reverse_rotor.swap_letter_from_links(key)
        assert reverse_rotor.swap_letter_from_links(val) == key
        assert reverse_rotor.swap_letter_from_links(val.lower()) == key


def test_reverse_rotor_swap_letter():
    reverse_rotor = ReverseRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW")

    assert reverse_rotor.swap_letter("E", 3, reverse=False) == "R"
    assert reverse_rotor.swap_letter("F", 8, reverse=False) == "J"
    assert reverse_rotor.swap_letter("j", 13, reverse=False) == "V"


def test_reverse_rotor_swap_letter_reverse():
    reverse_rotor = ReverseRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW")

    assert reverse_rotor.swap_letter("E", 3, reverse=True) == "T"
    assert reverse_rotor.swap_letter("F", 8, reverse=True) == "A"
    assert reverse_rotor.swap_letter("j", 13, reverse=True) == "K"


def test_reverse_rotor_swap_letter_incorrect():
    reverse_rotor = ReverseRotor("AY BR CU DH EQ FS GL IP JX KN MO TZ VW")

    with pytest.raises(KeyLetterError):
        reverse_rotor.swap_letter("!", 4, True)


def test_str_reverse_rotor():
    reverse = ReverseRotor("EQ AY BR FS GL HD IP KN MO TZ VW CU JX")
    assert str(reverse).rstrip() == "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
