# 체육복 | Lv1
# 체육복 도난당한 사람들 있음. 바로 앞번호 or 뒷번호 학생에게만 체육복 빌려줄 수 있음
# 최대한 많은 사람이 (체육복을 입고) 체육 수업을 들어야 함
# 전체 학생의 수 n, 체육복 도난당한 학생 번호 배열 lost, 여벌 체육복 있는 학생 배열 reserve
# return 체육수업을 들을 수 있는 학생의 최댓값
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.


# Method_1
# 정확성: 15.0


def solution(n, lost, reserve):
    # n의 값에서 lost len 빼고 if reserve 값의 같은 값이나 +-1 이 lost에 있으면 return +1
    answer = n - len(lost)
    for x in reserve:
        for y in lost:
            if x == y:
                reserve.remove(x)
                lost.remove(y)
                answer += 1
            elif x - 1 == y:
                reserve.remove(x)
                lost.remove(y)
                answer += 1
            elif x + 1 == y:
                reserve.remove(x)
                lost.remove(y)
                answer += 1
    return answer


solution(5, [2, 4], [1, 3, 5])


# Method_2 : 정확성: 60.0
# 개선 solution : lost, reserve


def solution(n, lost, reserve):
    lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost)
    for x in reserve:
        if x - 1 in lost:
            lost.remove(x - 1)
        elif x + 1 in lost:
            lost.remove(x + 1)

    return n - len(lost)


solution(5, [2, 4], [1, 3, 5])


# Method_3
# 정확성: 80.0


def solution(n, lost, reserve):
    for x in reserve:
        if x in lost:
            lost.remove(x)
        elif x - 1 in lost:
            lost.remove(x - 1)
        elif x + 1 in lost:
            lost.remove(x + 1)

    return n - len(lost)


solution(5, [2, 4], [1, 3, 5])


# Method_4
# 정확성: 90.0


def solution(n, lost, reserve):
    lost_ = [x for x in lost if x not in reserve]
    reserve_ = [x for x in reserve if x not in lost]

    for x in reserve_:
        if x - 1 in lost_:
            lost_.remove(x - 1)
        elif x + 1 in lost_:
            lost_.remove(x + 1)
    return n - len(lost_)


solution(5, [2, 4], [1, 3, 5])


# Mothod_5
# umm 아이디어 떨어졌는데 


def solution(n, lost, reserve):

