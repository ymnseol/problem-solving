# 큰 수의 법칙
## 문제
'큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다. 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.  
예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5인 46이 된다.  
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4+4+4+4+4+4+4인 28이 도출된다.  
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 대 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

### 입력 조건
- 첫째 줄에 N(2 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자여수는 1 이상 10,000 이하의 수로 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

### 출력 조건
- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

### 입력 예시
```
5 8 3
2 4 5 4 6
```

### 출력 예시
```
46
```

***

## 풀이
```Python
n_nums, n_additions, repeat_limit = map(int, input().split())
nums = [n * (-1) for n in list(map(int, input().split()))]
heapq.heapify(nums)

first_max = nums[0] * (-1)
if len(nums) == 2:
    second_max = nums[1] * (-1)
else:
    second_max = min(nums[1], nums[2]) * (-1)

remainder = n_additions % (repeat_limit + 1)
n_groups = (n_additions - remainder) // (repeat_limit + 1)

print((first_max * repeat_limit + second_max) * n_groups + second_max * remainder)
```

### 개선 과정
처음에는 최댓값과 최댓값 다음으로 큰 값을 찾기 위해 이진 탐색 트리(Binary Search Tree) 구조 활용을 고려했습니다.  

배열을 단순 정렬하여 최댓값과 최댓값 다음으로 큰 값을 찾는 것과, 주어진 배열로 binary search tree를 구성하고 node의 parent를 활용하여 최댓값과 최댓값 다음으로 큰 값을 찾는 것 중 어느 방법이 더 적은 시간을 소모할지 고민했습니다.  

Binary search tree의 경우 tree를 build하는 과정에서, 주어진 수가 $n$개일 때 skewed tree가 생성되는 최악의 경우 $O(n^2)$의 시간 복잡도를 가져 비효율적이라고 판단했습니다.  
AVL tree, Red-black tree 등 balance를 유지하기 위한 작업을 수행한다고 해도, 정렬을 위해 사용하는 $O(nlogn)$보다 나은 성능을 보일 것이라고 보장할 수 없다고 판단했습니다.  

그래서 내장 정렬 함수를 사용해 주어진 배열을 정렬하고, 그 중 최댓값과 최댓값 다음으로 큰 값을 추출했습니다.
```Python
n_nums, n_additions, repeat_limit = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

remainder = n_additions % (repeat_limit + 1)
n_groups = (n_additions - remainder) // (repeat_limit + 1)

print((nums[0] * repeat_limit + nums[1]) * n_groups + nums[1] * remainder)
```
해당 풀이는 정렬에서 $O(nlogn)$의 시간 복잡도를 가집니다.  

처음에 heap의 경우 search에 최적화되어있지 않은 구조라고 생각하여 후보에서 배제했었는데, 최댓값과 최댓값 다음으로 큰 값의 경우 heap의 search에서의 불리함과 상관 없이 쉽게 구할 수 있다고 생각했습니다.  

Max heap의 경우 heap property에 따라 모든 node의 children는 해당 node보다 작거나 같은 값을 가져야 합니다.  
해당 성질을 바탕으로, 최댓값 다음으로 큰 값의 경우 max heap의 root의 children 중 큰 값과 같다고 생각할 수 있었습니다.  

주어진 배열로 max heap을 build하고 최댓값과 최댓값 다음으로 큰 값을 찾는 과정은 $O(n)$의 시간 복잡도를 가집니다.
