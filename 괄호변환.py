# p가 빈 문자열 일 경우 그대로 리턴
# 1. p를 '(' 와 ')' 의 개수가 같은 u, 그 나머지인 v로 분리
# 2-1. u가 닫힌 괄호일 경우
#     1번으로 돌아가 p에 v를 넣어(=solution(v)) 결과 받기
#     (u+위의 결과) 리턴
# 2-2. u가 닫힌 괄호가 아닐 경우
#     '1번으로 돌아가 p에 v를 넣은(=solution(v)) 결과 임시 저장
#     u의 앞뒤 문자를 제거하고 남은 모든 괄호를 뒤집는다( '('는 ')'로 )
#     "(" + v + ")" + 뒤집은 결과 를 리턴

def split_string(string):
    cnt = 0
    is_perfect = True
    for i in range(len(string)):
        if string[i] == "(":
            cnt += 1
        elif string[i] == ")":
            cnt -= 1
        if cnt < 0:
            is_perfect = False
        if cnt == 0:
            return string[:i+1], string[i+1:], is_perfect

def change_u(string):
    for i in range(0, len(string)):
        if string[i] == "(":
            string = string[:i] + ")" + string[i+1:]
        elif string[i] == ")":
            string = string[:i] + "(" + string[i+1:]
    return string[1:-1]
    

def solution(p):
    answer = ""
    if p == "":
        return answer
    u, v, u_is_perfect = split_string(p)
    if u_is_perfect == True:
        answer += u
        p = solution(v)
        answer += p
        return answer
    else:
        p = solution(v)
        return "(" + p + ")" + change_u(u)

print(solution("()))((()"))

            


            