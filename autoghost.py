import os
import time
import shutil

# made by froggert (discord - kys#5888)
# you have to change paths everywhere (dont change anything after "saveghost\"

land = "D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav.ghost" #
pit = "D:\\RaymanLegends\gamesave\saveghost\spikyroad_main_sav.ghost"
dojo = "D:\\RaymanLegends\gamesave\saveghost\shaolinplaza_main_sav.ghost"
tower = "D:\\RaymanLegends\gamesave\saveghost\challenge_goingup_main_sav.ghost"
while True:
    time.sleep(3) # completes command every 3 seconds
#land
    if os.path.exists(land):
        shutil.copyfile(r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav.ghost', r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_load.ghost')
        os.remove(r'D:\\RaymanLegends\gamesave\saveghost\challenge_run_main_sav.ghost')
#pit
    if os.path.exists(pit):
        shutil.copyfile(r'D:\\RaymanLegends\gamesave\saveghost\spikyroad_main_sav.ghost', r'D:\\RaymanLegends\gamesave\saveghost\spikyroad_main_load.ghost')
        os.remove(r'D:\\RaymanLegends\gamesave\saveghost\spikyroad_main_sav.ghost')
#dojo
    if os.path.exists(dojo):
        shutil.copyfile(r'D:\\RaymanLegends\gamesave\saveghost\shaolinplaza_main_sav.ghost', r'D:\\RaymanLegends\gamesave\saveghost\shaolinplaza_main_load.ghost')
        os.remove(r'D:\\RaymanLegends\gamesave\saveghost\shaolinplaza_main_sav.ghost')
#tower
    if os.path.exists(tower):
        shutil.copyfile(r'D:\\RaymanLegends\gamesave\saveghost\challenge_goingup_main_sav.ghost', r'D:\\RaymanLegends\gamesave\saveghost\challenge_goingup_main_load.ghost')
        os.remove(r'D:\\RaymanLegends\gamesave\saveghost\challenge_goingup_main_sav.ghost')