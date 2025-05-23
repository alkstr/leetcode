# 3068. Find the Maximum Sum of Node Values
#
# There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.
# Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:
# - Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
#   - nums[u] = nums[u] XOR k
#   - nums[v] = nums[v] XOR k
# Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.

from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0
        xor_count = 0
        min_pos, max_neg = 1 << 30, -(1 << 30)

        for num in nums:
            xored = num ^ k
            total_sum += num
            diff = xored - num
            if diff > 0:
                min_pos = min(min_pos, diff)
                total_sum += diff
                xor_count += 1
            else:
                max_neg = max(max_neg, diff)

        if xor_count % 2 == 0:
            return total_sum

        return max(total_sum - min_pos, total_sum + max_neg)


assert Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]) == 6
assert Solution().maximumValueSum([2, 3], 7, [[0, 1]]) == 9

assert Solution().maximumValueSum(
    [7, 7, 7, 7, 7, 7],
    3,
    [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
) == 42
