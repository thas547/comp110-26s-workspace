def can_eat(allergic: bool, temp: float) -> bool:
    """Is it safe to eat this food?"""
    return not allergic and temp >= 165.0


can_eat(allergic=False, temp=100)


def can_order(got_paid: bool, cost: float) -> bool:
    """Can I afford to eat this"""
    return got_paid or cost < 5.0


print(can_order(got_paid=False, cost=2.0))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter[0]:
        return "Match!"
    else:
        return "No match!"


print(check_first_letter(word="happy", letter="h"))
