# 완주하지 못한 선수 | Lv1
# 모든 참가자 중 한명을 제외하고 모두 완주, 완주하지 못한 선수의 이름을 return
# 참가자 중에는 동명이인이 있을 수 있고, completion의 길이는 언제나 participant 보다 -1

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# Method_1
from collections import Counter


def solution_1(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


# Method_2


def solution_2(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# Method_3


def solution_3(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
