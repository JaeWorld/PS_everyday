# BOJ 11779 최소비용 구하기 2

# 다익스트라 알고리즘

import sys
import heapq
input = sys.stdin.readline

INF = 987654321


def djikstra(start, graph, n, parent):
    dist = [INF]*(n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        d, v = heapq.heappop(queue)
        for a, w in graph[v]:
            nxt = d + w
            if nxt < dist[a]:
                dist[a] = nxt
                heapq.heappush(queue, [nxt, a])
                parent[a] = v

    return dist


def main():
    n = int(input())
    m = int(input())
    links = [list(map(int, input().split())) for _ in range(m)]
    start, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    parent = [0]*(n+1)
    path = []

    for link in links:
        u, v, w = link
        graph[u].append([v, w])

    dist = djikstra(start, graph, n, parent)
    e = end

    while True:
        if start == e:
            path.insert(0, start)
            break
        path.insert(0, e)
        e = parent[e]

    print(dist[end])
    print(len(path))
    print(*path)


main()
