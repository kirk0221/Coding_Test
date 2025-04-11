n = int(input())
n_set = set()
for _ in range(n):
    name, state = input().split()
    if state == "enter":
        n_set.add(name)
    elif state == "leave":
        n_set.remove(name)
sorted_set = sorted(n_set)
for i in range(len(sorted_set)):
    print(sorted_set.pop())