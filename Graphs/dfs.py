def ajec_list(n,edges):
    graph=[[] for i in range (n)]
    for e in edges:
        a=e[0]
        b=e[1]
        graph[a].append(b)
        graph[b].append(a)
    
    return graph    



def dfs(graph, visited, current_node):
    visited[current_node]=True
    print(current_node)
    for node in graph[current_node]:
        if visited[node]:
            continue
        dfs(graph, visited, node)

n=5
edges=[(0,1),(0,2), (0,4), 
        (1,2),(1,3),
        (2,3),
        (3,1)
        ]
graph=ajec_list(n,edges)
print(edges)

visited=[False for i in range(n)]

# if not all nodes connected togethers
for i in range(n):
    if visited[i]:
        continue
    dfs(graph, visited, i)
