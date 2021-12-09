import requests
import json
from requests.models import HTTPError
from datetime import datetime


KEY = r"F5F683EB356F24EE2AAC4CB527064B1E"
PATH = r'./games/'
site = r"http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v1"

MAX_TRY = 2


def get_matches_by_sequence_number(seq_number):
    url = site + r'?key=' + KEY + '&start_at_match_seq_num=' + str(seq_number)
    n = 1
    while n < MAX_TRY:
        r = requests.get(url)
        if r.ok:
            return r.json()
        else:
            print(f"Code: {r.status_code}, {n} th try")
            n += 1
    raise ValueError("max try reached")

def is_ad_game(game):
    return game['game_mode']==18


def save_game_as_json(game):
    name = str(game['match_seq_num'])
    with open(PATH + name + ".json", 'w+') as f:
        json.dump(game, f)


def get_ad_games(r_json):
    tmp = r_json['result']['matches']
    tmp = [a for a in tmp if is_ad_game(a)]
    return tmp


def fetch_ad_games_by_sequence_number(seq_number):
    r_json = get_matches_by_sequence_number(seq_number)
    games = get_ad_games(r_json)
    for g in games:
        save_game_as_json(g)
    return len(games)


def save_by_seq(seq, name='tmp.json'):
    r_json = get_matches_by_sequence_number(seq)
    with open('./'+name, 'w') as f:
        json.dump(r_json, f, indent=4)


def save_cur_seq_num(num):
    with open("./current_seq_num", 'w') as f:
        f.write(str(num))


def read_cur_seq_num():
    with open("./current_seq_num", 'r') as f:
        s = f.readline()
    return int(s)


def get_time_of_game(seq_number):
    r_json = get_matches_by_sequence_number(seq_number)
    games = get_ad_games(r_json)
    game = games[0]
    return game["start_time"]