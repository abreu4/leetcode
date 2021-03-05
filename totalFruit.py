# https://leetcode.com/problems/fruit-into-baskets/

def totalFruit(tree):
                
        start = 0
        max_sum = 0    
        baskets = {}
        
        
        for i, fruit in enumerate(tree):

            baskets[fruit] = i
            
            if len(baskets) >= 3:
                
                old_minimum = min(baskets.values())
                del baskets[tree[old_minimum]]

                start = old_minimum + 1 
            
            current_sum = i - start + 1
            if current_sum > max_sum: max_sum = current_sum

        return max_sum