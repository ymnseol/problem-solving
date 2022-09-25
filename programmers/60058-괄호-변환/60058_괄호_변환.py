from collections import deque

def is_proper(string: deque) -> bool:
    stack = []
    for parenthesis in string:
        if parenthesis == '(':
            stack.append('(')
        elif parenthesis == ')' and not stack:
            return False
        elif parenthesis == ')' and stack[-1] == '(':
            stack.pop()
    return (not stack)

def separate(string: deque) -> (deque, deque):
    u = deque()
    n_left_parentheses = 0
    while string:
        parenthesis = string.popleft()
        u.append(parenthesis)
        if parenthesis == '(':
            n_left_parentheses += 1
        if len(u) == n_left_parentheses << 1:
            break
    return u, string

def repeat(w: deque) -> deque:
    answer = deque()
    
    if not w:
        return w
    
    u, v = separate(w)
    if is_proper(u):
        return u + repeat(v)
    else:
        answer.appendleft('(')
        answer += repeat(v)
        answer.append(')')
        u.popleft()
        u.pop()
        u = deque([')' if parenthesis == '(' else '(' for parenthesis in u])
        answer += u
    
    return answer

def solution(p):
    p = deque(p)
    return ''.join(repeat(p))
