"""testing functions"""

__author__ = "730733868"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_1() -> None:
    """The dictionaries keys and values should be switched"""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_2() -> None:
    """Testing invert again"""
    assert invert({"class": "early"}) == {"early": "class"}


def test_invert_edge() -> None:
    """Testing the edge case"""
    assert invert({}) == {}


def test_favorite_color_1() -> None:
    """This function should return the color seen the most"""
    assert (
        favorite_color({"Me": "green", "mom": "green", "dad": "blue", "sister": "idk"})
        == "green"
    )


def test_favorite_color_2() -> None:
    """testing to see if fav color returns the first one when duplicates of most common"""
    assert (
        favorite_color({"Me": "green", "mom": "green", "dad": "blue", "sister": "blue"})
        == "green"
    )


def test_favorite_color_edge() -> None:
    """testing edge case"""
    assert favorite_color({"me": "yellow"}) == "yellow"


def test_count_1() -> None:
    """counting repetitions"""
    assert count(["red", "orange", "red", "red"]) == {"red": 3, "orange": 1}


def test_count_2() -> None:
    """counting non repetitions"""
    assert count(["red", "orange", "blue"]) == {"red": 1, "orange": 1, "blue": 1}


def test_count_edge() -> None:
    """testing the edge for count"""
    assert count([]) == {}


def test_alphabetizer_1() -> None:
    """seeing if words get grouped by letter"""
    assert alphabetizer(["red", "orange", "green"]) == {
        "r": ["red"],
        "o": ["orange"],
        "g": ["green"],
    }


def test_alphabetizer_2() -> None:
    """testing it again but with multiple in a list"""
    assert alphabetizer(["red", "orange", "green", "rare"]) == {
        "r": ["red", "rare"],
        "o": ["orange"],
        "g": ["green"],
    }


def test_alphabetizer_edge() -> None:
    """testing the edge case of it"""
    assert alphabetizer([]) == {}


def update_attendance_1() -> None:
    """add person to already existing day"""
    attendance = {"Thursday": ["Tommy", "Brooke"]}
    update_attendance(attendance, "Thursday", "George")
    assert attendance == {"Thursday": ["Tommy", "Brooke", "George"]}
