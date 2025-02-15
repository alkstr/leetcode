# 2698. Find the Punishment Number of an Integer
#
# Given a positive integer n, return the punishment number of n.
# The punishment number of n is defined as the sum of the squares of all integers i such that:
# - 1 <= i <= n
# - The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

# import math
#
#
# def print_task_nums():
#    nums = []
#
#    def _is_suitable(num: int) -> bool:
#        square_str = str(num ** 2)
#        for i in range(1, len(square_str) + 1):
#            if __is_suitable(square_str, [(0, i)]):
#                return True
#        return False
#
#    def __is_suitable(square_str: str, parts: list[int, int]) -> bool:
#        last_part_end = parts[-1][1]
#
#        if last_part_end == len(square_str):
#            return sum(int(square_str[i:j]) for i, j in parts) == math.sqrt(int(square_str))
#
#        for i in range(last_part_end + 1, len(square_str) + 1):
#            if __is_suitable(square_str, parts + [(last_part_end, i)]):
#                return True
#
#        return False
#
#    for i in range(1, 1001):
#        if _is_suitable(i):
#            nums.append(i)
#
#    print("task_nums = [\n\t"
#          + ",\n\t".join(str(i) for i in nums)
#          + "\n]"
#          )

class Solution:
    def punishmentNumber(self, n: int) -> int:
        task_nums = [
            1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414,
            657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000
        ]

        result = 0
        for i in task_nums:
            if i > n:
                return result
            result += i ** 2

        return result


assert Solution().punishmentNumber(10) == 182
assert Solution().punishmentNumber(37) == 1478
