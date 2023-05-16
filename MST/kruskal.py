graph = {
	'vt' : ['A', 'B', 'C', 'D', 'E'],
    'ed' : [
    	(3, 'A', 'B'),
        (7, 'A', 'C'),
        (5, 'A', 'D'),
        (3, 'B', 'A'),
        (8, 'B', 'C'),
        (6, 'B', 'E'),
        (7, 'C', 'A'),
        (8, 'C', 'B'),
        (3, 'C', 'D'),
        (5, 'D', 'A'),
        (3, 'D', 'C'),
        (9, 'D', 'E'),
        (6, 'E', 'B'),
        (6, 'E', 'C'),
        (9, 'E', 'D'),
    ]
}

parent = dict()		# path compression을 사용하기 위한 딕셔너리
rank= dict()		# union-by-rank를 사용하기 위한 딕셔너리

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    

def union(v,u):
    root1 = find(v)
    root2 = find(u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] +=1
            
            
def make_set(node):
    parent[node] = node
    rank[node] = 0
            
def kruskal(graph):
    mst = list()
    
    for node in graph['vt']:
        make_set(node)		# 각 정점을 독립적인 집합으로 초기화
    
    edges = graph['ed']
    edges.sort()			# 간선을 가중치 기준으로 정렬

   
    for edge in edges:
        w, v, u = edge
       
        if find(v) != find(u):		# 두 정점의 부모 노드가 다르다면 합치고 mst에 추가
            union(v,u)
            mst.append(edge)
    return mst

print(kruskal(graph))