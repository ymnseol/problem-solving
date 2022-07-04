# 줄 세우기

## 문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

## 입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

## 출력
첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

## 예제 입력 1
```
3 2
1 3
2 3
```

## 예제 출력 1
```
1 2 3
```

## 예제 입력 2
```
4 2
4 2
3 1
```

## 예제 출력 2
```
4 2 3 1
```

## 출처
- 빠진 조건을 찾은 사람: indioindio
- 데이터를 추가한 사람: lhs456852

***

## 풀이
위상 정렬(Topological sort)을 활용합니다.
```python
from collections import deque

class SimpleDirectedGraph:
    def __init__(self, n_vertices):
        self.adj_list = [[] for _ in range(n_vertices + 1)]
        self.indegree = [0 for _ in range(n_vertices + 1)]

    def insert(self, s, d):
        self.indegree[d] += 1
        self.adj_list[s].append(d)
    
    def topological_sort(self):
        order = []
        queue = deque()

        for v, i in enumerate(self.indegree):
            if v and not i:
                queue.append(v)
        
        while queue:
            u = queue.popleft()
            order.append(str(u))
            
            for n in self.adj_list[u]:
                self.indegree[n] -= 1
                if not self.indegree[n]:
                    queue.append(n)

        return ' '.join(order)

if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = SimpleDirectedGraph(N)

    for i in range(M):
        s, d = map(int, input().split())
        graph.insert(s, d)

    print(graph.topological_sort())
```

### 개선 과정
이전에 그래프를 활용하는 문제에서 정점(vertex)의 개수가 간선(edge)의 개수보다 큰 희소 그래프(sparse graph)의 경우를 접해서, 입력 받은 정점에 대해서만 정보를 추가하도록 구조를 작성했습니다.
```python
from collections import deque

class SimpleDirectedGraph:
    def __init__(self):
        self.adj_list = dict()
        self.indegree = dict()
    
    def _set_indegree(self, v):
        if v not in self.indegree:
            self.indegree[v] = 0
    
    def _update_indegree(self, d):
        if d in self.indegree:
            self.indegree[d] += 1
        else:
            self.indegree[d] = 1

    def insert(self, s, d):
        self._set_indegree(s)
        self._update_indegree(d)
        if s in self.adj_list:
            self.adj_list[s].append(d)
        else:
            self.adj_list[s] = [d]
    
    def topological_sort(self):
        order = []
        queue = deque()

        for v, i in self.indegree.items():
            if not i:
                queue.append(v)
        
        while queue:
            u = queue.popleft()
            order.append(str(u))
            if u in self.adj_list:
                for n in self.adj_list[u]:
                    self.indegree[n] -= 1
                    if not self.indegree[n]:
                        queue.append(n)

        return ' '.join(order)

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = SimpleDirectedGraph()

    for i in range(M):
        s, d = map(int, input().split())
        graph.insert(s, d)
    
    print(graph.topological_sort())
```
채점이 70% 정도 진행되었을 때 오답 판정을 받았습니다.  

코드의 '_set_indegree'는 입력에서 주어지는 정점의 경우에만 self.indegree에 indegree를 세팅합니다.  
간선이 주어지지 않아 개념적으로 indegree가 0인 정점들을 결과에 추가해주지 않았기 때문에, 모든 학생에 대한 순서를 도출하지 않은 것이 실패 원인이었습니다.  

예를 들어,
```
3 1
1 2
```
와 같은 입력이 주어지면,
```
1 3 2
``` 
와 같은 결과를 기대하지만, 실제로 위의 코드는 간선에 주어지지 않은 3을 제외하고
```
1 2
```
와 같은 결과를 출력합니다.  

'topological_sort'에 간선에 주어지지 않은 정점의 indegree를 self.indegree에 추가하는 부분을 작성하여 채점을 통과할 수 있었습니다.
```python
from collections import deque

class SimpleDirectedGraph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_list = dict()
        self.indegree = dict()
    
    def _set_indegree(self, v):
        if v not in self.indegree:
            self.indegree[v] = 0
    
    def _update_indegree(self, d):
        if d in self.indegree:
            self.indegree[d] += 1
        else:
            self.indegree[d] = 1

    def insert(self, s, d):
        self._set_indegree(s)
        self._update_indegree(d)
        if s in self.adj_list:
            self.adj_list[s].append(d)
        else:
            self.adj_list[s] = [d]
    
    def topological_sort(self):
        order = []
        queue = deque()

        for v in range(1, self.n_vertices + 1):
            if v not in self.indegree:
                queue.append(v)
            elif not self.indegree[v]:
                queue.append(v)
        
        while queue:
            u = queue.popleft()
            order.append(str(u))
            if u in self.adj_list:
                for n in self.adj_list[u]:
                    self.indegree[n] -= 1
                    if not self.indegree[n]:
                        queue.append(n)

        return ' '.join(order)

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = SimpleDirectedGraph(N)

    for i in range(M):
        s, d = map(int, input().split())
        graph.insert(s, d)
    
    print(graph.topological_sort())
```
위의 코드는 채점 시 약 6000ms의 시간을 소모했습니다.  
<br>
> 학생들의 번호는 1번부터 N번이다.

정점은 N개, 정점의 번호는 1부터 N까지로 정해져 있습니다.  
모든 정점을 나열해야 하는 위상 정렬 과정을 고려해, 
1. 인접 리스트(adjacent list)를 dictionary 대신 N개의 sublist를 가진 list로 나타냅니다.  
2. 정점들의 indegree를 dictionary 대신 N개의 정점에 대해 indegree를 0으로 초기화한 list로 나타냅니다.  
   
수정된 코드는 채점 시 약 4000ms의 시간을 소모했습니다.