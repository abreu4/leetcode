# https://leetcode.com/problems/excel-sheet-column-number/

def titleToNumber(columnTitle):

	keyme = lambda e: ord(e)-64

	if len(columnTitle) == 1: return keyme(columnTitle)

	max_cols = keyme("Z")
	nr = 0

	for i in range(len(columnTitle)):
		nr += keyme(columnTitle[-1-i]) * (26 ** i)

	return nr

# key(A) = 1, key(B) = 2...
# A -> key(A)
# AA -> key(A) * 26 + key(A)
# AAA -> key(A) * 26² + key(A) * 26 + key(A)

print(titleToNumber("AB"))
print(titleToNumber("FXSHRXW"))