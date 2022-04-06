import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_clash():
    # 플레이어의 정보 중 ID값을 가져오기 위해 플레이어의 전체 정보를 불러옴.
    name = input("소환사의 닉네임을 입력해주세요: ")
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})

    # 가져온 데이터를 딕셔너리 타입으로 변환하고 필요한 id값만 추출
    result = json.loads(res.text)
    id = result['id']

    # 닉네임을 입력하여 정보를 가져오기위한  url
    URL2 = "https://kr.api.riotgames.com/lol/clash/v1/players/by-summoner/" + id

    # 팀 아이디로 팀 정보 검색
    # URL = "https://kr.api.riotgames.com/lol/clash/v1/teams/" + team_id
    # 서버 별 격정 정보 검색
    # URL = "https://kr.api.riotgames.com/lol/clash/v1/tournaments"
    # 팀 아이디로 격전 정보 검색
    # URL = "https://kr.api.riotgames.com/lol/clash/v1/tournaments/by-team/" + team_id
    # 격전 아이디로 격전 정보 검색
    # URL = "https://kr.api.riotgames.com/lol/clash/v1/tournaments/" + tournaments_id

    # URL에 api키를 보내서 값을 요청
    res2 = requests.get(URL2, headers={"X-Riot-Token": api_key})
    result2 = json.loads(res2.text)
    if res2.status_code == 200:
        # 코드가 200일때
        if len(result2) == 0:
            print("플레이한 격전 정보가 없습니다.")
        else:
            print(result2)
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")