# 프로그래머스 - 단속카메라(42884)
# https://school.programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    n_cameras = 1
    
    routes = sorted(routes, key=lambda route: route[1])
    curr_camera = routes[0][1]

    for start, end in routes:
        if start > curr_camera:
            curr_camera = end
            n_cameras += 1
    
    return n_cameras
