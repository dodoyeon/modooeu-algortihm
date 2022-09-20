# 7. 순차 탐색(sequential search) : list 안의 요소를 순차적으로 비교하며 탐색
def seq_search(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1

# a = [17, 92, 18, 33, 58, 5, 33, 42]
# print(seq_search(a, 900))
# print(seq_search(a, 33)) # 중복이 있을경우 첫번째 나온 위치만 리턴한다.
# print(seq_search(a, 92))

# 연습문제
# 7-1
def seq_search(l, x):
    ans = []
    for i in range(len(l)):
        if l[i] == x:
            ans.append(i)
    return ans # 7-2 : 똑같이 O(n) 복잡도를 가질듯.

#7-3
def num_name(num, name, x):
    for i in range(len(name)):
        if num[i] == x:
            return name[i]
    return '?'

def dict_numname(num, name):
    return
a = [39, 14, 67, 105]
b = ['just', 'john', 'mike', 'summ']
# print(num_name(a,b, 39))

# 8. 선택정렬 (selection sort)
def sel_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(i+1, n):
            if l[j] > l[i]:
                l[j], l[i] = l[i], l[j]
    return l

# l = [2, 4, 5, 1, 3]
# print(sel_sort(l))

# 9. 삽입 정렬 (Insertion Sort)
def ins_sort(l):
    n = len(l)
    new_l = [l[0]]
    for i in range(1, n):
        for j in range(len(new_l)):
            if l[i] < new_l[j]: # and l[i] <= new_l[j+1]
                new_l.insert(j, l[i])
                break
        if new_l[-1] < l[i]:
            new_l.append(l[i])
    return new_l

def book_insort(l):
    n = len(l)
    for i in range(1, n):
        m = l[i]
        j = i-1
        while j >= 0 and l[j] >m:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = m

# l = [2, 4, 5, 1, 3, 4]
# print(ins_sort(l))
# book_insort(l)
# print(l)

# 10. 병합 정렬 (Merge Sort) : 재귀 사용
def mer_sort(l):
    n = len(l)
    if n <= 1: # merge sort 함수 종료조건
        return l
    key = n//2
    l1 = mer_sort(l[:key])
    l2 = mer_sort(l[key:])

    result = [] # 2개 list 합칠 때 (merge)
    while l1 and l2:
        if l1[0] > l2[0]:
            result.append(l2.pop(0))
        else:
            result.append(l1.pop(0))

    while l1:
        result.append(l1.pop(0))
    while l2:
        result.append(l2.pop(0))
    return result

def book_mergesort(l):
    n = len(l)
    if n <= 1:
        return # l -> return 을 하지 않는다

    key = n//2
    l1=l[:key]
    l2=l[key:]
    book_mergesort(l1)
    book_mergesort(l2)

    idx1, idx2, idx_l = 0,0,0
    n1 = len(l1)
    n2 = len(l2)
    while idx1 < n1 and idx2 < n2:
        if l1[idx1] > l2[idx2]:
            l[idx_l] = l2[idx2]
            idx_l +=1
            idx2 +=1
        else:
            l[idx_l] = l1[idx1]
            idx_l += 1
            idx1 += 1

    while idx1 < n1:
        l[idx_l] = l1[idx1]
        idx_l += 1
        idx1 += 1

    while idx2 < n2:
        l[idx_l] = l2[idx2]
        idx_l += 1
        idx2 += 1

l = [6,8,3,9,10,1,2,4,7,5,4]
# print(mer_sort(l))
# book_mergesort(l)
# print(l)

# 11. 퀵 정렬 (Quick Sort)
def quick_sort(l):
    n = len(l)
    if n <= 1:
        return
    pivot = l[-1]
    l1, l2=[],[]
    for i in range(n-1):
        if l[i]<=pivot:
            l1.append(l[i])
        else:
            l2.append(l[i])
    return quick_sort(l1)+[pivot]+quick_sort(l2)

def book_quick(l, start, end):
    if (end-start) <= 0:
        return
    pivot = l[end]
    i = start
    for j in range(start, end):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[end] = l[end], l[i]
    book_quick(l, start, i-1)
    book_quick(l, i+1, end)

def book_quicksort(l):
    book_quick(l, 0, len(l)-1)

# print(quick_sort(l))
# book_quicksort(l)
# print(l)

# 12. 이분 탐색 (Binary Search)
def bin_search(l,x):
    start = 0
    end = len(l)-1
    while start <= end:
        n = (end+start) // 2
        if x == l[n]:
            return n
        elif x > l[n]:
            start = n+1
        else:
            end = n-1
    return -1

d = [1,4,9,16,25,36,49,64,81]
# print(bin_search(d, 36))
# print(bin_search(d, 50))