# https://leetcode.com/problems/fizz-buzz/

def fizzBuzz(n):
        
        if not n: return []
        answer = []
        names = {1: "Fizz", 2: "Buzz", 3: "FizzBuzz"}
        
        for i in range(1, n+1):
            key = 0
            if not i % 3: key += 1
            if not i % 5: key += 2
                
            answer.append(names[key]) if key else answer.append(str(i))
                
        return answer

n = 15
print(fizzBuzz(n))