import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_summoner():
    name = input("소환사의 닉네임을 입력해주세요: ")
    # 닉네임을 입력하여 정보를 가져오기위한  url
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name

    # 계정 id를 입력하여 정보를 겁색
    # URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account
    # puuid를 입력하여 정보를 검색
    # URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/" + puuid
    # 플레이어의 소환사 아이디를 입력하여 정보를 검색
    # URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/" + id

    # URL에 api키를 보내서 값을 요청
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    result = json.loads(res.text)
    if res.status_code == 200:
        # 코드가 200일때
        print("암호화 아이디 : " + result['id'])
        print("암호화 계정 아이디 : " + result['accountId'])
        print("플레이어 고유 아이디 : " + result['puuid'])
        print("닉네임 : " + result['name'])
        print("소환사 레벨 : " + str(result['summonerLevel']))
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")