import random

# TODO: add GUI - with images for items
# TODO: add input field for raid level, team size, path settings, number of runs to simulate

# raid level 375
# TODO: fetch purple rate from https://oldschool.runescape.wiki/api.php?rswcalcautosubmit=disabled
purple_chance = 0.07171 * 100000
white_chance = 100000 - purple_chance

loot = [("White loot", int(white_chance)), ("Purple item", int(purple_chance))]
purple = [("Lightbearer", 29163), ("Osmumten's Fang", 29163),
          ("Elidinis' Ward", 12500), ("Masori mask", 8333),
          ("Masori chaps", 8333), ("Masori body", 8333),
          ("Tumeken's Shadow", 4166)]

choices = []
purple_choices = []
counter = 0

while counter < 25:
    for item, weight in loot:
        choices.extend([item]*weight )
        roll = random.choice(choices)
    if roll == "Purple item":
        for p_item, p_weight in purple:
            purple_choices.extend([p_item]*p_weight)
            purple_roll = random.choice(purple_choices)
        print("Run " + str(counter+1)+ " - " + roll + " - " + purple_roll)
    else:
        # TODO: implement white loot calculation
        print("Run " + str(counter+1)+ " - " + roll)

    counter += 1

# TODO: fetch current ge prices, show value of loot