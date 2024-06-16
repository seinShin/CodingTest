from collections import defaultdict
from heapq import *
edges=[
    (3, 'A', 'B'), (5, 'A', 'D'), (7, 'A', 'C'),
    (6, 'B', 'C'), (6, 'B', 'E'),
    (3, 'C', 'D'), (6, 'C', 'E'),
    (9, 'D', 'E')
]

def prim(start_node, edges):
    mst = list()
    adj = defaultdict(list)		# value가 지정되어있지 않을 시 빈 리스트로 초기화
    for w, n1, n2 in edges:
        adj[n1].append((w,n1,n2))
        adj[n2].append((w,n2,n1))
        
    connected_node = set(start_node)	# 시작 노드를 연결 노드 집합에 삽입
    next_edge_list = adj[start_node]
    heapify(next_edge_list)				# 간선 리스트에서 최소 가중치를 가진 간선을 꺼내기 위해
    
    while next_edge_list:
        w, n1, n2 = heappop(next_edge_list)
        if n2 not in connected_node:
            connected_node.add(n2)
            mst.append((w, n1, n2))
            
            for edge in adj[n2]:			# n2 정점의 인접 간선 리스트 중 연결된 정점이 노드 집합에 없다면 heappush
                if edge[2] not in connected_node:
                    heappush(next_edge_list, edge)

    return mst

print(prim('A', edges))