# 프로그래머스 - 다리를 지나는 트럭(42583)
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length - 1)])
    sum_on_bridge = 0
    n_trucks_on_bridge = 0
    
    while bridge:
        time += 1
        
        truck_passed = bridge.popleft()
        if truck_passed:
            sum_on_bridge -= truck_passed
            n_trucks_on_bridge -= 1
        
        if n_trucks_on_bridge == bridge_length:
            continue
        
        if truck_weights and sum_on_bridge + truck_weights[0] <= weight:
            truck_entering = truck_weights.popleft()
            sum_on_bridge += truck_entering
            n_trucks_on_bridge += 1
            for _ in range(0, bridge_length - len(bridge) - 1):
                bridge.append(0)
            bridge.append(truck_entering)
    
    return time
