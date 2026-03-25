__author__ = "730733868"
"""Challenge question in class"""


def num_instances(phrase: str, search_char: str) -> int:
    index = 0
    count = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    return count


def get_evens(numbers: str) -> str:
    index = 0
    evens = str()
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            evens = evens + numbers[index]
            index += 1
        else:
            index += 1
    return evens
