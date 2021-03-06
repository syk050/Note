# O(n^3) n <= 500
INF = 1e9

# 노드의 개수, 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트 무한을 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용: c
    graph[a][b] = c

# 점화식
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINYTY', end=' ')
        else:
            print(graph[a][b], end=' ')
