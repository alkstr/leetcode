# 1352. Product of the Last K Numbers
#
# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
# Implement the ProductOfNumbers class:
# - ProductOfNumbers() Initializes the object with an empty stream.
# - void add(int num) Appends the integer num to the stream.
# - int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
# The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.


class ProductOfNumbers:
    def __init__(self):
        self.count = 0
        self.last_zero_index = -1
        self.numbers = [-1 for _ in range(40_000)]

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero_index = self.count
        if self.count == 0:
            self.numbers[0] = num
        elif self.numbers[self.count-1] == 0:
            self.numbers[self.count] = num
        else:
            self.numbers[self.count] = self.numbers[self.count-1] * num

        self.count += 1

    def getProduct(self, k: int) -> int:
        if self.last_zero_index == -1 and k == self.count:
            return self.numbers[self.count-1]
        if self.count - k <= self.last_zero_index:
            return 0
        if self.count - 1 - k == self.last_zero_index:
            return self.numbers[self.count-1]

        return self.numbers[self.count-1] // self.numbers[self.count-1-k]
