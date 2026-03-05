"""Mutating functions."""

__author__ = "730733868"


def manual_append(numb: list[int], a: int) -> None:
    numb.append(a)
    return


course: list[int] = [1, 2, 3]
manual_append(course, 2)
print(course)


def double(b: list[int]) -> None:
    index = 0
    while index < len(b):
        b[index] = b[index] * 2
        index += 1
    return


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
