import numpy as np

# from numpy.core.defchararray import endswith
import pandas as pd
import os
import json 
from collections import defaultdict
from const import *

abnormal_abs = defaultdict(lambda: 0)
non_ult_abs = set()



def ab_is_bonus(ab_id, id2ab):
    """
    Check if the ability is a bonus ability
    """
    id = str(ab_id)
    if id2ab.get(id) is None or id2ab[id][0:7] == 'special' or id2ab[id][0:10] == 'ad_special':
        return True
    else:
        return False

def correct_id(ab_id):
    """
    Recast the ability id. There are abilities with multiple ids, this function recasts them to a single id.
    See ab_id_recast in const.py for the recastings.
    """
    tmp = ab_id_recast.get(ab_id)
    if tmp is None:
        return ab_id
    else:
        return tmp


def get_abs(player):
    if player.get('ability_upgrades') is None:
        return []
    
    id_seq = [a['ability'] for a in player['ability_upgrades']]
    # for i in range(3):
    #     non_ult_abs.add(int(id_seq[i]))

    all_ids = set(id_seq)
    ab_ids = [correct_id(a) for a in all_ids if not ab_is_bonus(a, id2ab)]
    ab_ids = list(set(ab_ids))

    if len(ab_ids) > 4:
        print([id2ab[str(k)] for k in ab_ids])
        for ab in ab_ids:
            abnormal_abs[ab] += 1
        raise ValueError

    return ab_ids


def get_hero(player):
    return player["hero_id"]


def has_abandon(game):
    assert len(game['players']) == 10
    for i in range(10):
        if game['players'][i]['leaver_status'] > 1:
            return True
    return False

def summarize_match_ids_to_file(games_folder, out_folder="./"):
    """
    Summarize match ids of json files in the games_folder to a file in out_folder
    """
    filename_list = os.listdir(games_folder)
    n_file = len(filename_list)
    print("Summarizing a total of ", n_file, " files...")
    out_file_name = "match_ids"
    match_ids = np.zeros((n_file,), dtype=np.uint64)
    for i, name in enumerate(filename_list):
        with open(games_folder + name, 'r', encoding='utf-8') as f:
            game = json.load(f)
        match_ids[i] = game['match_id']
        if i % 10000 == 0:
            print(f"{i}")
    filename = out_folder + out_file_name
    # match_ids.tofile(filename)
    np.savetxt(filename, match_ids, fmt='%d')



def summarize_games_to_csv(games_folder, out_folder="./data/", max_file=1000):
    """
    Summarize json files in the games_folder to a csv file in out_folder
    """
    filename_list = os.listdir(games_folder)
    n_file = min(len(filename_list), max_file)
    
    x_headers = []
    for i in range(10):
        x_headers.append(f"hero{i}")
        for j in range(4):
            x_headers.append(f"ab{i}{j}")
    d = dict()
    shape = (n_file,)
    for h in x_headers:
        d[h] = np.zeros(shape, dtype=np.uint16)
    d["radiant_win"] = np.zeros(shape, dtype=np.bool)
    d["has_abandon"] = np.zeros(shape, dtype=np.bool)
    d["match_seq_num"] = np.zeros(shape, dtype=np.uint64)
    d["match_id"] = np.zeros(shape, dtype=np.uint64)
    d["start_time"] = np.zeros(shape, dtype=np.uint64)
    d["duration"] = np.zeros(shape, dtype=np.uint16)
    d["lobby_type"] = np.zeros(shape, dtype=np.int8)
    d["bugged"] = np.zeros(shape, dtype=np.bool)
    
    for i, name in enumerate(filename_list[:n_file]):
        with open(games_folder + name, 'r', encoding='utf-8') as f:
            game = json.load(f)
        try:
            for j, player in enumerate(game['players']):
                tmp = get_abs(player)
                d[f"hero{j}"][i] = get_hero(player)
                for k, ab in enumerate(tmp):
                    d[f"ab{j}{k}"][i] = ab
            d["radiant_win"][i] = game["radiant_win"]
            d["match_seq_num"][i] = game["match_seq_num"]
            d["match_id"][i] = game["match_id"]
            d["start_time"][i] = game["start_time"]
            d["duration"][i] = game["duration"]
            d["lobby_type"][i] = game["lobby_type"]
            d["has_abandon"][i] = has_abandon(game)
        except:
            print(game["match_id"])
            d["bugged"][i] = True
            continue
        if i%1000 == 0:
            print(i)
    
    df = pd.DataFrame.from_dict(d)
    df.to_csv(out_folder + "games.csv")



# game_folder = "D:\\tmp\\50[29500702-45666065]\\games\\"
# game_folder = "D:\\tmp\\50[29500702-45666065]\\"
summarize_games_to_csv(game_folder, max_file=1000000)
summarize_match_ids_to_file(game_folder, out_folder="./")

