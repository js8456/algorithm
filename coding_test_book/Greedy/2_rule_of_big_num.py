# 배열의 숫자들을 M번 더하여 가장 큰 수를 만드는 법칙
# 그러나 배열의 특정한 인덱스에 해당하는 수가 연속으로 k번을 초과하여 더해질 수 없음
# [2,4,5,6,4,6]일 경우 6+6+6+5+6+6+6이 됨
# 배열의 크기 N, 더하는 횟수 M, 연속 더할 수 있는 번수 K

num_list = [2, 4, 5, 4, 6]
n, m, k = [5, 8, 3]

# Method_1


def max_sum():
    num_list.sort(reverse=True)
    max_iter = m // k  # 가장 큰 수로 max iter을 돌리고 두번째로 큰 숫자를 중간에 넣음
    remain = m % k
    total = (num_list[0] * k * max_iter) + (num_list[1] * remain)
    print(total)


max_sum()

# Method_2 -> 좀 비효율적으로 느껴짐
# 책에 있는 방법
# 반복되는 수열을 확인 -> 가장 큰 수가 K번 반복되어 더해지고 그 수에 두번째로 큰 수가 더해짐
# 즉, K+1 수열의 길이가 반복되는 형태로 나타남
# M // (K+1)이 해당 수열이 반복되는 횟수 But 나머지가 나올 수 있음 그만큼 가장 큰 수를 더하면 됨


n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
