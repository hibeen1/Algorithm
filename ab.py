def solution(start_date, end_date, login_dates):
    answer = -1
    temp = [int(start_date[:2]), int(start_date[3:5]), start_date[6:]]
    end = [int(end_date[:2]), int(end_date[3:]), -1]
    what_day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    index = what_day.index(temp[2])
    arr = []
    while True:
        is_full = False
        print(temp)
        print(end_date)
        if temp[0] == end[0] and temp[1] == end[1]:
            end[2] = temp[2]
            break
        if index == 6:
            index = 0
        else:
            index += 1
        temp[2] = index
        
        if temp[0] == 12 and temp[1] == 31:
            temp[0], temp[1] = 1, 1
            arr.append((temp[0], temp[1]))
            continue
        else:
            if temp[0] == 2:
                if temp[1] == 28:
                    temp[0] += 1
                    is_full = True
                else:
                    pass
            elif temp[0] == 1 or temp[0] == 3 or temp[0] == 5 or temp[0] == 7 or temp[0] == 8 or temp[0] == 10 or temp[0] == 12:
                if temp[1] == 31:
                    temp[0] += 1
                    is_full = True
                else:
                    pass
            elif temp[0] == 4 or temp[0] == 6 or temp[0] == 9 or temp[0] == 11:
                if temp[1] == 30:
                    temp[0] += 1
                    is_full = True
                else:
                    pass
            if is_full:
                temp[1] = 1
                is_full = False
            else:
                temp[1] += 1
            if not (index == 5 or index == 6):
                arr.append((temp[0], temp[1]))

    login = []
    for i in login_dates:
        login.append((int(i[:2]), int(i[3:])))
    login.sort()
    idxs = []
    for i in login:
        for j in range(len(arr)):
            if i == arr[j]:
                idxs.append(j)
    cnt = 1
    for i in range(1, len(idxs)):
        if idxs[i-1] + 1 == idxs[i]:
            cnt += 1
        else:
            cnt = 1
        answer = max(answer, cnt)
    return answer

print(solution("05/04 MON", "05/30", ["05/26", "05/25", "05/27", "05/10", "05/11", "05/23", "05/22", "05/21", "05/06", "05/09", "05/07", "05/08"]))