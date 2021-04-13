# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):

        from collections import defaultdict
        groups = defaultdict(list)

        for a in strs: groups[tuple(sorted(a))].append(a)

        return list(groups.values())

A = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(A))
