# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 큰 수의 법칙

import heapq

if __name__ == '__main__':
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
