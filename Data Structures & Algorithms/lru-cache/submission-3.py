class Node:

    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.map = {}


    def get(self, key: int) -> int:

        if key not in self.map:
            return -1

        node = self.map[key]

        if node != self.tail:

            if node == self.head:
                self.head = node.next
                self.head.prev = None

            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        return node.value


    def put(self, key: int, value: int) -> None:

        if key in self.map:

            node = self.map[key]
            node.value = value

            if node != self.tail:

                if node == self.head:
                    self.head = node.next
                    self.head.prev = None

                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node

            return

        if self.size == self.capacity:

            temp = self.head

            self.head = self.head.next

            if self.head:
                self.head.prev = None

            self.map.pop(temp.key)

            self.size -= 1

        node = Node(key, value)

        if self.size == 0:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.map[key] = node
        self.size += 1