# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
#
# Sample Output
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
#
# Т.е. сгруппировать слова по "общим буквам".

from collections import defaultdict


def groupAnagrams(strs):
    d = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        d[key].append(s)
    return list(d.values())


strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams(strs))
