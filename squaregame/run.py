# Script Modules
import platform
import sys
import colored
from colored import fore, back, style
import time

# Script Settings
from shared import GameName, system_required

# This script was made in linux, it may not work on other operating systems

# Seperator thing
if not platform.system() == system_required:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this script" + style.RESET)

import music
import game
