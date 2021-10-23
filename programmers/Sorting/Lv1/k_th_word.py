# K번째 수 | Lv 1
# 배열 array의 i번째 숫자부터 j번째 숫자까지 슬라이싱 및 정렬 후 k번째에 있는 수를 return

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# Method_1


def solution1(array, commands):
    answer = []
    for c in commands:
        a = array[c[0] - 1 : c[1]]  # sort하기 전에 무조건 변수에 할당하고 sort 진행해야 None 안뜸
        a.sort()
        if len(a) >= c[2]:
            ans = a[c[2] - 1]
            answer.append(ans)
        else:
            pass

    return answer


# Method_2


def solution2(array, commands):
    return list(
        map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands)
    )


# Method_3


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command  # for i, j, k in command:
        answer.append(sorted(array[i - 1 : j])[k - 1])
    return answer
