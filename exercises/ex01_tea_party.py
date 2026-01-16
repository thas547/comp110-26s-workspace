"""programming and function practice"""

__author__: str = "730733868"


def main_planner(guests: int):
    """Use the other functions and their parameters to make a tea party planner"""
    # I was a little confused how to stop getting errors when I just had tea_bags(guest)
    # adding str corrected it thougj
    # I went back to the functions a few times to figure out how to print it right
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """Determine the number of tea bags based on the number of people attending"""
    return 2 * people


def treats(people: int) -> int:
    """Determine the number of treats based on the number of guests"""
    return int(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Use the number of tea bags and treats to make a calculator for cost"""
    return 0.5 * tea_count + 0.75 * treat_count


# I wasn't sure if this return was right until it worked in trailhead

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
