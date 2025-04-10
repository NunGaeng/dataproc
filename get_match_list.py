import json
import time
import requests

from get_puuid_single_page import API_KEY, HEADERS

API_KEY = "RGAPI-4e5b9804-f600-4965-9f72-da585b285abe"

HEADERS = {"X-Riot-Token" : API_KEY}

#https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/Eyk9_2a_nN5iKMrAP4HcUWU2w1sDr8sa-Cb3_JG67YvpRHYZj5ACsz14jLqSG6_4zusHf04exv_taQ/ids?startTime=1736294400&type=ranked&start=19&count=20&api_key=RGAPI-4e5b9804-f600-4965-9f72-da585b285abe

STARTTIME = "1736294400"
TYPE = "ranked"
COUNT = 100

with open("puuids_over_MASTER_tier.json", 'r' ,encoding='utf-8') as f:
    puuid_data = json.load(f)

print(f"첫 번째 CHALLENGER의 puuid : {puuid_data[0]['CHALLENGER'][0]}")

sample_puuid = puuid_data[0]['CHALLENGER'][0]
print(f"첫 번째 CHALLENGER의 puuid : {sample_puuid}")

# 특정 puuid에 대해서 최근 100개의 Match Id 리스트를 얻어오는 함수
def get_match_list_single_100(puuid):
    base_url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    url = f"{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}"
    responses = requests.get(url, headers=HEADERS)

    if responses.status_code == 200:
        match_list = responses.json()
        return match_list
    else:
        raise Exception(f"Error: {responses.status_code}")

match_list = get_match_list_single_100(sample_puuid)
print(match_list)
print(len(match_list))

def get_match_list_from_puuid(puuid):
    base_url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    match_ids = []
    start_idx = 0
    while True:
        url = f"{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}"
        responses = requests.get(url, headers=HEADERS)
        if responses.status_code == 200:
            match_list = responses.json()
            if not match_list:
                print(f"수집 종료. 현재까지 수집된 Match id 수는 {len(match_ids)}")
                break
            match_ids.extend(match_list)
            start_idx += COUNT
            print(f'현재까지 {len(match_ids)}개의 Match ID 수집 완료')
        elif responses.status_code == 429:
            print(f'사용 한도 초과. 10초 대기')
            time.sleep(10)
        else:
            print(f'요청 실패 : {responses.status_code}')
            break
        time.sleep(0.1)
    return match_ids
match_ids = get_match_list_from_puuid(sample_puuid)
print(match_ids, len(match_ids))