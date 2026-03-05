ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(len(ice_cream))
print("chocolate" in ice_cream)
print("mint" in ice_cream)

if "mint" in ice_cream:
    print(f"There are {ice_cream["mint"]} orders of mint")
else:
    print("There are no orders of mint")


print(ice_cream)


def grade_bump(gradebook: dict[str, str], student: str) -> None:
    letter_grade: str = gradebook[student]
    if letter_grade == "A":
        gradebook[student] = "A+"


grades: dict[str, str] = {"alyssa": "A", "luke": "B"}
grade_bump(grades, "luke")


def celebrate(pet_names: list[str]) -> None:
    for index in pet_names:
        msg: str = f"Good boy, {index}"
        print(msg)


names: list[str] = ["Alyssa", "Izzi", "Benjamin"]
for index in range(0, len(names)):
    element = names[index]
    print(f"{index}:{element}")


def celebrate_again(pet_names: list[str]) -> None:
    for index in range(0, len(pet_names)):
        print(f"Good boy, {pet_names[index]}")


def get_orders(orders: dict[str, int]) -> None:
    for flavor in orders:
        print(f"{flavor} has {orders[flavor]} orders.")
