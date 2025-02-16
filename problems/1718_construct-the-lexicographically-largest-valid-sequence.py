# 1718. Construct the Lexicographically Largest Valid Sequence
#
# Given an integer n, find a sequence that satisfies all of the following:
# - The integer 1 occurs once in the sequence.
# - Each integer between 2 and n occurs twice in the sequence.
# - For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.
# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0 for _ in range(n * 2 - 1)]
        used = [False for _ in range(n + 1)]

        def _backtrack(i: int):
            if i == len(seq):
                return True
            if seq[i] != 0:
                return _backtrack(i + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue
                used[num] = True
                seq[i] = num

                if num == 1 and _backtrack(i + 1):
                    return True
                elif i + num < len(seq) and seq[i + num] == 0:
                    seq[i + num] = num

                    if _backtrack(i + 1):
                        return True

                    seq[i + num] = 0

                seq[i] = 0
                used[num] = False

            return False

        _backtrack(0)
        return seq


assert Solution().constructDistancedSequence(3) == [3, 1, 2, 3, 2]
assert Solution().constructDistancedSequence(5) == [5, 3, 1, 4, 3, 5, 2, 4, 2]
