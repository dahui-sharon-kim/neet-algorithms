# https://leetcode.com/problems/permutation-in-string/

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        letters_in_s1 = defaultdict(int)
        for i in s1:
          letters_in_s1[i] += 1
          
        letters_in_s2 = defaultdict(int)
        length_s1 = len(s1)
        left = 0

        for right in range(len(s2)):
            letters_in_s2[s2[right]] += 1

            if right - left + 1 > length_s1:
                if letters_in_s2[s2[left]] == 1:
                    del letters_in_s2[s2[left]]
                else:
                    letters_in_s2[s2[left]] -= 1
                left += 1

            if letters_in_s1 == letters_in_s2:
                return True
        return False
        
        

print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
