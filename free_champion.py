import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_free_champion():
    URL = "https://kr.api.riotgames.com/lol/platform/v3/champion-rotations"
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        # 코드가 200일때
        print(res.text)
    else:
        # 코드가 200이 아닐때(무료인 챔피언이 없을때)
        selection("무로료 사용할 수 있는 챔피언이 없습니다.")