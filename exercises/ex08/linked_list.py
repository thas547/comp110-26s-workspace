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


node_c: Node = Node(4, None)
node_b: Node = Node(0, node_c)
node_a: Node = Node(5, node_b)


print(node_a.next.value)  # value of node_b
print(node_a.next.next.value)  # value of node_c
