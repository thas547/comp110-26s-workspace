from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first_names_output() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_first(names) == "Alyssa"


def test_get_and_remove_first_names_output() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_and_remove_first(names) == "Alyssa"


def test_remove_first_names_behavior() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]


def test_get_and_remove_first_names_behavior() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_and_remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]


def test_get_first_names_behavior() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_first(names)
    assert names == ["Alyssa", "Izzi", "Anusha", "Benjamin"]
