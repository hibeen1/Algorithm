import copy

def ssafy(n, array):
    result = 0
    for i in range(n):
        cnt = 0
        array2 = copy.deepcopy(array)
        array2[i] = 0
        for j in range(n):
            print(sum(array2[:j+1]), end=' ')
            if sum(array2[:j+1]) == 0:
                cnt += 1
        result = max(result, cnt)
        print()
    return result
    

print("답 : ", ssafy(5, [2,2,-1,1,-2]))

        
