import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_mastery():
    # 플레이어의 정보 중 ID값을 가져오기 위해 플레이어의 전체 정보를 불러옴.
    name = input("소환사의 닉네임을 입력해주세요: ")
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})

    # 가져온 데이터를 딕셔너리 타입으로 변환하고 필요한 id값만 추출
    result = json.loads(res.text)
    id = result['id']

    # json url에 정보를 얻어올 id를 입력하고 데이터를 불러옴
    URL2 = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id

    # 암호화된 아이디와 챔피언아이디로 챔피언 숙련도를 검색
    # URL2 = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + "/by-champion/" + champ_id
    res2 = requests.get(URL2, headers={"X-Riot-Token": api_key})
    if res2.status_code == 200:
        # 코드가 200일때
        print(res2.text)
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")