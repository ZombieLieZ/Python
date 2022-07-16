# Ez most egy chatbot lesz! :)
# pip install pywhatkit

import pywhatkit as kit

botname = input("Bot neve: ")
név = input("Neved: ")
start = input(f"{név}: ")



if start == "":
    print(f"{botname}: Ez még sajnos nincsen benne a szótáramban!")
    start = input(f"{név}: ")

if "Szia!" in start:
    print(f"{botname}: Hali!")
    start = input(f"{név}: ")

if f"Az én nevem {név}" in start:
    print(f"{botname}: Szép név! Az én nevem {botname}")
    start = input(f"{név}: ")

if "Hogy vagy?" in start:
    print(f"{botname}: Köszönöm, jól!")
    start = input(f"{név}: ")

if "Jól vagyok" in start:
    print("Ennek nagyon örülök!")
    start = input(f"{név}: ")

if "Rickroll" in start:
    kit.playonyt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    start = input(f"{név}: ")

if "youtube" in start:      # Ez elindít egy youtube videót azzal kapcsolatban amit beírtatok! pl: Sütemény készítés youtube
    kit.playonyt(start)
    start = input(f"{név}: ")

if "google" in start:     #Ez ugyan azt teszi mint a youtube, csak itt google keresőben keres rá a szövegre!
    kit.search(start)
    start = input(f"{név}: ")

if "Mennem kell" in start:
    print("Oh, okés, később találkozunk!")
    exit()

# Ezeket folytathatjátok saját kitalált párbeszédeitekkel ugyan így!
