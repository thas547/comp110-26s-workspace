"""ex05 exercise"""

__author__ = "730733868"


def invert(a: dict[str, str]) -> dict[str, str]:
    done: dict[str, str] = dict()

    for key in a:
        value = a[key]
        if value in done:
            raise KeyError("Duplicate value found!")
        done[value] = key
    return done


def favorite_color(input: dict[str, str]) -> str:
    times: dict[str, int] = dict()
    for name in input:
        color = input[name]
        if color in times:
            times[color] += 1
        else:
            times[color] = 1

        most = ""
        high = 0

        for color in times:
            if times[color] > high:
                high = times[color]
                most = color

        return most


def count(c: list[str]) -> dict[str, int]:
    empty: dict[str, int] = dict()
    for key in c:
        if key in empty:
            empty[key] += 1
        else:
            empty[key] = 1

    return empty


def alphabetizer(d: list[str]) -> dict[str, list[str]]:
    em: dict[str, list[str]] = {}
    for word in d:
        low = word[0].lower()
        if low.isalpha():
            if low in em:
                em[low].append(word)
            else:
                em[low] = [word]
    return em


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return
