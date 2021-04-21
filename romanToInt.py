# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
        
    total = 0
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
           
    prev = ""

    for c in reversed(s):
        total += -val[c] if prev and val[prev] > val[c] else val[c]
        prev = c

    return total


A = "XIX"
B = "MCMXCIV"
print(romanToInt(B))