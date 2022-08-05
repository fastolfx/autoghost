import os
import time

#you have to change paths everywhere (dont change anything after "saveghost\"

path = "D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav.ghost" # here
path2 = "D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav_1.ghost" # here
while True:
    time.sleep(5) # completes command every 5 seconds
    if os.path.exists(path):
        os.rename(r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav.ghost', r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_load.ghost') # if path to challenge_run_main_sav.ghost exists it renames it into challenge_run_main_load.ghost
    if os.path.exists(path2):
        os.remove(r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_load.ghost')
        os.rename(r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav_1.ghost', r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_load.ghost') # if path to challenge_run_main_sav_1.ghost exists it removes challenge_run_main_load.ghost and renames challenge_run_main_sav_1.ghost into challenge_run_main_load.ghost
