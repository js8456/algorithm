# 모의고사 | Lv1
# 1번부터 마지막 문제까지 답을 찍음
# 찍는방식1. 1, 2, 3, 4, 5
# 찍는방식2. 2, 1, 2, 3, 2, 4, 2, 5
# 찍는방식3. 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
# 모든 문제의 정답이 순서대로 들은 배열 answer, 가장 많이 맞힌 사람 배열에 담아 return


# Method_1 | 테스트 14개 중 8개만 통과 -> 실패


def solution(answer):
    right_ans = {}
    p1_count = 0
    p2_count = 0
    p3_count = 0
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 2, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answer):
        if ans == p1[i % len(p1)]:
            p1_count += 1
        if ans == p2[i % len(p2)]:
            p2_count += 1
        if ans == p3[i % len(p3)]:
            p3_count += 1

    right_ans[1] = p1_count
    right_ans[2] = p2_count
    right_ans[3] = p3_count

    # right_ans = {
    #     k: v for k, v in sorted(right_ans.items(), key=lambda item: item[1])
    # }

    max_correct_p = []
    for k, v in right_ans.items():
        if v >= max(right_ans.values()):
            max_correct_p.append(k)

    return max_correct_p


solution([1, 3, 2, 4, 2])
# solution([1, 2, 3, 4, 5])


# Method_2 | 실패 -> 정확성: 57.1


def solution(answer):
    right_ans_f = []
    p1_count = 0
    p2_count = 0
    p3_count = 0
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 2, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answer):
        if ans == p1[i % len(p1)]:
            p1_count += 1
        if ans == p2[i % len(p2)]:
            p2_count += 1
        if ans == p3[i % len(p3)]:
            p3_count += 1

    right_ans = [p1_count, p2_count, p3_count]

    for p, score in enumerate(right_ans):
        if score == max(right_ans):
            right_ans_f.append(p + 1)

    return right_ans_f


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
