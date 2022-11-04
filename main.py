import os
import subprocess
from colorama import *
import time
import os



print(f"""{Fore.RED}
    ____  __  ______  _   _______  __    __  _____ ___    __      __  _______  __ __
   / __ \/ / / / __ \/ | / /  _/ |/ /   /  |/  / //_/ |  / /     /  |/  / __ \/ // /
  / /_/ / /_/ / / / /  |/ // / |   /   / /|_/ / ,<  | | / /_____/ /|_/ / /_/ / // /_
 / ____/ __  / /_/ / /|  // / /   |   / /  / / /| | | |/ /_____/ /  / / ____/__  __/
/_/   /_/ /_/\____/_/ |_/___//_/|_|  /_/  /_/_/ |_| |___/     /_/  /_/_/      /_/   
                                                                                    
""")

mkv = input("MKV file name (needs to be in the folder): ")

output_name = input("output name: ")
subprocess.run(
    ["ffmpeg", "-i", f"{mkv}", "-codec", "copy", f"result/{output_name}"], check=True)
os.system('cls' if os.name=='nt' else 'clear')
time.sleep(1)
print(f"{Fore.LIGHTGREEN_EX}Converting Done!")
time.sleep(0.5)
print(f"{Fore.LIGHTGREEN_EX}Opening results file...")
time.sleep(1)
os.startfile("result")
