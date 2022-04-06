import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_account():
    name = input("소환사의 닉네임을 입력해주세요: ")
    country = input("소환사의 활동 서버를 입력해주세요")
    # 닉네임을 입력하여 정보를 가져오기위한  url
    URL = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + name + "/" + country

    # 플레이하는 게임과 고유 아이디를 입력하여 검색
    # URL = "https://asia.api.riotgames.com/riot/account/v1/active-shards/by-game/" + game + "/by-puuid/" + puuid
    # 고유 아이디를 입력하여 정보를 검색
    # URL = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-puuid/" + puuid

    # URL에 api키를 보내서 값을 요청
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    result = json.loads(res.text)
    if res.status_code == 200:
        # 코드가 200일때
        print("고유 아이디 : " + result['puuid'])
        print("닉네임 : " + result['gameName'])
        print("서버 : " + result['tagLine'])
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")
