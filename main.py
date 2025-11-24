inventory = [0]
vaultA = False
vaultB = False
vaultC = False
clue1 = False
clue2 = False
clue3 = False
endGame = False
watch = False
lives = 5


def lobby():
    done = False
    global clue1
    global clue2
    global clue3
    global endGame
    while not done and lives > 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You are in the lobby")
        print("Where do you want to look?")
        print("1: Go to the seating area")
        print("2: Go to the picture wall")
        print("3: Go back to main menu")
        response = int(input())
        if response == 1:
            print("You are at the seating area")
            print("Where do you want to look?")
            print("1: Search the trash can")
            print("2: Search under the seats")
            response2 = int(input())
            if response2 == 1:
                print("You find 2 items that catch your attention")
                print("A newspaper and an empty can of coke")
                print("Which one do you want to examine first?")
                print("1: Newspaper")
                print("2: Can of coke")
                response3 = int(input())
                if response3 == 1:
                    print("You see a lowercase letter bolded on the front page")
                    print("v")
                    print("You add this letter to your inventory for future reference")
                    inventory.append("v")
                    clue1 = True
                elif response3 == 2:
                    print("You see some numbers under the can")
                    print("357")
                    print("You add this number to your inventory for future reference")
                    inventory.append("357")
                    clue2 = True
            elif response2 == 2:
                print("You look under the seats")
                print("You find 2 items that catch your attention")
                print("You pick them up, hoping to find a clue")
                print("Unfortunately, these items are of no help")
        elif response == 2:
            print("You go to the picture wall")
            print("You look to examine the pictures")
            print("You see a couple sitting down in a park, a man running with music, and children on the swings")
            print("You add these observations to your inventory")
            inventory.append("Couple sitting down")
            inventory.append("A man running")
            inventory.append("Children on the swings")
            clue3 = True
        elif response == 3:
            done = True


def guards():
    done = False
    global endGame
    print("Hi there, how can I help you?")
    while not done and lives > 0:
        print("1: Bribe the guard for information")
        print("2: Go back to main menu")
        response = int(input())
        if response == 1:
            if not vaultA:
                print("Talk to receptionist for some information")
            if inventory[0] > 10:
                if clue1 and clue2 and clue3:
                    inventory[0] -= 10
                    print("today is a Very good day to count to 357, and go for a run")
                else:
                    print("Get all the clues in the lobby before you come to me")
            elif inventory[0] < 10 and vaultA:
                print("You don't have enough money to give me")
        elif response == 2:
            done = True


def vault1():
    global vaultA
    global lives
    global endGame
    done = False
    while not done and lives > 0 and not vaultA:
        password = input("Enter your password: ")
        correctPass = "map"
        if password == correctPass and not vaultA:
            vaultA = True
            print("Congrats! You opened vault 1")
            inventory[0] += 50
            inventory.append("Vault 1 password: map")
            print("You found $50 in this vault!")
            print("You add this password to your inventory")
            print("Do you want to go to vault 2?")
            print("1: Yes")
            print("2: No, go back to main menu")
            response = int(input())
            if response == 1:
                vault2()
            elif response == 2:
                done = True
                mainMenu()
        elif password != correctPass and not vaultA:
            lives -= 1
            print("You only have ", lives, " lives left")
            print("Do you want to try again or go back to main menu?")
            print("1: Try again")
            print("2: Back to main menu")
            response1 = int(input())
            if response1 == 1:
                print("Try again!")
            elif response1 == 2:
                done = True
                mainMenu()
            if lives == 0:
                endGame = True
    while vaultA and not vaultC and lives > 0:
        print("Do you want to go to vault 2?")
        print("1: Yes")
        print("2: No, go back to main menu")
        response = int(input())
        if response == 1:
            vault2()
        elif response == 2:
            mainMenu()

    if endGame:
        print("Can't do anything because you are arrested for life")


def vault2():
    global vaultB
    global lives
    global endGame
    done = False
    while not done and lives > 0 and not vaultB:
        password = input("Enter your password: ")
        correctPass = "v357run"
        if password == correctPass and not vaultB:
            vaultB = True
            inventory[0] += 50
            inventory.append("Vault 2 password: v357run")
            print("Congrats! You successfully opened vault 2")
            print("You add this password to your inventory")
            print("You found 50 dollars which have been added to your inventory")
            print("You need to unlock the main vault to be able to escape and win this escape room")
            print("Do you want to go to vault 3?")
            print("1: Yes")
            print("2: No, go back to main menu")
            response = int(input())
            if response == 1:
                mainVault()
            elif response == 2:
                done = True
                mainMenu()
        elif password != correctPass and not vaultB:
            lives -= 1
            print("You only have ", lives, " lives left")
            print("Do you want to try again or go back to main menu?")
            print("1: Try again")
            print("2: Back to main menu")
            response1 = int(input())
            if response1 == 1:
                print("Try again!")
            elif response1 == 2:
                done = True
                mainMenu()
            if lives == 0:
                endGame = True
    while vaultB and not vaultC and lives > 0:
        print("Do you want to go to vault 3?")
        print("1: Yes")
        print("2: No, go back to main menu")
        response = int(input())
        if response == 1:
            mainVault()
        elif response == 2:
            mainMenu()

    if endGame:
        print("Can't do anything because you are arrested for life")


def mainVault():
    global vaultC
    global lives
    global endGame
    done = False
    while not done and lives > 0 and not vaultC:
        password = input("Enter the password: ")
        correctPassword = "brownies"
        if password == correctPassword:
            vaultC = True
            print("Congrats! You successfully opened vault 3")
            done = True
            lives = -1
        else:
            lives -= 1
            print("You only have ", lives, " lives left")
            print("Do you want to try again or go back to main menu?")
            print("1: Try again")
            print("2: Back to main menu")
            response1 = int(input())
            if response1 == 1:
                print("Try again!")
            elif response1 == 2:
                done = True
                mainMenu()
            if lives == 0:
                endGame = True

    if endGame:
        print("Can't do anything because you are arrested for life")
    if vaultA and vaultB and vaultC:
        print("You have successfully opened all 3 vaults and have successfully escaped this escape room")


def store():
    done = False
    global watch
    print("Welcome to the store")
    print("Your goal is to find 4 letters hidden around and spell the word out in order to get a watch for the "
          "receptionist")
    while not done and lives > 0 and not watch:
        print("Where do you want to go")
        print("1: Snack aisle")
        print("2: Makeup Aisle")
        print("3: Cashier")
        print("4: Try the password")
        print("5: Back to Main Menu")
        response = int(input())
        if response == 1:
            print("You are in the snack aisle")
            print("You see 3 snacks that catch your eye")
            print("Hot Cheetos, Oreos, Elma Chips")
            print("What do you want to do?")
            print("1: Examine items")
            print("2: Ignore these items")
            response1 = int(input())
            if response1 == 1:
                print("You find clues in the names of these brands")
                print("The letters E, H, and O are bolded")
                print("You save this to your inventory for future use")
                inventory.append("E")
                inventory.append("H")
                inventory.append("O")
            elif response1 == 2:
                print("Back to main menu")
        elif response == 2:
            print("You are in the makeup aisle")
            print("You find 3 items")
            print("Madison Reed, Chanel, Estee Lauder")
            print("What do you want to do?")
            print("1: Examine items")
            print("2: Ignore these items")
            response2 = int(input())
            if response2 == 1:
                print("You find clues in the names of these brands")
                print("The letter M is bolded")
                print("You save this to your inventory for future use")
                inventory.append("M")
            elif response2 == 2:
                print("Back to main menu")
        elif response == 3:
            print("You are at the cashier")
            print("You find 1 item")
            print("a barcode scanner with the letter R")
            print("What do you want to do?")
            print("1: Examine items")
            print("2: Ignore these items")
            response3 = int(input())
            if response3 == 1:
                print("You don't find any major clues in this, and it was mostly just a waste of time")
            elif response3 == 2:
                print("Back to main menu")
        elif response == 4:
            password = input("Enter the password to get the watch: ")
            correctPassword = "home"
            if password == correctPassword:
                print("Correct Password")
                print("You have successfully gotten the watch")
                watch = True
            else:
                print("Wrong")
        elif response == 5:
            done = True
    while watch and lives > 0 and not done:
        print("You have already found the watch")
        done = True


def bankHouse():
    done = False
    while not done and lives > 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You are in the bank owner's House")
        print("Where do you want to look?")
        print("1: Go to the living room")
        print("2: Go to the kitchen")
        print("3: Go back to main menu")
        response = int(input())
        if response == 1:
            print("You are in the living room")
            print("Where do you want to look?")
            print("1: Under the couch")
            print("2: Behind the TV")
            print("3: Go back to house main menu")
            response1 = int(input())
            if response1 == 1:
                print("You look under the couch and you find the TV remote")
                print("You can either keep this remote or ignore it")
                print("1: Keep it")
                print("2: Ignore it")
                response2 = int(input())
                if response2 == 1:
                    print("This remote has been added to your inventory")
                    inventory.append("TV remote")
                elif response2 == 2:
                    print("You ignore this item")
            elif response1 == 2:
                print("You look behind the TV")
                print("You find a recipe on how to make brownies")
                print("You can either keep this recipe or ignore it")
                print("1: Keep it")
                print("2: Ignore it")
                response3 = int(input())
                if response3 == 1:
                    print("This recipe has been added to your inventory")
                    inventory.append("BROWNIES Recipe")
                elif response3 == 2:
                    print("You ignore this item")
            elif response1 == 3:
                print("Back to house main menu")
        elif response == 2:
            print("You are in the kitchen")
            print("Where would you like to look?")
            print("1: In the cabinets")
            print("2: In the microwave")
            print("3: In the sink")
            print("4: Back to house main menu")
            response4 = int(input())
            if response4 == 1:
                print("You look in the cabinets")
                print("You find Brownies")
                print("You can either keep these in your inventory or ignore it")
                print("1: Keep it")
                print("2: Ignore it")
                response5 = int(input())
                if response5 == 1:
                    print("These Brownies have been added to your inventory for future reference")
                    inventory.append("BROWNIES")
                elif response5 == 2:
                    print("You ignore this item")
            elif response4 == 2:
                print("Unfortunately there is nothing in the microwave")
            elif response4 == 3:
                print("You look in the sink")
                print("You find plates that need to be washed")
                print("Do you want to examine closer or ignore these plates?")
                print("1: Examine closer")
                print("2: Ignore")
                response6 = int(input())
                if response6 == 1:
                    print("You examine the plates closer but unfortunately don't find much")
                elif response6 == 2:
                    print("You ignore the plates")
            elif response4 == 4:
                print("Back to house main menu")
        elif response == 3:
            done = True


def receptionist():
    done = False
    global endGame
    global watch
    print("Hi! You need to get me a watch from the store in order to get information")
    while not done and lives > 0:
        if watch:
            print("Thanks for the watch")
            print("How can I help you?")
            print("1: Ask for help to get into vault 1")
            print("2: Go to vault1")
            print("3: Back to main menu")
            response = int(input())
            if response == 1:
                print("Remember you only have 5 lives")
                print("If you get a password wrong then you lose a life, and if you lose all your lives then the cops "
                      "will be called")
                print(
                    "I have cities, but no people. I have rivers, but no fish, I have roads, but no traffic signs. What"
                    " am I?")
            elif response == 2:
                vault1()
            elif response == 3:
                done = True
        else:
            print("You don't have the watch")
            done = True


def mainMenu():
    done = False
    global endGame
    while not done and lives > 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("What do you want to do?")
        print("1: Talk to guards")
        print("2: Talk to receptionist")
        print("3: Go to the lobby")
        print("4: Go to the store")
        print("5: Go to the bank owner's house")
        print("8: Inventory")
        response = int(input())
        if response == 1:
            guards()
        elif response == 2:
            receptionist()
        elif response == 3:
            lobby()
        elif response == 4:
            store()
        elif response == 5:
            bankHouse()
        elif response == 8:
            print(inventory)


def main():
    mainMenu()


main()
