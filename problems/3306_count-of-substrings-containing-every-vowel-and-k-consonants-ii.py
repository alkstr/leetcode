# 3306. Count of Substrings Containing Every Vowel and K Consonants II
#
# You are given a string word and a non-negative integer k.
# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def _count_of_substr_with_at_least_k(word: str, k: int) -> int:
            n = len(word)
            vowels = {"a", "e", "i", "o", "u"}

            left, right = 0, -1
            vowels_counter = Counter()
            consonants_count = 0
            substr_count = 0

            while left < n - 1:
                if right < n - 1 and (len(vowels_counter) < 5 or consonants_count < k):
                    right += 1
                    new_char = word[right]
                    if new_char in vowels:
                        vowels_counter[new_char] += 1
                    else:
                        consonants_count += 1
                else:
                    old_char = word[left]
                    left += 1
                    if old_char in vowels:
                        vowels_counter[old_char] -= 1
                        if vowels_counter[old_char] == 0:
                            del vowels_counter[old_char]
                    else:
                        consonants_count -= 1

                if len(vowels_counter) == 5 and consonants_count >= k:
                    substr_count += n - right

            return substr_count

        result = _count_of_substr_with_at_least_k(word, k) \
            - _count_of_substr_with_at_least_k(word, k + 1)
        return result


assert Solution().countOfSubstrings("aoaiuefi", 1) == 4
assert Solution().countOfSubstrings("iqeaouqi", 2) == 3

assert Solution().countOfSubstrings("aeioqq", 1) == 0
assert Solution().countOfSubstrings("aeiou", 0) == 1
assert Solution().countOfSubstrings("ieaouqqieaouqq", 1) == 3
