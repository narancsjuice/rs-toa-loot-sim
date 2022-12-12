import random

# TODO: add GUI - with images for items
# TODO: fetch purple rate from https://oldschool.runescape.wiki/api.php?rswcalcautosubmit=disabled
# TODO: fetch current ge prices, show value of loot


class RewardChest:
    """
    This class is used to hold all data related to TOA reward chest loot simulation.

    Methods:
        __init__(self)
        float_to_int(float_number)
        simulate_roll(self)
    """

    def __init__(self):
        """
        RewardChest class constructor to initialize object.
        """
        # TODO: add input field for raid level, team size, path settings, number of runs to simulate
        self.raid_lvl = 350
        self.wtp_invoc = "yes"
        self.path_invoc = "pathseeker"
        self.team_size = 1
        self.runs = 100
        self.purple_chance = 1 / 16.7979
        self.white_chance = 1 - self.purple_chance
        self.loot = [("White loot", self.float_to_int(self.white_chance)),
                     ("Purple item", self.float_to_int(self.purple_chance))]
        self.purple_rates = [("Lightbearer", 1 / 3.429),
                       ("Osmumten's Fang", 1 / 3.429),
                       ("Elidinis' Ward", 1 / 8),
                       ("Masori mask", 1 / 12),
                       ("Masori chaps", 1 / 12),
                       ("Masori body", 1 / 12),
                       ("Tumeken's Shadow", 1 / 24)]

    @staticmethod
    def float_to_int(float_number):
        """
        Multiplies float numbers to return back semi-accurate integers.

        :param float_number: Floating point number.
        :return: Integer created from given floating point number.
        """
        float_number = float_number * 1000000
        int_number = int(float_number)

        return int_number

    def simulate_roll(self):
        """
        Simulates item rolls from the TOA reward chest.

        :return: None
        """
        counter = 0
        choices = []
        purple_choices = []
        while counter < self.runs:
            for item, weight in self.loot:
                choices.extend([item] * weight)
                roll = random.choice(choices)
            if roll == "Purple item":
                for p_item, p_weight in self.purple_rates:
                    p_weight = self.float_to_int(p_weight)
                    purple_choices.extend([p_item] * p_weight)
                    purple_roll = random.choice(purple_choices)
                print("Run " + str(counter + 1) + " - " + roll + " - " + purple_roll)
            else:
                # TODO: implement white loot calculation
                # print("Run " + str(counter+1)+ " - " + roll)
                ""
            counter += 1

        return None


if __name__ == "__main__":
    try:
        reward_chest_instance = RewardChest()
        reward_chest_instance.simulate_roll()
    except BaseException:
        ""