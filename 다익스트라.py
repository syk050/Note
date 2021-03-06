import heapq
INF = int(1e9)

n, m = 6, 11
start = 1
data = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1), (2, 3, 3), (2, 4, 2), (3, 2, 3), (3, 6, 5),
    (4, 3, 3), (4, 5, 1), (5, 3, 1), (5, 6, 2)
]

# ------------------------------
# 각 노드에 연결되어있는 노드 정보 리스트
graph = [[] for i in range(n+1)]
# 시작 노드에서 각 노드까지의 거리
distance = [INF] * (n+1)

for d in data:
    a, b, c = d
    # 노드, 거리
    graph[a].append((b, c))


def dijkstra(start, graph):
    q = []
    INF = int(1e9)
    distance = [INF] * len(graph)

    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for node in graph[now]:
            n, c = node
            cost = c + dis
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

    return distance

