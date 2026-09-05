from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for word in strs:
      # Sort letters to form a universal key (e.g., 'act')
      sorted_key = "".join(sorted(word))
      res[sorted_key].append(word)

    return list(res.values())