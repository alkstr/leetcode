# 2551. Put Marbles in Bags
#
# You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the i_th marble. You are also given the integer k.
# Divide the marbles into the k bags according to the following rules:
# - No bag is empty.
# - If the ith marble and jth marble are in a bag, then all marbles with an index between the i_th and j_th indices should also be in that same bag.
# - If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
# The score after distributing the marbles is the sum of the costs of all the k bags.
# Return the difference between the maximum and minimum scores among marble distributions.

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)

        adj_sum = [weights[i] + weights[i+1] for i in range(N - 1)]
        adj_sum.sort()

        result = 0
        for i in range(k - 1):
            result += adj_sum[N - 2 - i] - adj_sum[i]

        return result


assert Solution().putMarbles([1, 3, 5, 1], 2) == 4
assert Solution().putMarbles([1, 3], 2) == 0
