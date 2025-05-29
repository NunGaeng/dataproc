import json

from match_data2 import to_extract

with open("match_0.json", "r", encoding="utf-8") as f:
    data_match = json.load(f)

with open("timeline_0.json", "r", encoding="utf-8") as f:
    data_timeline = json.load(f)

timeline = data_timeline[0]['info']
match = data_match[0]['info']

players = match['participants']
blue_team = {}
red_team = {}
for p in players:
    teamId = p['teamId']
    teamPosition = p['teamPosition']
    pid = p['participantId']
    if teamId == 100:
        blue_team[pid] = teamPosition
    else:
        red_team[pid] = teamPosition
    print(f'teamId = {teamId}, teamPosition = {teamPosition}, pid = {pid}')
print(f'blue_team : {blue_team}')
print(f'red_team : {red_team}')

# TO DO
# minutes = [0, 1, 2, 3, 4, 5, ..., 20]
# blue_score = [x1, x2, x3, x4, ..., x20] <- 20개(분단위 수)의 원소를 갖는 리스트
# red_score = [y1, y2, y3, y4, ..., y20] <- 20개의 원소를 갖는 리스트
# timeline에서 frames를 순회하면서, for frame in timeline['frames']
# frame에서 ParticipantsFrames를 순회 for pframe in frame['ParticipantsFrames']
# pframe은 모두 딕셔너리인데 여기의 키 값("1", "2", ..)으로 blue / red를 구분하여 합을 구한다.

minutes = []
blue_score = []
red_score = []
diff = []
to_extract = 'totalGold'
position = 'MIDDLE'
frames = timeline['frames']
for frame in frames:
    time = frame['timestamp'] // 60000
    minutes.append(time)
    blue_score_1min, red_score_1min = 0, 0
    diff_1min = 0
    for pid, item in frame['participantFrames'].items():
        if int(pid) in blue_team:
            if blue_team[int(pid)] == position:
                blue_score_1min += item[to_extract]
            print(f'time={time:2d}, pid={pid:2s}, team=blue, score={item[to_extract]}')
        else:
            if red_team[int(pid)] == position:
                red_score_1min += item[to_extract]
            print(f'time={time:2d}, pid={pid:2s}, team=red, score={item[to_extract]}')

        diff_1min = blue_score_1min - red_score_1min
    print(f'blue = {blue_score_1min}, red = {red_score_1min}\n')
    blue_score.append(blue_score_1min)
    red_score.append(red_score_1min)
    diff.append(diff_1min)


print(minutes)
if minutes[-1] == minutes[-2]:
    minutes[-1] = minutes[-2] + 1
print(minutes)
print(blue_score)
print(red_score)

import matplotlib.pyplot as plt

plt.plot(minutes, blue_score, label=f"Blue[{position}] {to_extract}", marker = 'o', linewidth=2)
plt.plot(minutes, red_score, label=f"Red[{position}] {to_extract}", marker = 'o', linewidth=2)

plt.xlabel('Minutes (m)')
plt.ylabel(f"{to_extract}")
plt.title(f'Feature {to_extract} Graph, Position = {position}')
plt.legend()
plt.grid(True)
plt.show()

# blue_score와 red_score의 차이를 그래프로 그려봅시다
plt.figure()

diff = []
for j in range(len(minutes)):
    diff.append(blue_score[j] - red_score[j])
print(diff)
plt.plot(minutes, diff, marker = 'o', linewidth=2)
plt.show()