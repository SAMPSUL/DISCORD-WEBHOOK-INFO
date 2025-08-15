#webhook info made by SAMPSUL
import requests
import time
import os
import sys

BLUE = "\033[34m"
RED = "\033[31m"
LIGHT_BLUE = "\033[94m"
RESET = "\033[0m"

os.system("title WEBHOOK INFO BY SAMPSUL")

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(BLUE + r"""
              ___.   .__                   __     .__        _____       
__  _  __ ____\_ |__ |  |__   ____   ____ |  | __ |__| _____/ ____\____  
\ \/ \/ // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / |  |/    \   __\/  _ \ 
 \     /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  |  |   |  \  | (  <_> )
  \/\_/  \___  >___  /___|  /\____/ \____/|__|_ \ |__|___|  /__|  \____/ 
             \/    \/     \/                   \/         \/        
                             GITHUB: SAMPSUL             
""" + RESET)
typewriter(LIGHT_BLUE + "DISCORD WEBHOOK INFO MADE BY SAMPSUL" + RESET)

while True:
    webhook_url = input(LIGHT_BLUE + "Put Discord webhook here: " + BLUE).strip()

    try:
        r = requests.get(webhook_url)
        
        if r.status_code == 200:
            data = r.json()
            print(LIGHT_BLUE + "\nWebhook is active!" + RESET)
            typewriter(LIGHT_BLUE + f"Name: {data.get('name')}" + RESET)
            typewriter(LIGHT_BLUE + f"Channel ID: {data.get('channel_id')}" + RESET)
            typewriter(LIGHT_BLUE + f"Server  ID: {data.get('guild_id')}" + RESET)
            if data.get('avatar'):
                typewriter(LIGHT_BLUE + f"Avatar URL: https://cdn.discordapp.com/avatars/{data.get('id')}/{data.get('avatar')}.png" + RESET)
            else:
                typewriter(LIGHT_BLUE + "Avatar URL: none" + RESET)
        else:
            print(RED + f"Webhook does not work: {r.status_code}" + RESET)

    except Exception as e:
        print(RED + "Error: " + str(e) + RESET)

    again = input("\nDo you want to check another webhook? (yes/no): ").lower()
    if again == "no":
        break

typewriter("Program is closing...")
time.sleep(1)
