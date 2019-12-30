import os
import time

os.system("clear")
is_game_on = True

start_or_not = ''

while start_or_not != "no":
    start_or_not = input("Do you want to play Terraria?: ").lower()

    if start_or_not == "yes":
        print("Starting your game...")
        time.sleep(2)
        os.system("steam steam://rungameid/105600 >/dev/null")
        time.sleep(5)
        os.system("xset r off")

        while is_game_on:
            stop = input("Say Stop To Stop Playing: ").lower()
            if stop == "stop":
                print("Exiting...")
                os.system("xset r on")
                time.sleep(3)
                os.system("pkill Main")
                os.system("clear")
                is_game_on = False
            else:
                print("Please say stop to stop playing!")

    elif start_or_not != "no":
        print("Please enter yes or no!")
print("Exiting...")
time.sleep(1)
os.system("clear")
