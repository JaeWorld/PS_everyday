import sys
import heapq
input = sys.stdin.readline

INF = 987654321


def main():
    t = int(input())
    for _ in range(t):
        n, d, c = map(int, input().split())
        links = [list(map(int, input().split())) for _ in range(d)]
        graph = [[] for _ in range(n+1)]

        for link in links:
            a, b, s = link
            graph[b].append([a, s])

        dist = djikstra(c, n, graph)
        infected = 0
        last = 0
        for i in range(len(dist)):
            if dist[i] == INF:
                continue
            infected += 1
            if dist[i] > last:
                last = dist[i]

        print(infected, last)


def djikstra(start, n, graph):
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

    return dist


main()
