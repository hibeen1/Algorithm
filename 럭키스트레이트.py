n = input()
front = 0
end = 0
length = len(n)
for i in range(int(length / 2)):
    front += int(n[i])
    end += int(n[length - i - 1])
if front == end:
    print("LUCKY")
else:
    print("READY")