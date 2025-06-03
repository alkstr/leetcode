# 135. Candy
#
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# - Each child must have at least one candy.
# - Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        result = [1 for _ in range(N)]

        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1

        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)

        return sum(result)


assert Solution().candy([1, 0, 2]) == 5
assert Solution().candy([1, 2, 2]) == 4
