# https://leetcode.com/problems/valid-anagram/

def isAnagram(s, t):
        return sorted(s) == sorted(t)

s1 = "nagaram"
s2 = "anagram"

print(isAnagram(s1, s2))