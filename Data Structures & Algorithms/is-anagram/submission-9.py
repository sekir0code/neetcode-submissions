class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for character in s:
            if character in s_count:
                s_count[character] += 1
            else:
                s_count[character] = 1
        for character in t:
            if character in t_count:
                t_count[character] += 1
            else:
                t_count[character] = 1
        return s_count == t_count
