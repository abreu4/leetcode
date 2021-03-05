# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

def findRestaurant(list1, list2):
        
        lookup = {}
        
        for i, item in enumerate(list1):
            lookup[item] = i
            
        result = []
        min_sum = len(list1) + len(list2)
        
        for i, item in enumerate(list2):
            
            if item in lookup:
                
                current_sum = i + lookup[item]
                
                if current_sum < min_sum:
                    result = [item]
                    min_sum = current_sum
                    
                elif current_sum == min_sum:
                    result.append(item)

                    
        return result