from sys import stdin

n = int(input())
arr = set()
for _ in range(n):
    temp = stdin.readline().rstrip()
    arr.add((len(temp), temp))

dic = dict()
for i in range(1, max(arr)[0]+1):
    dic[i] = list()

for i in arr:
    dic[i[0]].append(i[1])
    # print(i)

for i in dic.values():
    i.sort()
    for j in i:
        print(j)



# import sys
# word=set()
# for i in range(int(input())):
#     word.add(sys.stdin.readline().rstrip())
# word=list(word)
# word.sort()
# word.sort(key=lambda x:len(x))
# print("\n".join(word))