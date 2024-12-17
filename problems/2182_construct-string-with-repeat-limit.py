# 2182. Construct String With Repeat Limit
#
# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        n = len(s)
        chars = sorted(set(s), reverse=True)
        n_chars = len(chars)
        char_to_count = dict([(c, s.count(c)) for c in chars])
        left, right = 0, 0
        repeats = 0
        result = []

        for _ in range(n):
            while left < n_chars and char_to_count[chars[left]] == 0:
                left += 1
            if left >= n_chars:
                break

            if repeats == repeatLimit:
                if chars[left] != result[-1]:
                    result.append(chars[left])
                    char_to_count[chars[left]] -= 1
                else:
                    right = left + 1
                    while right < n_chars and char_to_count[chars[right]] == 0:
                        right += 1
                    if right >= n_chars:
                        break

                    result.append(chars[right])
                    char_to_count[chars[right]] -= 1
            else:
                result.append(chars[left])
                char_to_count[chars[left]] -= 1

            if len(result) >= 2 and result[-1] == result[-2]:
                repeats += 1
            else:
                repeats = 1

        return ''.join(result)


assert Solution().repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt",
                                      1) == "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"
assert Solution().repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy",
                                      2) == "yxxvvuvusrrqqppopponliihgfeeddcbba"

assert Solution().repeatLimitedString("cczazcc", 3) == "zzcccac"
assert Solution().repeatLimitedString("aababab", 2) == "bbabaa"
