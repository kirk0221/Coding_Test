n = int(input())
ans = 0
chat_set = set()
for _ in range(n):
    chat = input()
    if chat == "ENTER":
        chat_set.clear()
    elif chat not in chat_set:
        ans+=1
        chat_set.add(chat)
print(ans)