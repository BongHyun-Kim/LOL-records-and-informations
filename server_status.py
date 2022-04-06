import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_status():
    URL = "https://kr.api.riotgames.com/lol/status/v3/shard-data"
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        # 코드가 200일때
        print(res.text)
    else:
        # 코드가 200이 아닐때(플랫폼 상태를 알 수 없을때)
        print("서버의 상태를 알 수 없습니다.")