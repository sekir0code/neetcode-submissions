class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for i in s:
            s_count[i] = s_count.get(i, 0) + 1
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1
        return s_count == t_count