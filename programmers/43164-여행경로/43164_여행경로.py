# 프로그래머스 - 여행경로(43164)
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    path = []
    graph = dict()
    
    for s, d in tickets:
        try:
            graph[s].append(d) 
        except:
            graph[s] = [d]
        finally:
            if d not in graph:
                graph[d] = []

    for _, i in graph.items():
        i.sort(reverse=True)
    
    stack = ["ICN"]
    
    while stack:
        u = stack[-1]
        
        if graph[u]:
            stack.append(graph[u].pop())
        else:
            path.append(stack.pop())
    
    return list(reversed(path))
