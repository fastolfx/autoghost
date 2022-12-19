# Imports

import os
import time
import shutil

# Getting directory
directory = os.getcwd()

# Defining files
land = (str(directory) + '\challenge_run_main_sav.ghost') #
pit = (str(directory) + '\spikyroad_main_sav.ghost')
dojo = (str(directory) + '\shaolinplaza_main_sav.ghost')
tower = (str(directory) + '\challenge_goingup_main_sav.ghost')

while True:
    time.sleep(2) # completes command every 2 seconds
#land
    if os.path.exists(land):
        shutil.copyfile(r'challenge_run_main_sav.ghost', r'challenge_run_main_load.ghost')
        os.remove(r'challenge_run_main_sav.ghost')
#pit
    if os.path.exists(pit):
        shutil.copyfile(r'spikyroad_main_sav.ghost', r'spikyroad_main_load.ghost')
        os.remove(r'spikyroad_main_sav.ghost')
#dojo
    if os.path.exists(dojo):
        shutil.copyfile(r'shaolinplaza_main_sav.ghost', r'shaolinplaza_main_load.ghost')
        os.remove(r'shaolinplaza_main_sav.ghost')
#tower
    if os.path.exists(tower):
        shutil.copyfile(r'challenge_goingup_main_sav.ghost', r'challenge_goingup_main_load.ghost')
        os.remove(r'challenge_goingup_main_sav.ghost')
