import json

hero_id_path = "./constants/heros.json"
ab_id_path = "./constants/ab_ids.json"

with open(hero_id_path, 'r') as f:
    id2hero = json.load(f)

with open(ab_id_path, 'r') as f:
    id2ab = json.load(f)


'''
{5108: 'tiny_tree_grab',
 6937: 'tiny_toss_tree',

 5486: 'wisp_spirits',
 5490: 'wisp_spirits_in',
 5493: 'wisp_spirits_out',

 5625: 'phoenix_fire_spirits',
 5631: 'phoenix_launch_fire_spirit',

 5252: 'life_stealer_infest',
 5253: 'life_stealer_consume',

 6340: 'dark_willow_bedlam',
 8340: 'dark_willow_terrorize',
 
 5721: 'monkey_king_tree_dance',
 5724: 'monkey_king_primal_spring',
 
 5033: 'kunkka_x_marks_the_spot',
 5034: 'kunkka_return',
 
 5069: 'puck_illusory_orb',
 5071: 'puck_waning_rift',
 
 5366: 'alchemist_unstable_concoction',
 5367: 'alchemist_unstable_concoction_throw',
 
 5605: 'ember_spirit_flame_guard',
 5606: 'ember_spirit_fire_remnant',

 5471: 'keeper_of_the_light_illuminate',
 5479: 'keeper_of_the_light_spirit_form_illuminate',
 }
 '''

ab_id_recast = {
    6937: 5108,
    5493: 5486,
    5490: 5486,
    5631: 5625,
    5253: 5252,
    6340: 8340,
    5724: 5721,
    5034: 5033,
    5071: 5069,
    5367: 5366,
    5606: 5605,
    5479: 5471
}




