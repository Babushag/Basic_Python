def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
#       if not graph.has_key(start):
#          return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
        
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
print("choose the node from 'A','B','C','D','E','F'")     
frst=input("Enter the first node")
last=input("Enter the last node")
print("Path between the nodes you enter",find_path(graph,frst,last))                        
