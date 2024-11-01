# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
inventory = []
player_alive = True

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi' , 'dzīvojamo istabu' un 'otro stāvu' .")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba", "otrais stāvs"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        elif choice == "otrais stāvs":
             floor()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi un atslēgu no pagraba. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem", "aizvērtu"]:
        choice = input(">>> ").lower()
        if choice == "ņem":
            inventory.append("nazis")
            print("Tu paņēmi nazi.")
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        action = input(">>> ").lower()
        if action == "cīnīties":
            if "nazis" in inventory:
                print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game()
        elif action == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai tu vēlies 'skatīties' spogulī vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["skatīties", "atpakaļ"]:
        choice = input(">>> ").lower()
        if choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            end_game()
        elif choice == "atpakaļ":
            foyer()
        else:
            print("Nepareiza izvēle.")

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = ""
    while choice != "atvērt":
        choice = input(">>> ").lower()
        if choice == "atvērt":
            if "atslēga" in inventory:
                print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
                end_game()
            else:
                print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
                basement()
        else:
            print("Nepareiza izvēle.")
            foyer()

def istaba():
    print("Tu atver durvis un redzi uz galda divas kastes. Atvērt 'pirmo', 'otro', vai 'iet atpakaļ' ")
    choice = ""
    while choice not in ["pirmo", "otro", "iet atpakaļ"]:
        choice = input(">>> ").lower()
        if choice == "pirmo":
            kitchen()
        elif choice == "otro":
            print("Tu atveri otro kasti un viņa")
        elif choice == "iet atpakaļ":
             floor()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")
    
def floor():
    print("Tu ej pa kāpnēm un redzi divas durvis. Vai tu vēlies iet uz 'pirmo' vai uz 'otro' durvi?")
    choice = ""
    while choice not in ["pirmo", "otro"]:
        choice = input(">>> ").lower()
        if choice == "pirmo":
            istaba()
        elif choice == "otro":
            print("Tu esi istabā, grīda saplīs un tu esi atkal netālu no foaje")
            foyer()
        else:
            print("Nepareiza izvēle.")

  
   

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
