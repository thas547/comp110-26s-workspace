class Pizza:

    gluten_free: bool
    size: str
    num_toppings: int

    def __init__(self, gf: bool, sz: str, top: int):
        self.gluten_free = gf
        self.size = sz
        self.num_toppings = top
        # returns self

    def price(self, price_bump: float) -> float:
        total: float = price_bump
        if self.size == "small":
            total += 5.25
        else:
            total = 7.5
        total += self.num_toppings * 0.25
        if self.gluten_free == True:
            total += 1.0
        return total


# define function outside the class that uses the class
def num_orders(orders: list[Pizza]) -> int:
    return len(orders)


# instantiate class and use pizza constructor
alyssas_order: Pizza = Pizza(False, "small", 12)
jacks_order: Pizza = Pizza(True, "large", 4)
# alyssas_order.gluten_free = False
# alyssas_order.size = "small"
# alyssas_order.num_toppings = 12
# jacks_order.size = "large"
print(alyssas_order.size)
print(jacks_order.size)
print(alyssas_order.price(1.0))
pizza_list: list[pizza] = [alyssas_order, jacks_order, Pizza[False, "small", 0]]
print(pizza_list)
