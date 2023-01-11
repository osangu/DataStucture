from typing import Optional


class Node:

    def __init__(self, data):
        self.data = data

        self.previous: Optional['Node'] = None
        self.next: Optional['Node'] = None
