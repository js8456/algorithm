# 가장 큰 수 | Lv2
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들 수 있는 가장 쿤 수를 return
# 매개변수는 0 또는 양의 정수가 담긴 배열 numbers
# 양의 정수는 0 <= <=1000
# return값은 문자열로 바꾸어 return


numbers = [3, 30, 34, 5, 9]

# Method_1 [Error | Time Out]
# idea: 조합만드는 함수로 만들어서 가장 max 값을 추출할까
# 코드 실행시 문제 없지만 시간초과 occurred, permutation이 시간을 많이 잡아먹는 것 같은 느낌

import itertools


def solution(numbers):
    num = list(map(str, numbers))
    # print(num)
    number = list(map("".join, itertools.permutations(num)))
    answer = max(number)
    return answer


# Method_2
# ASCII 이용하는 방법 -> 활용하여 문제 해결할 수 있음을 확인


def solution2(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(num)))
