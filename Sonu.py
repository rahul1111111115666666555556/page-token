import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)   

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    logos = [
        r'''

          _________ _______                   
 |\     /|\__   __/(  ____ \|\     /||\     /|
 | )   ( |   ) (   | (    \/| )   ( || )   ( |
 | |   | |   | |   | (_____ | (___) || |   | |
 ( (   ) )   | |   (_____  )|  ___  || |   | |
  \ \_/ /    | |         ) || (   ) || |   | |
   \   /  ___) (___/\____) || )   ( || (___) |
    \_/   \_______/\_______)|/     \|(_______)
                                              
'''
    ]

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.GREEN + f"[+] APK3 MASSAG3 BHEJ DIYA GY4 HAI VISHANU KE TARAH SE😊 {message_index + 1} S3NT TO C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] FAIL3D T0 S3ND YOUR MASSAG3 {message_index + 1} T0 C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()
    
    print(Fore.MAGENTA + " 𝗧𝗛𝟯 𝗠𝟬𝗦𝗧 𝗪𝗔𝗡𝗧𝟯𝗗 𝗩𝗜𝗜𝗦𝗛𝟰𝗡𝗨 𝗙𝗧 𝗫𝗗 𝗧𝗢𝗢𝗟 𝗪𝟯𝗟𝗖𝟬𝗠𝟯 ")
    print(Fore.CYAN + "----------------𝗙𝗥𝟯𝟯 𝗧𝟬𝟬𝗟 𝗕𝗬 𝗢𝗪𝗡𝟯𝗥 𝗩𝟭𝗦𝗛𝟰𝗡𝗨 𝗥𝟰𝗝--------------------")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.MAGENTA + "𝗘𝗡𝗧𝟯𝗥 𝗧𝗛𝟯 𝗧𝗢𝗞𝟯𝗡 𝗜𝗗 𝗙𝗜𝗟𝗘 => ").strip()
    target_id = input(Fore.MAGENTA + "𝗘𝗡𝗧𝟯𝗥 𝗧𝗛𝟯 𝗚𝗥𝗢𝗨𝗣 𝗡𝗨𝗠 => ").strip()
    messages_file = input(Fore.MAGENTA + "𝗘𝗡𝗧𝟯𝗥 𝗧𝗛𝟯 𝗡𝗣/𝗔𝗕𝗨𝗦𝗘 𝗙𝗜𝗟𝗘 => ").strip()
    haters_name = input(Fore.MAGENTA + "𝗘𝗡𝗧𝟯𝗥 𝗧𝗛𝟯 𝗛𝗔𝗧𝟯𝗥-𝗡𝗔𝗠𝗘𝗦 => ").strip()
    speed = float(input(Fore.MAGENTA + "𝗘𝗡𝗧𝟯𝗥 𝗧𝗛𝟯 𝗦𝗣𝟯𝟯𝗗 𝗜𝗡 𝗦𝗘𝗖𝗢𝗡𝗗 𝗠𝗔𝗦𝗦𝗔𝗚𝟯 => ").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
