n, m = map(int, input().split())
dogam_name = dict()
dogam_num = dict()
for i in range(n):
    name = input()
    dogam_num[i+1] = name
    dogam_name[name] = i+1
for j in range(m):
    user_input = input()
    try:
        user_input = int(user_input)
        print(dogam_num[user_input])
    except:
        print(dogam_name[user_input])