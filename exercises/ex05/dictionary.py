"""ex05 exercise."""

__author__ = "730733868"


# I was confused on how to nest the if instead the for and difference between lists and dicts
def invert(a: dict[str, str]) -> dict[str, str]:
    """Inversion function"""
    done: dict[str, str] = dict()

    for key in a:
        value = a[key]
        if value in done:
            raise KeyError("Duplicate value found!")
        done[value] = key
    return done


# I messed up the indentation so many different times before it stopped giving me red warning signs and probably overcomplicated it
def favorite_color(inf: dict[str, str]) -> str:
    """How to find favorite color"""
    times: dict[str, int] = dict()
    for name in inf:
        color = inf[name]
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


# I keep messing up when to use key vs empty[key]
def count(c: list[str]) -> dict[str, int]:
    """counting with dictionaries and list"""
    empty: dict[str, int] = dict()
    for key in c:
        if key in empty:
            empty[key] += 1
        else:
            empty[key] = 1

    return empty


# being able to use append in a dict threw me off at first
def alphabetizer(d: list[str]) -> dict[str, list[str]]:
    """assigning words to a specific letter based on alphabet"""
    em: dict[str, list[str]] = {}
    for word in d:
        low = word[0].lower()
        if low.isalpha():
            if low in em:
                em[low].append(word)
            else:
                em[low] = [word]
    return em


# i didnt realize that day and student were supposed to also be in paramters at first
def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """adding attendance for each day and person"""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
