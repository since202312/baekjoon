# https://www.acmicpc.net/problem/2309
#
# Q:
# 아홉 난쟁이의 키가 주어졌을 때, 키의 합이 100인 일곱 난쟁이의 키를 찾으시오.
#
#
# Input:
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
# 주어지는 키는 100을 넘지 않는 자연수이며,
# 아홉 난쟁이의 키는 모두 다르며,
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
#
#
# Output:
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
#
# Example:
# in:
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
#
# out:
# 7
# 8
# 10
# 13
# 19
# 20
# 23

def answer():
    l = []
    for i in range(9):
        l.append(int(input()))

    l.sort()
    s = sum(l)

    for i in range(8):
        for j in range(i + 1, 9):
            if 100 == s - l[i] - l[j]:
                l.pop(j)
                l.pop(i)
                break
        if len(l) == 7:
            break

    for i in l:
        print(i)


if __name__ == '__main__':
    answer()