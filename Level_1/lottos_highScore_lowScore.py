# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

import random

def solution(lottos, win_nums):

    pop_win_nums = []
    for i in win_nums:
        pop_win_nums.append(i)

    not_lottos_num_all = list(range(1,47))
    for a in win_nums:
        not_lottos_num_all.remove(a)

    max_lottos = []
    min_lottos = []

    for i in lottos:
        max_lottos.append(i)
        min_lottos.append(i)

    for a in win_nums:
        if a in lottos:
            pop_win_nums.remove(a)

    # 로또 최대로 맞출 경우
    for i in range(0,6):
        if max_lottos[i] == 0:
            for j in pop_win_nums:
                for z in max_lottos:
                    if z not in pop_win_nums:
                        max_lottos[i] = j
                        pop_win_nums.remove(j)
                        break
                break

    print(max_lottos)

    # 로또 최소로 맞출 경우
    for i in range(0,6):
        if min_lottos[i] == 0:
            not_num = random.choice(not_lottos_num_all)
            min_lottos[i] = not_num
            not_lottos_num_all.remove(not_num)

    print(min_lottos)

    lottos_max_result = 7
    lottos_min_result = 7

    for i in max_lottos:
        if i in win_nums:
            lottos_max_result -= 1
    if lottos_max_result == 7:
        lottos_max_result = 6

    for i in min_lottos:
        if i in win_nums:
            lottos_min_result -= 1
    if lottos_min_result == 7:
        lottos_min_result = 6

    answer = [lottos_max_result, lottos_min_result]

    return answer
