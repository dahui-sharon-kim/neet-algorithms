# https://leetcode.com/problems/valid-anagram/description/
from collections import deque

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    for i in s:
      if i in s_dict:
        s_dict[i] += 1
      else:
        s_dict[i] = 1
        
    for i in t:
      if i in t_dict:
        t_dict[i] += 1
      else:
        t_dict[i] = 1
    
    for i in t_dict:
      if not (i in s_dict) or s_dict[i] != t_dict[i]:
        return False
    for i in s_dict:
      if not (i in t_dict) or s_dict[i] != t_dict[i]:
        return False
    
    return True

print(Solution().isAnagram("ab", "a"))
print(Solution().isAnagram("a", "ab"))