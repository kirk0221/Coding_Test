n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(list(set(x)))
dict_x = {}

for i in range(len(sorted_x)):
    dict_x[sorted_x[i]] = i

for i in x:
    print(dict_x[i], end = ' ')

'''
풀이과정 설명
list의 index는 시간복잡도가 O(n)
시간을 줄이기 위해 딕셔너리를 사용하여 정렬된 리스트의 값을 키로, 인덱스를 값으로 하여 O(1)로 시간복잡도를 줄임
'''

# 생각 방법 2

# n = int(input())
# x = list(map(int, input().split()))
# sorted_x = sorted(list(set(x)))
# for i in x:
#     print(sorted_x.index(i), end = ' ')


# 생각 방법 1

# n = int(input())
# x = list(map(int, input().split()))
# sorted_x = sorted(list(set(x)))
# for i in x:
#     for j in sorted_x:
#         if i == j:
#             print(sorted_x.index(j), end= ' ')
