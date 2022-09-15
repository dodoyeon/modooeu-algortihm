# Ch2. 재귀 호출 Recursion

# 4. 재귀호출 없이 팩토리얼 구현하기
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
# print(i_fact(5))

# 연습문제 4-1
def i_sum(n):
    if n <= 0:
        return 1
    return n+i_sum(n-1)

# 4-2 (o)
def i_max(l, m):
    if len(l) == 0:
        return m
    if m < l[0]:
        m = l[0]
    return i_max(l[1:], m)

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(i_max(v,0))

# 5. 최대공약수 구하기
def GCD(a,b):
    m = min(a,b)
    for i in range(m):
        if a%m==0 and b%m==0:
            return m
        else:
            m -= 1

# 유클리드 알고리즘 : a 와 b 의 최대공약수는 b와 a를 b로나눈 나머지의 최대공약수와 같다.
def euclid_GCD(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    if a>b:
        a=a%b
    else:
        b=b%a
    return euclid_GCD(a,b) # 굳이 이럴 필요가 없어어어어ㅓ

def re_euclid_GCD(a,b):
    if b == 0:
        return a
    return re_euclid_GCD(a,b%a)

# 연습문제 5-1 (x)
def fibonacci(n,m,prev_m):
    if n == 0:
        return m
    temp = m
    m += prev_m
    prev_m = temp
    return fibonacci(n-1,m,prev_m)

# print(fibonacci(7,1,0))
# print(fibonacci(10,1,0))

def book_fibo(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    return book_fibo(n-1)+book_fibo(n-2)
# print(fibo(7))
# print(fibo(10))

# 6. 하노이 탑 옮기기
def hanoi(n):
    if n == 1:
        return 1
    return 1+2*hanoi(n-1)
# print(hanoi(3))

def hanoi_simul(n, from_pos, to_pos, temp_pos):
    if n == 1:
        print(from_pos,'->',to_pos)
        return

    hanoi(n-1, from_pos, temp_pos, to_pos)
    print(from_pos,'->',to_pos)

    hanoi(n-1, temp_pos, to_pos, from_pos)
