import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from backend import RewardChest

# backend class instance
reward_chest_instance = RewardChest()


class RsLootSimApp:
    """
    This class contains the main window of the application.
    """
    # TODO: place fields correctly, in an aesthetically pleasing way
    # TODO: add area for loot with images
    # TODO: add pet and white loot calculations
    # TODO: fetch current ge prices, show value of loot
    # TODO: add area for loot value, calculations for hourly profit
    # TODO: change colors, theme, fonts
    # TODO: add scrollbar to sidepanel, add button to clear sidepanel + list

    def __init__(self):
        """
        RsLootSimApp class constructor.
        """
        # creating root window
        self.window = Tk()
        self.window.title('OSRS Tombs of Amascut Loot Simulator')
        self.window.geometry("400x300+10+10")
        self.window.eval('tk::PlaceWindow . center')
        self.style = tk.ttk.Style(self.window)
        self.style.theme_use("vista")
        self.logo = PhotoImage(
            file='./static/media/game_icon_tombsofamascut.png')
        self.window.iconphoto(False, self.logo)
        self.runs_window = None

        # validation
        self.validation = self.window.register(self.callback)

        # declaring raid config variables
        self.raid_lvl_var = tk.IntVar()
        self.wtp_invoc_var = tk.BooleanVar()
        self.path_invoc_var = tk.StringVar()
        self.team_size_var = tk.IntVar()
        self.runs_var = tk.IntVar()

        # other variables
        self.panel_counter = 0

        # setting up UI elements
        # raid_lvl
        self.raid_lvl_label = tk.Label(self.window, text='Raid Level',
                                       font=('calibre', 10, 'bold'))
        self.raid_lvl_entry = tk.Entry(self.window,
                                       textvariable=self.raid_lvl_var,
                                       font=('calibre', 10, 'normal'),
                                       validate="key",
                                       validatecommand=(self.validation, '%S'))

        # team_size
        self.team_size_label = tk.Label(self.window, text='Team Size',
                                        font=('calibre', 10, 'bold'))
        self.team_size_entry = tk.Entry(self.window,
                                        textvariable=self.team_size_var,
                                        font=('calibre', 10, 'normal'),
                                        validate="key",
                                        validatecommand=(self.validation, '%S'))

        # runs
        self.runs_label = tk.Label(self.window, text='Runs',
                                   font=('calibre', 10, 'bold'))
        self.runs_sp = Spinbox(self.window, from_=0, to=1000,
                               textvariable=self.runs_var)
        # runs_sp.place(x=80, y=170)

        # path invoc
        self.path_invoc_label = tk.Label(self.window, text='Path Invocations',
                                         font=('calibre', 10, 'bold'))
        self.path_invoc_var.set("None")
        self.path_invoc_var_data = (
        "None", "Pathseeker", "Pathfinder", "Pathmaster")
        self.path_invoc_cb = Combobox(self.window,
                                      values=self.path_invoc_var_data,
                                      textvariable=self.path_invoc_var)
        # path_invoc_cb.place(x=60, y=150)

        # wtp
        self.wtp_label = tk.Label(self.window, text='WTP',
                                  font=('calibre', 10, 'bold'))
        self.wtp_invoc_var_cb = Checkbutton(self.window, text="Walk The Path",
                                            variable=self.wtp_invoc_var)
        self.wtp_invoc_var_cb.place(x=100, y=100)

        # button that will call the configure function
        self.cfg_btn = tk.Button(self.window, text='Configure',
                                 command=self.configure)

        # button that will call the simulate function
        self.sim_btn = tk.Button(self.window, text='Simulate',
                                 command=self.simulate)

        # button to open right side panel
        self.opn_btn = tk.Button(self.window, text='>>',
                                 command=self.open_panel)

        # placing fields in grid
        self.raid_lvl_label.grid(row=0, column=0, sticky=W)
        self.raid_lvl_entry.grid(row=0, column=1)
        self.team_size_label.grid(row=1, column=0, sticky=W)
        self.team_size_entry.grid(row=1, column=1)
        self.path_invoc_label.grid(row=2, column=0, sticky=W)
        self.path_invoc_cb.grid(row=2, column=1)
        self.wtp_label.grid(row=3, column=0, sticky=W)
        self.wtp_invoc_var_cb.grid(row=3, column=1)
        self.cfg_btn.grid(row=4, column=1)
        self.runs_label.grid(row=6, column=0)
        self.runs_sp.grid(row=6, column=1)
        self.sim_btn.grid(row=7, column=1)
        self.opn_btn.grid(row=8, column=2)

    def open_panel(self):
        """
        Opens the side panel for the runs breakdown.
        :return:
        """
        if self.panel_counter == 0:
            self.runs_window = SidePanel()
            self.panel_counter += 1
            self.opn_btn['text'] = '<<'
        else:
            # TODO: if exited with red X, button and counter is not updated
            self.runs_window.panel.destroy()
            self.panel_counter -= 1
            self.opn_btn['text'] = '>>'

        return None

    @staticmethod
    def callback(user_input):
        """
        Method for validating user input.
        :param user_input: User input to validate.
        :return: True or False based on validity of user input.
        """
        if user_input.isdigit():
            return True
        else:
            return False

    def configure(self):
        """
        This method configures the raid settings.
        :return: None
        """
        raid_lvl = self.raid_lvl_var.get()
        if raid_lvl < 0 or raid_lvl > 600:
            messagebox.showerror("User Input Error",
                                 "Raid level can only be a number between 0 and 600!")
            # self.open_popup()

        team_size = self.team_size_var.get()
        if team_size < 1 or team_size > 8:
            messagebox.showerror("User Input Error",
                                 "Team size can onyl be a number between 1 and 8!")
            # self.open_popup()

        wtp_invoc = self.wtp_invoc_var.get()
        path_invoc = self.path_invoc_var.get()

        if wtp_invoc:
            wtp_invoc = "yes"
        else:
            wtp_invoc = "no"

        print("Raid lvl : " + str(raid_lvl))
        print("Team size : " + str(team_size))
        print("Wtp? : " + str(wtp_invoc))
        print("Path invoc : " + str(path_invoc))

        chance = reward_chest_instance.get_chance(raid_lvl, team_size,
                                                  path_invoc, wtp_invoc)

    def simulate(self):
        """
        This method simulates the reward chest based on the config and
        the number of runs.
        :return:
        """
        runs = self.runs_var.get()
        reward_chest_instance.simulate_roll(runs)

        # clear listbox before next simulation
        self.runs_window.runs_listbox.delete(0, tk.END)

        for index, purple_item in enumerate(reward_chest_instance.all_purple_loot):
            if self.panel_counter == 1:
                self.runs_window.runs_listbox.insert(index, purple_item)

        return None

class SidePanel(RsLootSimApp):
    """
    This class contains the side panel that shows the runs breakdown.
    """
    def __init__(self):
        self.panel = Toplevel(loot_sim_app.window)
        self.panel.title("Run Breakdown")
        self.panel.iconphoto(False, loot_sim_app.logo)
        x = loot_sim_app.window.winfo_x()
        y = loot_sim_app.window.winfo_y()
        self.panel.geometry("500x700")
        self.panel.geometry("+%d+%d" % (x + 400, y))
        self.runs_listbox = Listbox(self.panel, width='70', height='40')
        self.runs_listbox.grid(row=0, column=0)


if __name__ == "__main__":
    loot_sim_app = RsLootSimApp()
    # loop window
    loot_sim_app.window.mainloop()
