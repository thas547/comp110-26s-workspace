def get_first(i: list[str]) -> str:
    return i[0]


def remove_first(f: list[str]) -> None:
    f.pop(0)


def get_and_remove_first(g: list[str]) -> str:
    el: str = g[0]
    g.pop(0)
    return el
