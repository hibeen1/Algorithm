# def solution(s):
#     answer = s
#     new_s =""
#     for unit in range(1, len(s) // 2 + 1):
#         cnt = 1
#         temp = 0
#         while temp < len(s):
#             if s[temp : temp + unit] == s[temp + unit : temp + unit + unit]:
#                 cnt += 1
#                 temp += unit
#                 print(cnt)
#                 continue
#             if cnt == 1:
#                 new_s = new_s + s[temp : temp + unit]
#                 print("1이당!", new_s)
#             if cnt > 1:
#                 new_s = new_s + str(cnt) + s[temp:temp + unit]
#                 cnt = 1
#                 print("슬라이싱이 ", unit,"일 때, ", "new_s :", new_s) 
#             temp += unit
#         if len(new_s) <= len(answer):
#             answer = new_s 
#         new_s = ''
#         print("슬라이싱 :", unit,"답 :", answer)
#     return len(answer)
# # aabbaccc
# # print(9//2 + 1)
# print(len(solution("abcabcabcabcdededededede")))



# def solution(s):
#     answer = len(s)
#     for step in range(1, len(s) // 2 + 1):
#         compressed = ""
#         prev = s[0:step]
#         count = 1
#         for j in range(step, len(s), step):
#             if prev == s[j:j + step]:
#                 count += 1
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j + step]
#                 count = 1
#         compressed += str(count) + prev if count >= 2 else prev
#         answer = min(answer, len(compressed))
#     return answer


s = "1234567890"
print("hello" + s[11:15] + "hehe")