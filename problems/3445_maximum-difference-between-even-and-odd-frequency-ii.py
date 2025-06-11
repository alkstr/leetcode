# 3445. Maximum Difference Between Even and Odd Frequency II
#
# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
# - subs has a size of at least k.
# - Character a has an odd frequency in subs.
# - Character b has an even frequency in subs.
# Return the maximum difference.
# Note that subs can contain more than 2 distinct characters.

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)

        def _status(a_count: int, b_count: int) -> int:
            return ((a_count & 1) << 1) | (b_count & 1)

        result = float("-inf")
        for a in "01234":
            for b in "01234":
                if a == b:
                    continue

                best = [float("inf")] * 4
                a_count = b_count = 0
                prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    a_count += (s[right] == a)
                    b_count += (s[right] == b)
                    while right - left >= k and b_count - prev_b >= 2:
                        left_status = _status(prev_a, prev_b)
                        best[left_status] = min(
                            best[left_status], prev_a - prev_b
                        )
                        left += 1
                        prev_a += (s[left] == a)
                        prev_b += (s[left] == b)

                    right_status = _status(a_count, b_count)
                    if best[right_status ^ 0b10] != float("inf"):
                        result = max(
                            result,
                            a_count - b_count - best[right_status ^ 0b10]
                        )

        return result


assert Solution().maxDifference("12233", 4) == -1
assert Solution().maxDifference("1122211", 3) == 1
assert Solution().maxDifference("110", 3) == -1
