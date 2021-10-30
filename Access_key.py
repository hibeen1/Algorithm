import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '9478d7a269c38ad19ae6d23805065eac'
redirect_uri = 'http://127.0.0.1:8000'
authorize_code = 'CePb9j1RNUL-H_wYHYaByTr__mRsfQhIjmg_Qak9SsJrveM2_qbNnMAC08EqlKDswXHesgopyV8AAAF80CuBVA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# # json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)


# with open("kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])