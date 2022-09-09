import math

# 들어가며
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

def abs_square(a):
    return math.sqrt(a**2)

# print(abs_sign(-3), abs_square(-3))

# 1
def n_sum(n):
    a = n//2
    b = n%2
    if b == 1:
        return a*(n+1) +(n+1)//2
    else:
        return a*(n+1)

def n_ssum(n): # 정답 ㅠㅜ
    return n*(n+1)//2

# print(n_ssum(100))
# print(n_sum(100))

# 연습문제 1-1
def sq_sum(n):
    out = 0
    for i in range(1,n+1):
        out += i**2
    return out

# 1-2
'''O(n)'''
#1-3
'''O(n^(3)) 아냐?..O(1)인가ㅠㅜ'''

# 2
def n_max(l):
    m=l[0]
    for i in l[0:]:
        if m < i:
            m=i
    return m

def index_max(l):
    # m=l[0]
    index=0
    for i in range(len(l)):
        if l[i]>l[index]:
            index=i
    return index

# a=[2,34,52,3,22,60,3]
# print(n_max(a))
# print(index_max(a))
# print(max(a))

# 연습문제
def i_min(l):
    m = l[0]
    for i in l[1:]:
        if m > l[i]:
            m=l[i]
    return m

# 3
def dongmung(l):
    n = len(l)
    res = []
    for i in range(n): # n-1이 낫다!
        for j in range(i+1, n):
            if l[i]==l[j]:
                res.append(l[i])
    return res

a=['tom', 'robert', 'bert', 'sara', 'jw', 'tom']
print(dongmung(a))

# 연습문제
def jjack(l):
    jj=[]
    n = len(l)
    for i in range(n):
        for j in range(i+1,n):
            jj.append([l[i],l[j]])
    return jj

'''O(1), O(n), O(n**2), O(n^4)'''