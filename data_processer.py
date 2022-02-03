from const import *
import pandas as pd
import numpy as np
from itertools import product
import pickle as pkl

df = pd.read_csv("./data/games.csv")
df = df.loc[df.bugged==False].loc[df.has_abandon==False].reset_index()

def re_index(cat_data):
    idx2id = np.sort(np.unique(cat_data))
    id2idx = {}

    for idx, id in enumerate(idx2id):
        id2idx[id]= idx 
        
    f = np.vectorize(lambda x : id2idx[x])
    new_data = f(cat_data)
    return new_data, idx2id, id2idx

tmp_hero = df[[f"hero{i}" for i in range(10)]].to_numpy()
tmp_ab = df[[f"ab{i}{j}" for i, j in product(range(10), range(4))]].to_numpy()

match_ids = df["match_id"]

X_ab, ab_id2idx, ab_idx2id = re_index(tmp_ab)
X_hero, hero_id2idx, hero_idx2id = re_index(tmp_hero)

X_ab = X_ab.reshape(-1, 10, 4)
X_hero = X_hero.reshape(-1, 10)

Y = df["radiant_win"].to_numpy()

data = (X_ab, X_hero, Y, ab_id2idx, ab_idx2id, hero_id2idx, hero_idx2id, match_ids)

with open("./data/ml_ready_data.pickle", "bw") as f:
    pkl.dump(data, f)