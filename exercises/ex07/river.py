__author__ = "730733868"

"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        newf = list()
        for fish in self.fish:
            if fish.age <= 3:
                newf.append(fish)
        self.fish = newf

        newb = list()
        for bear in self.bears:
            if bear.age <= 5:
                newb.append(bear)
        self.bears = newb

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        new_bear = list()
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bear.append(bear)
        self.bears = new_bear
        return None

    def repopulate_fish(self):
        baby_fish = int(len(self.fish) / 2) * 4
        num = 0
        while num < baby_fish:
            self.fish.append(Fish())
            num += 1
        return None

    def repopulate_bears(self):
        baby_bear = int(len(self.bears) / 2)
        num = 0
        while num < baby_bear:
            self.bears.append(Bear())
            num += 1
        return None

    def __str__(self) -> str:
        return f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"

    def __add__(self, r: River) -> River:
        all_fish = len(self.fish) + len(r.fish)
        all_bears = len(self.bears) + len(r.bears)
        all_river = River(all_fish, all_bears)
        return all_river

    def __mul__(self, factor: int) -> River:
        all_fish = len(self.fish) * factor
        all_bears = len(self.bears) * factor
        total_river = River(all_fish, all_bears)
        return total_river

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self) -> None:
        num = 0
        while num < 7:
            self.one_river_day()
            num += 1
        return None

    def remove_fish(self, amount: int):
        num = 0
        while num < amount:
            self.fish.pop(0)
            num += 1
        return None
