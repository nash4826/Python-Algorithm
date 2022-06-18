# 네트워크 딜레이 타임(743)
# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능한 경우 -1을 리턴한다.
# 입력값(u,v,w)는 각각 출발지, 도착지, 소요시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

# 다익스트라 알고리즘!

# 네덜란드의 컴퓨터 과학자 다익스트라가 대학원생이던 1956년 여자 친구와 함께 커피숍에 갔다가 20분 만에 고안해서 만든 알고리즘 (천재들이란..... )

# 다익스트라 알고리즘은 항상 노드 주변의 최단 경로만을 택하는 대표적인 그리디 알고리즘 중 하나이다.

# BFS(너비 우선 탐색)을 이용할 것이며, 본 풀이는 우선순위 큐(힙)를 이용하여 시간복잡도를 O(ElogV)로 만든다.

import collections
import heapq


def sol(times: list[list[int]], N: int, K: int):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == N:
        return max(dist.values())

    return -1


times = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [
    4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
n = 8
k = 3

print(sol(times, n, k))

# 후기
# 책을 보면서 구현했는데 최단거리, 그래프 관련한 알고리즘은 정말 어렵다. 문제에 따라 선택해야할 알고리즘의 폭이 넓고 적절한 알고리즘을 찾는 insight도 필요하다는 것을 느꼈다.
# 컴퓨터공학을 전공하시는 분들은 대단하신것 같다.
