import sys
input = sys.stdin.readline

def nqueen(depth):     
  global result
  
  if depth == n : 
    result += 1 
    return 
  
  for i in range(n):
      chess[depth] = i
      if check(depth):
        nqueen(depth + 1)

def check(n):
  for i in range(n):
    if (chess[n] == chess[i]) or (abs(n-i) == abs(chess[n] - chess[i])):
      return False
  return True

n = int(input())
result = 0
chess = [0]*n
nqueen(0)
print(result)