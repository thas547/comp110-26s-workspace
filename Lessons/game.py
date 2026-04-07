from __future__ import annotations


class GameCollection:
    inventory: list[str]
    wishlist: list[str]
    budget: float

    def __init__(self, curr_inventory: list[str], wish: list[str], start_budget: float):
        self.inventory = curr_inventory
        self.wishlist = wish
        self.budget = start_budget

    def purchase(self, name: str, cost: float) -> None:
        if cost < self.budget:
            self.budget = self.budget - cost
            self.inventory.append(name)
            idx = 0
            while idx < len(self.wishlist):
                curr_game: str = self.wishlist[idx]
                if curr_game == name:
                    self.wishlist.pop(idx)
                idx += 1
            # if name in self.wishlist:
            # self.wishlist.pop(name)
        else:
            print("Sorry! Not enough money!")

    def __add__(self, new_game: str) -> GameCollection:
        new_wishlist: list[str] = []
        for item in self.wishlist:
            new_wishlist.append(item)
        new_wishlist.append(new_game)
        new_collection: GameCollection = GameCollection(
            self.inventory, self.wishlist, self.budget
        )
        return new_collection

    my_games: GameCollection = GameCollection(["Sims"], ["Witcher"], 50.75)
    my_games.purchase("Stardew", 40.25)
    my_games.purchase("Witcher", 60.00)
    ryans_games: GameCollection = my_games + "Mario"
