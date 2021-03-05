# https://leetcode.com/problems/clone-graph/

def cloneGraph(node):
        
        if node is None:
            return None
        elif not node.neighbors:
            return Node(node.val)
        
        visited = {}
        q = [node]
        
        while q:
            current_node = q.pop(0)
            
            if current_node not in visited:
                new_node = Node(current_node.val)
                visited[current_node] = new_node
                
            for ngb in current_node.neighbors:
                
                if ngb not in visited:
                    q.append(ngb)
                    new_ngb = Node(ngb.val)
                    visited[ngb] = new_ngb
                    
                visited[current_node].neighbors.append(visited[ngb])
        
        return visited[node]