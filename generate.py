# https://leetcode.com/problems/pascals-triangle/

def generate(numRows):

	result = [[1]]

	for n in range(2, numRows+1):

		previous = result[n-2]
		current = [previous[0]]

		for i in range(1, n-1):
			current.append(previous[i]+previous[i-1])

		current.append(previous[-1])
		result.append(current)

	return result

n = 5
print(generate(n))