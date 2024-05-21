visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        if node in graph:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)

# Driver Code
# n = int(input())
# tree = list(map(int, input().split()))
n = 9
tree = 4, -1, 4, 1, 1, 0, 2, 0, 2
graph = {}
for i in range(n):
    graph[tree[i]] = graph.get(tree[i], [])
    graph[tree[i]].append(i)
#root = graph[-1][0]
root = -1
dfs(visited, graph, root)
#print()
print(graph)
#print(res)