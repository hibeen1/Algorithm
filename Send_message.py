import requests
import json

#2.
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"안뇽?",
        "link":{
            "web_url":"응?"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)