"""EX04 lists"""

__author__ = "730733868"


def all(lint: list[int], num: int) -> bool:
    if len(lint) == 0:
        return False
    index = 0
    while index < len(lint):
        if lint[index] != num:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 1
    high = input[0]
    while index < len(input):
        if input[index] > high:
            high = input[index]
        index += 1
    return high


def is_equal(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False
    index = 0
    while index < len(a):
        if a[index] != b[index]:
            return False
        index += 1
    return True


def extend(c: list[int], d: list[int]) -> None:
    index = 0
    while index < len(d):
        c.append(d[index])
        index += 1
