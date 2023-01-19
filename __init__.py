from typing import Optional


class Head:

    def __init__(self, next_node: Optional['Node'] = None):
        self.next = next_node


class Node:

    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None
