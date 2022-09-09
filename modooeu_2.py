# Ch2. 재귀 호출

# 재귀호출 없이 팩토리얼 구현하기
def fact(n):
    out=1
    for i in range(1,n+1):
        out *= i
    return out

# 재귀호출 시
def i_fact(n):
    if n <= 1:
        return 1
    return n*i_fact(n-1)

print(i_fact(5))

# 연습문제 1
def i_sum(n):
    if n <= 0:
        return 1
    return n+i_sum(n-1)

# 연습문제 2
def i_max(l):

    return