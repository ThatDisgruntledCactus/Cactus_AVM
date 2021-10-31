#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 04:18:15 2021

@author: TheDisgruntledCactus
"""

import urllib.request
import os
import os.path
import zipfile
from PIL import Image

# work_directory_init opens up the file given to it from the GUI
# Different variables will have different read-ins and variables (obviously)

os.system('clear')

current_dir = os.getcwd()
current_dir = current_dir.replace("\n", "")


if os.path.isfile(current_dir + "/cactus_bully.py") == False:
    print('Sorry, but you must launch this script from the root python directory; where cactus_bully.py resides. CD into the directory it is in, and')
    print('run it from there with:    python cactus_bully.py\n\n' )
    raise SystemExit()

print("Welcome to the Cactus Automated Vidya Modifier!")
print("================================================")
print('\n\nThis script will automate the install of the excellent Widescreen Patch by ThirteenAG, and')
print('the Silent Patch by Cookieplmonster and P3ti, a well-regarded fan-patch for modern computers.')
print('\nThis uses no copyrighted code by Rockstar, so pls no Bully.')

print("\n-----------------------")

print('\n\nPhotos will pop up during the process to guide you along the process. If you do not')
print('need assistance, and prefer text, you have the option. Be sure to check if you know')
print('what the photo is instructing before blindly exiting out of it if the option is selected.')
print('\nMaximize terminal for the best possible experience.')

input('\n\nTo begin the process, press Enter ...')

current_dir = os.getcwd()
current_dir = current_dir.replace("\n", "")

os.system('clear')

photo_help = \
    input("""If you would like photo assistance from this point forward, enter 1.\n
Otherwise, if you feel more advanced, enter anything else for 
text instructions only. \n\n(Photos are poorly drawn, but helpful. Do not be
alarmed if they pop up in front of your terminal):  """)

if photo_help == '1':
    placeholder = Image.open(current_dir + '/Images/Guide_to_root_directory_pasting.png')
    placeholder.show()

os.system('clear')

work_directory_active = \
    input("""Please copy the root directory of your Bully game folder (Follow photo if you need
additional assistance) :  """)

work_directory_active = work_directory_active.replace("\n", "")

if work_directory_active.endswith('n'):
    work_directory_active = (work_directory_active + "/")
    
elif work_directory_active.endswith("/"):
    pass
else:
    print('\n\nGame directory is wrong. Last character should be a /, or the word "Edition".')
    raise SystemExit()
    
print(work_directory_active)

if os.path.isfile(work_directory_active + 'Bully.exe') == True:
    pass
else:
    print('Bully.exe is not here. Not sure where this is. Wrong directory.')
    raise SystemExit()
        
os.system('clear')

fps_choice = \
    input("""Would you like to raise the FPS from 30 to 60? Most of the game runs
without issue at this speed.
\n\nEnter y for Yes, or n for No :  """)

os.system('clear')

if fps_choice == 'y' or fps_choice == 'Y':
    print('60 FPS it is! If you have problems later on in the game on an activity,')
    print('edit SilentPatchBully.ini, located in the same root folder you copied at the start.')

elif fps_choice == 'n' or fps_choice == 'N':
    print('No problem, the FPS will stay at 30.')

else:
    print('You entered incorrectly. Only a y for Yes or n for no, capitalized or not, is allowed.')
    raise SystemExit()

os.system('clear')

        

mod_zip_dir = ('SilentPatchBully.zip')

print('Grabbing the Silent Patch by Cookieplmonster and P3ti...')
print('-------------------------------------------------------------')

url = 'https://github.com/CookiePLMonster/SilentPatchBully/releases/latest/download/SilentPatchBully.zip'

urllib.request.urlretrieve(
    url, (work_directory_active + mod_zip_dir))

mod_zip_location = (work_directory_active + mod_zip_dir)


if os.path.isfile(work_directory_active + mod_zip_dir) == True:
    print('\n\nMod aquired! We are this much closer to enjoying one of the last')
    print('original games that Rockstar put out before milking GTA V!')

else:
    print('\nThe downloading process is being a real dork. Report it on my')
    print('github, and I will try to get back to you shortly.\n')
    raise SystemExit

with zipfile.ZipFile((work_directory_active + 'SilentPatchBully.zip'), 'r') as zip_ref:
    zip_ref.extractall((work_directory_active))
    

mod_ini_dir = ('SilentPatchBully.ini')

mod_ini_location = (work_directory_active + mod_ini_dir)
mod_ini_location = mod_ini_location.replace("\n", "")

    
if os.path.isfile(work_directory_active + mod_ini_dir) == True:     
    
    os.remove((mod_zip_location))
    
    if fps_choice == 'y' or fps_choice == 'Y':
        
        os.remove(work_directory_active + mod_ini_dir)
        
        new_ini = open(work_directory_active + mod_ini_dir, "x")
        
        new_ini.write("[SilentPatch]\nFPSLimit=60\nCustomMemoryMgr=0")
        
        new_ini.close()
                                    
        print('\n\nFPS successfully changed to 60!')
            
    mod_zip_dir = ('dinput8.dll')
    
    mod_zip_location = (work_directory_active + mod_zip_dir)
    
    os.remove((mod_zip_location))
        
    mod_zip_dir = ('Bully.WidescreenFix.zip')

    print('\n\nRemoving zip file, since it is no longer needed ...')
    print('\n\nMod has been successfully installed onto the system!')
           
    print('\n\nNow installing Widescreen Fix by ThirteenAG ...')
    print('-------------------------------------------------------------')     
        

    url = 'https://github.com/ThirteenAG/WidescreenFixesPack/releases/download/bully/Bully.WidescreenFix.zip'

    urllib.request.urlretrieve(
        url, (work_directory_active + mod_zip_dir))

    mod_zip_location = (work_directory_active + mod_zip_dir)


    if os.path.isfile(work_directory_active + mod_zip_dir) == True:
            pass

    else:
            print('\nThe downloading process is being a real dork. Report it on my')
            print('github, and I will try to get back to you shortly.\n')
            raise SystemExit

    with zipfile.ZipFile((work_directory_active + 'Bully.WidescreenFix.zip'), 'r') as zip_ref:
            zip_ref.extractall((work_directory_active))
            
    print("Widescreen fixed installed!")
    
    os.system('clear')
    
    if photo_help == '1':
        placeholder = Image.open(current_dir + '/Images/Bully_end_help.png')
        placeholder.show()
    
    print("""Some last steps before you're finished. Some things are unfortunately unable to
be optimized at this point and time.\n
First, go to the Properties for Bully in your Steam library again.
For the launch options, copy the text inside the equal signs, and paste it into the box:
=====================================================================
PROTON_USE_WINED3D=1 WINEDLLOVERRIDES="dinput8.dll=n,b" %command%
=====================================================================
\n\nThe WINEDLLOVERRIDES part lets Proton know to use the mods' files instead of its' own.
\nThe PROTON_USE_WINED3D is thankfully only something we need to run once.
\nSelect the Compatibility option on the side of the window, and make sure you have both
have the "Force the use of specific Steam Play Compatibility tool" checked, as well as 
your selection of Proton being Proton 6.3-(X). As of right now, this is 6.3-7, but the 
seven could become another number down the road.
Any other choice of Proton can't be promised to work under the script; as I don't know 
what the future will bring, and only recent versions have been able to run videos properly.
\nStart the game after closing the Properties window. The main menu will not
load in correctly until you change the Video options. Set your Resolution, then set
Anti-Aliasing to either 1 or 2. This will fully fix the video for you.
Be sure to set Shadows before closing the game, and also turn on Vsync, as the mod is
said to micro-stutter without it on (60 FPS option still exists with Vsync on).
\nNow exit the game, and go back to properties. Remove the PROTON_USE_WINED3D=1 text
completely from the box, leaving only WINEDLLOVERRIDES="dinput8.dll=n,b" %command%
\n\nAt this point, the game can be ran like normal and with high performance, with both
mods running well.""")

    input('\n\nWhen you no longer need this text, press Enter ...')
    
    os.system('clear')
        
    print('Thank you for taking the time to try Cactus_AVM.\n')
    print('After taking so much from the community over the years, this is a way I wish to give back.')
    print(' I hope you enjoy your time playing Bully; it is one of the best Rockstar Games. \n\n')
            
    os.remove((mod_zip_location))

else:
    print('Whelp, program cannot find what it just installed.')
    print('Do not blame yourself; I probably messed up somewhere.')
    print('\n\nPlease let me know on github if I have made a mistake so it can be fixed.')
    raise SystemExit
