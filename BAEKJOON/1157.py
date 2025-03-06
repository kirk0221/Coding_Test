words = str(input()).upper()
word_list = list(set(words))
cnt = []

for i in word_list:
    count = words.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])