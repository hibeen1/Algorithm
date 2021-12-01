s = input()
s = sorted(s)
is_string = []
is_number = []
for i in s:
    if i.isdigit() == True:
        is_number.append(int(i))
    else:
        is_string.append(i)
is_string.sort()
s = ''.join(is_string)
if len(is_number) == 0:
    print(s)
else:
    print(s+str(sum(is_number)))
