import random
import requests

# TODO: add GUI - with images for items
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
        #self.raid_lvl = input("Raid level (0-600): ")
        #self.wtp_invoc = input("Walk The Path? (yes, no): ")
        #self.path_invoc = input("Path invocations (pathseeker, pathfinder, pathmaster): ")
        #self.team_size = input("Team size? (1-8)")
        #self.runs = input("Number of runs to simulate? ")
        self.contr_pts = 0
        self.purple_chance = 0
        self.pet_chance = 0
        self.white_chance = 0
        self.loot = []

        self.purple_rates = [("Lightbearer", 1 / 3.429),
                       ("Osmumten's Fang", 1 / 3.429),
                       ("Elidinis' Ward", 1 / 8),
                       ("Masori mask", 1 / 12),
                       ("Masori chaps", 1 / 12),
                       ("Masori body", 1 / 12),
                       ("Tumeken's Shadow", 1 / 24)]

    def get_chance(self, raid_lvl, team_size, path_invoc, wtp_invoc):
        """
        Fetches contribution points, purple and pet chances from OSRS Wiki API
        based on the set raid parameters.

        :param raid_lvl: Integer of raid difficulty level.
        :param team_size: Integer of number of players.
        :param path_invoc: String of set path invocation name.
        :param wtp_invoc: Bool of set WTP invocation.
        :return: None
        """
        url = "https://oldschool.runescape.wiki/api.php"
        data = "action=parse&text=%7B%7B%23invoke%3ATombs+of+Amascut+loot%7Cmain" \
               "%7Craid_level%3D" + str(raid_lvl) + \
               "%7Cteam_size%3D" + str(team_size) + \
               "%7Cpath_invocation%3D" + str(path_invoc) + \
               "%7Cwalk_the_path%3D" + str(wtp_invoc) + \
               "%7D%7D&prop=text%7Climitreportdata&title=Calculator%3ATombs_of_Amascut_loot&disablelimitreport=true&contentmodel=wikitext&format=json"
        response = requests.post(url, data=data, headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})

        raw_text = response.json()["parse"]["text"]
        raw_text = str(raw_text)
        text_dict = raw_text.split()

        # get chance values from text
        matching = [t for t in text_dict if "<b>" in t]
        print("match:" + str(matching))
        self.contr_pts = matching[0][3:-4]
        self.purple_chance = float(matching[2][3:-5]) / 100
        self.pet_chance = float(matching[3][3:-5]) / 100
        self.white_chance = 1 - self.purple_chance
        self.loot = [("White loot", self.float_to_int(self.white_chance)),
                     ("Purple item", self.float_to_int(self.purple_chance))]

        return None

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

    def simulate_roll(self, runs):
        """
        Simulates item rolls from the TOA reward chest.

        :return: None
        """
        counter = 0
        choices = []
        purple_choices = []
        while counter < int(runs):
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
    #TODO: restore try catch block
    reward_chest_instance = RewardChest()
    #reward_chest_instance.get_chance()
    #reward_chest_instance.simulate_roll()
    #try:
    #    reward_chest_instance = RewardChest()
    #    reward_chest_instance.get_chance()
    #    reward_chest_instance.simulate_roll()
    #except BaseException:
    #    ""