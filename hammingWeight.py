# https://leetcode.com/problems/number-of-1-bits/

def hammingWeightA(n):
    return bin(n).count('1')

    
n = '00000000000000000000000000001011'
print(hammingWeightB(n))