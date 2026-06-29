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
class  Queue1:
    def __init__(self):
        self.q=[]

    def enqueue(self, value):
        self.q.append(value)


    def dequeue(self):
        self.q.pop(0)

    def front(self):
        return self.q[0]
    def isEmpty(self):
        return len(self.q)==0
def bfs(graph, visited):
    q = Queue1()

    q.enqueue(0)
    visited[0] = True

    while not q.isEmpty():
        current_node = q.front()
        print(current_node)
        q.dequeue()

        for node in graph[current_node]:
            if visited[node]:
                continue

            q.enqueue(node)
            visited[node] = True
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

bfs(graph, visited)
