from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for word in strs:
      # Create a frequency array of 26 zeros for 'a' through 'z'
      count = [0] * 26

      for char in word:
        count[ord(char) - ord("a")] += 1

      # Tuples can be used as dictionary keys because they are immutable
      res[tuple(count)].append(word)

    return list(res.values())