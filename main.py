import account
import platform_status
import summoner
import league
import mastery
import free_champion
import clash
import server_status
import all_league

# https://developer.riotgames.com/
# 위 링크로 접속하여 로그인한 뒤 얻은 개발 api키를 입력
api_key = "RGAPI-b1170cb8-6b28-4609-894c-454fd80c0cf5"

selection = 0

while(selection != "0"):
    print("\n---------------------------------------------------------------------------------------------------")
    print("0: 종료")
    print("1: 계정 정보 검색")
    print("2: 플레이어 정보 검색")
    print("3: 플레이어의 경쟁전 시즌 정보 검색")
    print("4: 전체 시즌 경쟁전 정보 검색")
    print("5: 플레이어의 챔피언 숙련도 검색")
    print("6: 주간 무료 챔피언 검색")
    print("7: 격전 정보 검색")
    print("8: 서버 상태")
    print("9: 플랫폼 상태")
    print("---------------------------------------------------------------------------------------------------")
    selection = input("번호를 입력해주세요: ")
    print("---------------------------------------------------------------------------------------------------")

    #  계정 정보 가져오기
    if selection == "1":
        account.get_account()

    #  플레이어 정보 가져오기
    elif selection == "2":
        summoner.get_summoner()

    # 플레이어의 시즌 경쟁전 정보 검색
    elif selection == "3":
        league.get_league()

    # 전체 시즌 경쟁전 정보 검색
    elif selection == "4":
        all_league.get_all_league()

    # 플레이어의 챔피언 숙련도 검색
    elif selection == "5":
        mastery.get_mastery()

    # 주간 사용가능한 무료 챔피언 검색
    elif selection == "6":
        free_champion.get_free_champion()

    # 격전 정보 가져오기
    elif selection == "7":
        clash.get_clash()

    # 서버 상태 가져오기
    elif selection == "8":
        server_status.get_status()

    # 서버 플랫폼 상태 가져오기
    elif selection == "9":
        platform_status.get_status()


    elif selection == "0":
        print("검색을 종료합니다")
        break

    else:
        print("잘못된 번호입니다.")
        continue