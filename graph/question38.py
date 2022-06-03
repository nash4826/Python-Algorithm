# 332. Reconstruct Itinerary
# 일정 재구성

# [from,to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전 어휘순으로 방문한다.

import collections
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

#result = ["JFK","MUC","LHR","SFO","SJC"]


def sol(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    print(graph)
    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))

        route.append(a)

    dfs('JFK')
    return route[::-1]


print(sol(tickets))

# 후기
# result 값이 어떻게 출력되는지는 이해했으나, 이걸 구현하는데 감을 잡지 못하여 답안을 보았다.
# 딕셔너리를 이용한 재귀풀이인데 어떻게 이런 방식으로 풀 수 있는지 놀라움과 신기함이 공존했다.
# 반복,숙달하면 이해할 수 있지 않을까 생각한다.
