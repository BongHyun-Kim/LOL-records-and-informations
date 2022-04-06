import requests
import json

api_key = "RGAPI-106f4a35-1008-4489-9f38-80c37709b87d"

selection = 0

def get_all_league():

    print("입력 할 수 있는 큐는 다음 예시와 같습니다.")
    print("RANKED_SOLO_5x5\nRANKED_TFT\nRANKED_FLEX_SR\nRANKED_FLEX_TT")
    queue = input("큐를 입력해주세요 : ")

    print("입력 할 수 있는 티어는 다음 예시와 같습니다.")
    print("IRON\nBRONZE\nSILVER\nGOLD\nPLATINUM\nDIAMOND\nMASTER\nGRANDMASTER\nCHALLENGER")
    tier = input("티어를 입력해주세요 : ")

    print("입력할 수 있는 랭크는 다음 예시와 같습니다.")
    print("I\nII\nIII\nIV")
    division = input("랭크를 입력해주세요 : ")

    URL = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/" + queue + "/" + tier + "/" + division + "/page=1"
    res = requests.get(URL, headers={"X-Riot_Token": api_key})

    if res.status_code == 200:
        # 코드가 200일때
        print(res.text)
    else:
        # 코드가 200이 아닐때(경쟁전 정보가 없을때)
        print("검색하신 경쟁전 정보가 없습니다.")