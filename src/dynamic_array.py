class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):

        if self.count >= self.capacity:

            self.double_size()

        if index > self.count:
            self.double_size()

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]


        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)


    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage