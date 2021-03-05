# https://leetcode.com/problems/first-unique-character-in-a-string/

def firstUniqChar(s):
        
        if not s: return -1
        
        lookup = {}

        for i, c in enumerate(s):

            if c not in lookup: lookup[c] = [i]
            else: lookup[c].append(i)

                
        single_indexes = [indexes[0] for (char, indexes) in lookup.items() if len(indexes) == 1]
        
        if single_indexes: return min(single_indexes)
        else: return -1