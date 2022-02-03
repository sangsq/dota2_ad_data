import json

hero_id_path = "./constants/heros.json"
ab_id_path = "./constants/ab_ids.json"

with open(hero_id_path, 'r') as f:
    id2hero = json.load(f)

with open(ab_id_path, 'r') as f:
    id2ab = json.load(f)

ult_abs = {5606, 5121, 5125, 5640, 5129, 5133, 5137, 5141, 5654, 5144, 7705, 5149, 5153, 5157, 5161, 5165, 5176, 5177, 5181, 5185, 5189, 5193, 5197, 5725, 5221, 5225, 5229, 5240, 5244, 5248, 5252, 7304, 5258, 5262, 5266, 5267, 8340, 5274, 5278, 5279, 5288, 5292, 5300, 6343, 5323, 5331, 5337, 5342, 7906, 5348, 5356, 5360, 5364, 5369, 5380, 5394, 5398, 5403, 5415, 5425, 5429, 5437, 5447, 6482, 5461, 5465, 6491, 5470, 5474, 5483, 5488, 5497, 5507, 5512, 5517, 5006, 5521, 5010, 5013, 5527, 5018, 5022, 5026, 5030, 8106, 5035, 5551, 5043, 5047, 5049, 5568, 6598, 5064, 5067, 5584, 5073, 5588, 5077, 5081, 5594, 5085, 5598, 5089, 5602, 5093, 5097, 5612, 5101, 5616, 5105, 5109, 5622, 5113, 5117, 5630}

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
 5070: 'puck_ethereal_jaunt',
 
 5366: 'alchemist_unstable_concoction',
 5367: 'alchemist_unstable_concoction_throw',
 
 5606: 'ember_spirit_fire_remnant',
 5607: 'ember_spirit_activate_fire_remnant',

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
    5070: 5069,
    5367: 5366,
    5607: 5606,
    5479: 5471
}




