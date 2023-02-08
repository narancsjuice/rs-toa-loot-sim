import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from backend import RewardChest

reward_chest_instance = RewardChest()

#TODO: add validation for fields
#TODO: place fields correctly
#TODO: add toggleable sidebar
#TODO: add area for loot
#TODO: add area for loot value
#TODO: change colors, theme, fonts

window = Tk()
window.title('OSRS Tombs of Amascut Loot Simulator')
window.geometry("400x300+10+10")
style = tk.ttk.Style(window)
style.theme_use("vista")

# declaring variables
raid_lvl_var = tk.IntVar()
wtp_invoc_var = tk.BooleanVar()
path_invoc_var = tk.StringVar()
team_size_var = tk.IntVar()
runs_var = tk.IntVar()


def configure():
    """

    :return:
    """
    raid_lvl = raid_lvl_var.get()
    wtp_invoc = wtp_invoc_var.get()
    path_invoc = path_invoc_var.get()
    team_size = team_size_var.get()

    if wtp_invoc:
        wtp_invoc = "yes"
    else:
        wtp_invoc = "no"

    print("Raid lvl : " + str(raid_lvl))
    print("Team size : " + str(team_size))
    print("Wtp? : " + str(wtp_invoc))
    print("Path invoc : " + str(path_invoc))

    chance = reward_chest_instance.get_chance(raid_lvl, team_size, path_invoc, wtp_invoc)


def simulate():
    """

    :return:
    """
    runs = runs_var.get()
    roll_sim = reward_chest_instance.simulate_roll(runs)


# creating a label for raid_lvl
raid_lvl_label = tk.Label(window, text='Raid Level',
                          font=('calibre', 10, 'bold'))

# creating an entry for raid_lvl
raid_lvl_entry = tk.Entry(window, textvariable=raid_lvl_var,
                          font=('calibre', 10, 'normal'))

# creating a label for team_size
team_size_label = tk.Label(window, text='Team Size',
                           font=('calibre', 10, 'bold'))

# creating an entry for team_size
team_size_entry = tk.Entry(window, textvariable=team_size_var,
                           font=('calibre', 10, 'normal'))

# runs
runs_label = tk.Label(window, text='Runs',
                           font=('calibre', 10, 'bold'))
runs_sp = Spinbox(window, from_=0, to=1000, textvariable=runs_var)
#runs_sp.place(x=80, y=170)

# path invoc
path_invoc_label = tk.Label(window, text='Path Invocations',
                           font=('calibre', 10, 'bold'))
path_invoc_var.set("None")
path_invoc_var_data = ("None", "Pathseeker", "Pathfinder", "Pathmaster")
path_invoc_cb = Combobox(window, values=path_invoc_var_data, textvariable=path_invoc_var)
#path_invoc_cb.place(x=60, y=150)

# wtp
wtp_label = tk.Label(window, text='WTP',
                           font=('calibre', 10, 'bold'))
wtp_invoc_var_cb = Checkbutton(window, text="Walk The Path", variable=wtp_invoc_var)
wtp_invoc_var_cb.place(x=100, y=100)

# creating a button using the widget Button that will call the configure function
cfg_btn=tk.Button(window, text='Configure', command=configure)

# creating a button using the widget Button that will call the simulate function
sim_btn=tk.Button(window, text='Simulate', command=simulate)

# placing fields in grid
raid_lvl_label.grid(row=0, column=0)
raid_lvl_entry.grid(row=0, column=1)
team_size_label.grid(row=1, column=0)
team_size_entry.grid(row=1, column=1)
path_invoc_label.grid(row=2, column=0)
path_invoc_cb.grid(row=2, column=1)
wtp_label.grid(row=3, column=0)
wtp_invoc_var_cb.grid(row=3, column=1)
cfg_btn.grid(row=4, column=1)
runs_label.grid(row=6, column=0)
runs_sp.grid(row=6, column=1)
sim_btn.grid(row=7, column=1)

#loop window
window.mainloop()
