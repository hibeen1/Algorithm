n = int(input())
first_door = bool(int(input()))

if n > 5:
    print("Love is open door")
else:
    for i in range(n-1):
        first_door = not first_door
        print(int(first_door))
