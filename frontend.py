import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
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
        self.runs_breakdown = None
        self.loot_tab = None

        # validation
        self.validation = self.window.register(self.callback)

        # declaring raid config variables
        self.raid_lvl_var = tk.IntVar()
        self.wtp_invoc_var = tk.BooleanVar()
        self.path_invoc_var = tk.StringVar()
        self.team_size_var = tk.IntVar()
        self.runs_var = tk.IntVar()

        # other variables
        self.rpanel_counter = 0
        self.lpanel_counter = 0

        # displayed item images and labels
        self.uniques_images = {}
        self.purple_img_x = 8
        self.purple_img_y = 8
        self.count_labels = {}

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
        self.runs_sp = Spinbox(self.window, from_=1, to=1000,
                               textvariable=self.runs_var)

        # path invoc
        self.path_invoc_label = tk.Label(self.window, text='Path Invocations',
                                         font=('calibre', 10, 'bold'))
        self.path_invoc_var.set("None")
        self.path_invoc_var_data = (
        "None", "Pathseeker", "Pathfinder", "Pathmaster")
        self.path_invoc_cb = Combobox(self.window,
                                      values=self.path_invoc_var_data,
                                      textvariable=self.path_invoc_var)

        # wtp
        self.wtp_label = tk.Label(self.window, text='WTP',
                                  font=('calibre', 10, 'bold'))
        self.wtp_invoc_var_cb = Checkbutton(self.window, text="Walk The Path",
                                            variable=self.wtp_invoc_var)
        self.wtp_invoc_var_cb.place(x=100, y=100)

        # simulate button
        self.sim_btn = tk.Button(self.window, text='Simulate',
                                 command=self.simulate)

        # reset button
        self.reset_btn = tk.Button(self.window, text='Reset', command=self.reset)

        # quit button
        self.quit_btn = tk.Button(self.window, text='Quit', command=self.quit)

        # placing fields in grid
        self.raid_lvl_label.grid(row=0, column=0, sticky=W)
        self.raid_lvl_entry.grid(row=0, column=1)
        self.team_size_label.grid(row=1, column=0, sticky=W)
        self.team_size_entry.grid(row=1, column=1)
        self.path_invoc_label.grid(row=2, column=0, sticky=W)
        self.path_invoc_cb.grid(row=2, column=1)
        self.wtp_label.grid(row=3, column=0, sticky=W)
        self.wtp_invoc_var_cb.grid(row=3, column=1)
        self.runs_label.grid(row=6, column=0)
        self.runs_sp.grid(row=6, column=1)
        self.sim_btn.grid(row=7, column=1)
        self.reset_btn.grid(row=8, column=2)
        self.quit_btn.grid(row=9, column=2)

    def disable_event(self):
        pass

    def quit(self):
        """

        :return:
        """
        self.window.destroy()

        return None

    def reset(self):
        """

        :return:
        """
        #reward_chest_instance.all_runs_loot.clear()
        reward_chest_instance.all_purple_loot.clear()
        self.uniques_images.clear()
        self.raid_lvl_entry.delete(0, END)
        self.raid_lvl_entry.insert(0, 0)
        self.team_size_entry.delete(0, END)
        self.team_size_entry.insert(0,0)
        self.path_invoc_cb.set("None")
        self.wtp_invoc_var_cb.deselect()
        self.runs_sp.delete(0, END)
        self.runs_sp.insert(0, 1)
        self.rpanel_counter = 0
        self.lpanel_counter = 0
        self.runs_breakdown.runs_listbox.delete(0, tk.END)
        self.runs_breakdown.rpanel.destroy()
        self.loot_tab.lpanel.destroy()
        self.purple_img_x = 5
        self.purple_img_y = 5

        return None

    def open_runs_breakdown(self):
        """
        Opens the side panel for the runs breakdown.
        :return:
        """
        if self.rpanel_counter == 0:
            self.runs_breakdown = RunsBreakdown()
            self.rpanel_counter += 1
        else:
            # TODO: if exited with red X, button and counter is not updated
            self.runs_breakdown.rpanel.destroy()
            self.rpanel_counter -= 1

        return None

    def open_loot_tab(self):
        """
        Opens the side panel for the loot tab.
        :return:
        """
        if self.lpanel_counter == 0:
            self.loot_tab = LootTab()
            self.lpanel_counter += 1
        else:
            # TODO: if exited with red X, button and counter is not updated
            self.loot_tab.lpanel.destroy()
            self.lpanel_counter -= 1
            self.uniques_images.clear()

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

    def simulate(self):
        """
        This method simulates the reward chest based on the config and
        the number of runs.
        :return:
        """
        raid_lvl = self.raid_lvl_var.get()
        if raid_lvl < 0 or raid_lvl > 600 or raid_lvl == "":
            messagebox.showerror("User Input Error",
                                 "Raid level can only be a number between 0 and 600!")

        team_size = self.team_size_var.get()
        if team_size < 1 or team_size > 8 or team_size == "":
            messagebox.showerror("User Input Error",
                                 "Team size can only be a number between 1 and 8!")

        wtp_invoc = self.wtp_invoc_var.get()
        path_invoc = self.path_invoc_var.get()

        if wtp_invoc:
            wtp_invoc = "yes"
        else:
            wtp_invoc = "no"

        chance = reward_chest_instance.get_chance(raid_lvl, team_size,
                                                  path_invoc, wtp_invoc)

        runs = self.runs_var.get()
        if runs < 1 or runs == "":
            messagebox.showerror("User Input Error",
                                 "To roll the reward chest, you have to clear the raid at least once!")

        reward_chest_instance.simulate_roll(runs)

        if self.lpanel_counter == 0:
            self.open_loot_tab()

        if self.rpanel_counter == 0:
            self.open_runs_breakdown()

        if self.rpanel_counter == 1:
            for index, purple_item in enumerate(reward_chest_instance.all_runs_loot):
                # clear listbox before next simulation
                #    self.runs_breakdown.runs_listbox.delete(0, tk.END)
                self.runs_breakdown.runs_listbox.insert(index, purple_item)

        self.display_img()

        return None

    def display_img(self):
        """

        :return:
        """
        uniques = set(reward_chest_instance.all_purple_loot)
        purple_count = {}

        for unique in uniques:
            purple_count[unique] = reward_chest_instance.all_purple_loot.count(unique)
            if unique not in self.uniques_images.keys():
                img = tk.PhotoImage(file="static/media/purple_loot_png/" + str(unique) + ".png")
                img_panel = tk.Label(self.loot_tab.lpanel, image=img)
                img_panel.photo = img
                count_label = tk.Label(self.loot_tab.lpanel, text=purple_count[unique], bg='#000', fg='#ff0', bd=0)
                count_label.place(x=self.purple_img_x + img.width() + 2, y=1)
                self.count_labels[unique] = count_label
                if img.height() > 25:
                    img_panel.place(x=self.purple_img_x, y=self.purple_img_y)
                else:
                    img_panel.place(x=self.purple_img_x, y=self.purple_img_y + 5)
                self.purple_img_x = self.purple_img_x + img.width() + 10
                self.uniques_images[unique] = img
            elif unique in self.uniques_images.keys():
                self.count_labels[unique].config(text=purple_count[unique])

        return None


class LootTab(RsLootSimApp):
    """
    This class contains the images and amount of the received loot.
    """
    def __init__(self):
        self.lpanel = Toplevel(loot_sim_app.window)
        self.lpanel.title("Loot Tab")
        self.lpanel.iconphoto(False, loot_sim_app.logo)
        x = loot_sim_app.window.winfo_x()
        y = loot_sim_app.window.winfo_y()
        self.lpanel.geometry("300x200")
        self.lpanel.geometry("+%d+%d" % (x + 400, y))
        self.lpanel.protocol("WM_DELETE_WINDOW", self.disable_event)


class RunsBreakdown(RsLootSimApp):
    """
    This class contains the side panel that shows the runs breakdown.
    """
    def __init__(self):
        self.rpanel = Toplevel(loot_sim_app.window)
        self.rpanel.title("Runs Breakdown")
        self.rpanel.iconphoto(False, loot_sim_app.logo)
        #x = loot_sim_app.loot_tab.lpanel.winfo_x()
        #y = loot_sim_app.loot_tab.lpanel.winfo_y()
        x = loot_sim_app.window.winfo_x()
        y = loot_sim_app.window.winfo_y()
        self.rpanel.geometry("500x700")
        self.rpanel.geometry("+%d+%d" % (x + 700, y))
        self.runs_listbox = Listbox(self.rpanel, width='70', height='40')
        self.runs_listbox.grid(row=0, column=0)
        self.rpanel.protocol("WM_DELETE_WINDOW", self.disable_event)


if __name__ == "__main__":
    loot_sim_app = RsLootSimApp()
    # loop window
    loot_sim_app.window.mainloop()
