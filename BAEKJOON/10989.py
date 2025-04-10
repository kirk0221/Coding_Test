import sys
n = int(sys.stdin.readline())
l = [0] * 10001
for _ in range(n):
    l[int(sys.stdin.readline())]+=1

for i in range(len(l)):
    if l[i] != 0:
        for _ in range(l[i]):
            sys.stdout.write(f"{i}\n")


'''
1. sys.stdin.readline()이 속도가 더 빠르다
    sys.stdin.readline()
        - 입력값을 무조건 문자열로 받음
    input()
        - 입력으로 들어온 값을 evaluate해서 값에 맞는 자료형으로 자동 초기화
        - parameter로 prompt message를 출력(없더라도 출력여부 확인을 하기에 부하로 작용)
        - return값에 개행 문자(\n)을 삭제

2. Counting Sort 사용
    주어진 수의 범위가 작은 경우 빠름
    최댓값과 입력 배열의 원소 값 개수를 누적합으로 저장하는 배열을 사용
    동작 방식
        1) 입력 배열의 최댓값 길이의 Counting Array 생성
        2) 입력 배열의 원소 값를 Counting Array의 해당 원소 index에 누적합
        3) Counting Array의 index에 해당하는 원소값을 출력

3. sys.stdout.write() 사용
    sys.stdout.write()
        - 문자열로 작성
        - 개행 문자 직접 입력
    print()
        - 개행 문자를 자동 삽입하여 느림 

'''

# 메모리초과

# import sys
# n = int(input())
# l = []
# for _ in range(n):
#     l.append(int(sys.stdin.readline()))
# l = sorted(l)
# for i in range(n):
#     print(l[i])