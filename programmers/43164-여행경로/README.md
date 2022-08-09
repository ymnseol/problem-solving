# 여행경로

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.</p>

<p>항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>모든 공항은 알파벳 대문자 3글자로 이루어집니다.</li>
<li>주어진 공항 수는 3개 이상 10,000개 이하입니다.</li>
<li>tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.</li>
<li>주어진 항공권은 모두 사용해야 합니다.</li>
<li>만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.</li>
<li>모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>tickets</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]</td>
<td>["ICN", "JFK", "HND", "IAD"]</td>
</tr>
<tr>
<td>[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]</td>
<td>["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1</p>

<p>["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.</p>

<p>예제 #2</p>

<p>["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.</p>
</div>
    </div>

***

## 풀이

DFS를 활용합니다.

```Python
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
```

### 수행 과정

1. 주어진 tickets으로 adjacent list를 생성합니다.
2. adjacent list의 모든 노드에 대해 인접 노드들을 알파벳 내림차순 정렬합니다. 이는 아래 조건을 만족시키기 위한 연산입니다.
   
   > 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

3. 'ICN'에서부터 DFS를 수행합니다.
   1. 만약 현재 위치한 노드에 방문하지 않은 인접 노드가 있다면, 알파벳 오름차순으로 정렬했을 때 가장 먼저 오는 노드를 스택에 삽입합니다. 이때 인접 노드 list에서 해당 인접 노드를 pop해, 해당 인접 노드를 방문했다는 것을 기록합니다.
   2. 만약 현재 위치한 노드에 방문하지 않은 인접 노드가 없다면, 경로에 기록합니다.
4. 기록된 경로를 뒤집습니다.

### 개선 과정

처음에는 아래와 같은 코드를 작성했습니다.

```Python
def dfs(s, g, p):
    stack = [s]
    visited = set()
    
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            u = u[:3]
            p.append(u)
            if u in g:
                g[u].sort(reverse=True)
                for v in g[u]:
                    if v not in visited:
                        stack.append(v)

def solution(tickets):
    tickets.sort()
    graph = dict()
    path = []
    tag = 0
    for s, d in tickets:
        try:
            graph[s].append(d + str(tag))
        except:
            graph[s] = [d + str(tag)]
        finally:
            tag += 1
    
    dfs("ICN", graph, path)
    
    return path
```

같은 공항을 여러 번 들릴 상황을 고려하여 모든 공항에 별도의 tag를 붙여 사용한 항공권을 구분할 수 있도록 했습니다.

DFS에서 기대하는 결과는 얻을 수 있었지만, 아래 조건을 동시에 만족시키지 못하는 경우가 발생했습니다.

> 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

> 주어진 항공권은 모두 사용해야 합니다.

| **tickets** | **return** |
|-|-|
| [["ICN", "ATL"], ["ATL", "CDG"], ["ATL", "IAD"], ["CDG", "SFO"], ["IAD", "ATL"]] | ["ICN", "ATL", "IAD", "ATL", "CDG", "SFO"] |

![testcase](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_43164_1.png)

위 예제의 tickets가 주어졌을 때, 위의 풀이는 ["ATL", "IAD"], ["IAD", "ATL"] 항공권을 사용하지 않습니다.  
현재 방문한 노드에서 이동할 수 있는 노드가 여러 개인 경우 알파벳 순서가 앞서는 노드로 이동하고, 더이상 이동할 수 있는 경로가 존재하지 않을 시 모든 항공권을 사용했는지 여부를 확인하지 않고 종료하기 때문입니다.  
따라서 잘못된 값인 ["ICN", "ATL", "CDG", "SFO"]가 반환됩니다.

문제에서 말하는 '가능한 경로'는 문제에서 주어진 모든 조건을 만족하는 경로를 의미합니다.  
이동 가능한 노드가 여러 개일 경우 알파벳 순서가 가장 빠른 노드로 이동한다고 해도, 항공권을 모두 사용하지 않고 종료되는 경우 이는 '가능한 경로'라고 할 수 없습니다.

이동 가능한 노드가 여러 개일 경우 알파벳 순서가 가장 빠른 노드로 이동했을 때, 모든 항공권을 사용하지 못하고 이동 불가능한 노드에 다다르는 경우, 아래 조건에 따라 해당 노드는 최종 도착지입니다.

> 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

위 성질을 활용해 현재 노드의 인접 노드 리스트에서 알파벳 오름차순으로 빠른 노드로 이동하고, 해당 노드를 방문 처리합니다.  
현재 노드의 인접 노드 리스트에 아무 것도 없다면, 경로에 추가합니다.

