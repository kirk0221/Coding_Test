# def merge_sort(x):
#     if len(x) < 2: # 2보다 작으면 리스트 값을 그대로 반환 -> 1개만 남았을 때
#         return x
#     mid = len(x)//2 # 중앙으로 나눠서 문제 해결 -> 분할 정복
#     x_l = merge_sort(x[:mid]) # 앞쪽 리스트 해결
#     x_h = merge_sort(x[mid:]) # 뒤쪽 리스트 해결
#     merged_arr = [] # 병합할 리스트
#     l = h = 0 # 리스트의 길이를 저장하기 위한 변수
#     while l < len(x_l) and h < len(x_h): # 리스트 길이만큼 반복
#         if x_l[l] < x_h[h]: # 앞쪽 리스트의 l번째 값이 뒤쪽 리스트의 h번째 값보다 작은지 확인 -> 더 작은값을 리스트에 저장히기 위해
#             merged_arr.append(x_l[l])
#             l += 1 # 리스트에서 다음으로 큰 값과 비교하기 위해 더해줌
#         else:
#             merged_arr.append(x_h[h])
#             h += 1
#     # 남은 숫자를 전부 다 넣어주기 위해 사용
#     merged_arr += x_l[l:]
#     merged_arr += x_h[h:]
#     return merged_arr

import sys

n = int(input())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l = sorted(l)
for i in range(n):
    print(l[i])

"""
input() 이 sys.stdin.readline() 보다 느린 이유 :

input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,

개행 문자를 삭제한 값을 리턴하기 때문에 느리다.

 

 

input() 과 sys.stdin.readline() 의 차이점 :

일단 sys.stdin.readline()과 input()은 같은 역할을 하지 않는다.
input() 내장 함수는 parameter로 prompt message를 받을 수 있다

따라서 입력받기 전 prompt message를 출력해야 한다

물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다

 

하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다

즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다

반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 이 때문에 조금 귀찮은 점이 있기도 하다.
"""
