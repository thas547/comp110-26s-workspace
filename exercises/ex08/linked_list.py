from __future__ import annotations


class Node:

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value}->None"
        else:
            return f"{self.value}->{self.next}"

    courses: Node = Node(110, Node(210, None))

    def sum(head: Node | None) -> int:
        # base case
        if head.next is None:
            return head.value
        else:
            return sum(head.next) + head.value  # next nodse sum + my value

    def value_at(head: Node | None, index: int) -> int:
        if head is None:
            raise IndexError("Index is out of bounds on the list.")
        if index == 0:
            return head.value
        return value_at(head.next, index - 1)

    def max(head: Node | None) -> int:
        if head is None:
            raise ValueError("Canot call max with None")
        if head.next is None:
            return head.value
        rest = max(head.next)
        if head.value > rest:
            return head.value
        else:
            return rest

    def linkify(items: list[int]) -> Node | None:
        if len(items) == 0:
            return None
        return Node(items[0], linkify(items[1:]))

    def scale(head: Node | None, factor: int) -> Node | None:
        if head is None:
            return None
        return Node(head.value * factor, scale(head.next, factor))


node_c: Node = Node(4, None)
node_b: Node = Node(0, node_c)
node_a: Node = Node(5, node_b)


print(node_a.next.value)  # value of node_b
print(node_a.next.next.value)  # value of node_c
