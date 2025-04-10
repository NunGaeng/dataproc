import json

with open("puuids_over_MASTER_tier.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print("CHALLENGER의 첫 번째 puuid")
print(data[0]["CHALLENGER"][0])