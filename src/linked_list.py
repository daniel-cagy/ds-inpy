
class Node:
    def __init__(self, val: object, nxt: Node | None = None):
        self.val = val
        self.nxt = nxt

    def __eq__(self, node: object) -> bool:
        if type(node) != Node:
            return NotImplemented
        return self.val == node.val


    def __str__(self) -> str:
        return f"({self.val})"

    def __repr__(self) -> str:
        return f"({self} -> {self.nxt})"


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.len: int = 0

    def __str__(self) -> str:
        current = self.head
        elements: list[Node | None] = [None for _ in range(self.len)]
        i = 0
        while current != None:
            elements[i] = current
            current = current.nxt
            i+=1
        return f"{elements}"

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, key: int) -> object:
        if key < 0:
            raise IndexError
        current = self.head
        for _ in range(key):
            if type(current) != Node:
                raise IndexError
            current = current.nxt
        if type(current) != Node:
            raise IndexError
        return current.val

    def append(self, val: object) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = self.head
        elif self.head is self.tail:
            self.head.nxt = node
            self.tail = node
        else:
            if type(self.tail) == Node:
                self.tail.nxt = node
                self.tail = self.tail.nxt
        self.len += 1

    def pop(self) -> Node | None:
        if type(self.head) != Node:
            return None
        if not self.head is self.tail:
            current: Node | None = self.head
            while not (current.nxt is self.tail):
                print(current, current.nxt, self.tail)
                if type(current.nxt) == Node:
                    current = current.nxt
            if type(current) == Node:
                current.nxt = None
        else:
            self.head = None
            current = None
        popped = self.tail
        self.tail = current
        self.len -= 1
        return popped


