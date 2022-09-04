import heapq
from collections import defaultdict

def solution(alp, cop, problems):
    max_alp = max([prob[0] for prob in problems])
    max_cop = max([prob[1] for prob in problems])
    graph = {(prob[0], prob[1]): (prob[2], prob[3], prob[4]) for prob in problems}
    if alp >= max_alp and cop >= max_cop:
        return 0
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    
    cost = defaultdict(lambda: float('inf'))
    pq = [(0, alp, cop)]
    visited = set()
    
    while pq:
        curr_cost, ua, uc = cu = heapq.heappop(pq)
        u = (ua, uc)
        
        if curr_cost > cost[u]:
            continue
        cost[u] = curr_cost
        
        if ua == max_alp and uc == max_cop:
            break
        
        for v in graph:
            va, vc = v
            if ua >= va and uc >= vc:
                wa, wc = w = (min(ua + graph[v][0], max_alp), min(uc + graph[v][1], max_cop))
                new_cost = curr_cost + graph[v][2]
                if new_cost < cost[w]:
                    cost[w] = new_cost
                    cw = (new_cost, wa, wc)
                    if cw not in visited:
                        heapq.heappush(pq, cw)
            elif ua >= va and uc < vc:
                cw = (curr_cost + 1, ua, uc + 1)
                if cw not in visited:
                    heapq.heappush(pq, cw)
            elif ua < va and uc >= vc:
                cw = (curr_cost + 1, ua + 1, uc)
                if cw not in visited:
                    heapq.heappush(pq, cw)
            elif ua < va and uc < vc:
                cw = (curr_cost + 1, ua, uc + 1)
                cx = (curr_cost + 1, ua + 1, uc)
                if cw not in visited:
                    heapq.heappush(pq, cw)
                if cx not in visited:
                    heapq.heappush(pq, cx)
    
    return cost[(max_alp, max_cop)]
