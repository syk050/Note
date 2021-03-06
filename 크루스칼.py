# 신장 트리 -------------
# 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# => 트리의 조건

# 크루스칼 알고리즘 ------ 간선의 개수가 E일 때 O(ElogE)
# 최소 신장 트리 알고리즘
# 그리디 알고리즘
# 1. 간선 비용에 따라 오름차순으로 정렬
# 2. 간선을 확인하며 사이클 발생 우뮤 확인
# => 발생시 트리에 미 포함
# 3. 모든 간선에 대하여 2번의 과정 반복


# 특정 원소가 속한 집합
def find_parent(parent, x):
    # 자신이 부모노드의 부모로 설정되어 있는지
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


line = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (4, 6), (4, 7), (5, 6), (6, 7)]
cost = [29, 75, 35, 34, 7, 23, 13, 53, 25]
# 간선의 개수는 노드 개수의 -1개
parent = [0] * (len(cost)+1)

for i in range(1, len(cost)+1):
    parent[i] = i

edges = []
for i in range(len(cost)):
    # cost를 앞에 둬서 정렬하기 편하게
    edges.append((cost[i], line[i][0], line[i][1]))

result = 0
edges.sort()
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost)
