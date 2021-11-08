import random
import json

# import ZombieGame.health
phealth = 100
zhealth = 100


def mainGame():
    global phealth
    global zhealth
    zombie = input("A zombie approaches you what do you do? 'a' for attack, 'd' to dodge, 'n' to do nothing\n")
    print(zombie)
    if zhealth <= 0:
        gameOver_zom()
    if phealth <= 0:
        gameOver_pl()
    if zombie == 'n':
        dam = random.randrange(10, 30, 10)
        if dam == 10:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 10
                    print(f"The Zombie hit you and dealt 10 damage! \n Your health is now %{phealth}")
                    return mainCont()
        if dam == 20:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 20
                    print(f"The Zombie hit you and dealt 20 damage! \n Your health is now %{phealth}")
                    return mainCont()
        if dam == 30:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 30
                    print(f"Critical! \n The Zombie hit you and your health is now %{phealth}")
                    return mainCont()

    if zombie == 'd':
        num = random.randint(1, 2)
        dam = random.randrange(10, 30, 10)
        if num == 1:
            print("Dodge was successful no damage dealt towards you!")
            return mainCont()
        if num == 2:
            print("The dodge was unsuccessful and the zombie hit you!")
            if dam == 10:
                try:
                    check()
                finally:
                    if phealth == 0:
                        check()
                    else:
                        phealth -= 10
                        print(f"The Zombie hit you and dealt 10 damage! \n Your health is now %{phealth}")
                        return mainCont()
            if dam == 20:
                try:
                    check()
                finally:
                    if phealth == 0:
                        check()
                    else:
                        phealth -= 20
                        print(f"The Zombie hit you and dealt 20 damage! \n Your health is now %{phealth}")
                        return mainCont()
            if dam == 30:
                try:
                    check()
                finally:
                    if phealth == 0:
                        check()
                    else:
                        phealth -= 30
                        print(f"Critical! \n The Zombie hit you and your health is now %{phealth}")
                        return mainCont()

    if zombie == 'a':
        num = random.randrange(10, 40, 10)
        if num == 10:
            try:
                check()
            finally:
                if zhealth == 0:
                    check()
                else:
                    zhealth -= 10
                    print(f"The attack was successful! \n Zombies health is now %{zhealth}")
                    return mainCont()
        if num == 20:
            try:
                check()
            finally:
                if zhealth == 0:
                    check()
                else:
                    zhealth -= 20
                    print(f"The attack was successful! \n Zombies health is now %{zhealth}")
                    return mainCont()
        if num == 30:
            try:
                check()
            finally:
                if zhealth == 0:
                    check()
                else:
                    zhealth -= 30
                    print(f"Critical! \n Zombies health is now %{zhealth}")
                    return mainCont()


def mainCont():
    global phealth
    global zhealth
    zombie = input("What do you do? 'a' for attack, 'd' to dodge, 'n' to do nothing\n")
    print(zombie)
    if zombie == 'n':
        dam = random.randrange(10, 30, 10)
        if dam == 10:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 10
                    print(f"The Zombie hit you and dealt 10 damage! \n Your health is now %{phealth}")
                    return mainCont()
        if dam == 20:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 20
                    print(f"The Zombie hit you and dealt 20 damage! \n Your health is now %{phealth}")
                    return mainCont()
        if dam == 30:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 30
                    print(f"The Zombie hit a critical on you and dealt 30 damage! \n Your health is now %{phealth}")
                    return mainCont()

    if zombie == 'd':
        num = random.randint(1, 2)
        dam = random.randrange(10, 30, 10)
        if num == 1:
            print("Dodge was successful no damage dealt towards you!")
            return mainCont()
        if num == 2:
            print("The dodge was unsuccessful and the zombie hit you!")
            if dam == 10:
                try:
                    check()
                finally:
                    if phealth == 0:
                        check()
                    else:
                        phealth -= 10
                        print(f"The Zombie hit you and dealt 10 damage! \n Your health is now %{phealth}")
                        return mainCont()
        if dam == 20:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 20
                    print(f"The Zombie hit you and dealt 20 damage! \n Your health is now %{phealth}")
                    return mainCont()
        if dam == 30:
            try:
                check()
            finally:
                if phealth == 0:
                    check()
                else:
                    phealth -= 30
                    print(f"The Zombie hit a critical on you and dealt 30 damage! \n Your health is now %{phealth}")
                    return mainCont()

    if zombie == 'a':
        num = random.randrange(10, 40, 10)
        do = random.randrange(0, 2, 8)
        if do <= 6:
            if num == 10:
                try:
                    check()
                finally:
                    if zhealth == 0:
                        check()
                    else:
                        zhealth -= 10
                        print(
                            f"The Attack was successful and you dealt 10 damage! \n The Zombies health is now %{zhealth}")
                        return mainCont()
            if num == 20:
                try:
                    check()
                finally:
                    if zhealth == 0:
                        check()
                    else:
                        zhealth -= 20
                        print(
                            f"The Attack was successful and you dealt 20 damage! \n The Zombies health is now %{zhealth}")
                        return mainCont()
            if num == 30:
                try:
                    check()
                finally:
                    if zhealth == 0:
                        check()
                    else:
                        zhealth -= 30
                        print(f"Critical! \n The Zombies health is now %{zhealth}")
                        return mainCont()
        else:
            if zhealth == 0:
                check()
            if phealth == 0:
                check()
            else:
                print(f"The Zombie dodged the attack! No damage dealt towards the Zombie!")
                return mainCont()


def check():
    if zhealth <= 0:
        gameOver_zom()
    if phealth <= 0:
        gameOver_pl()


def nextGame():
    global zhealth, phealth
    cont = input("Would you like to continue? (Y) Yes (N) No")
    if cont == 'n':
        return dont_cont()
    if cont == 'y':
        phealth = 100
        zhealth = 100
        return mainGame()


def gameOver_zom():
    print("You have killed the Zombie! \n Congratulations!")
    nextGame()


def gameOver_pl():
    print("You have died! \n Better luck next time!")
    nextGame()


def dont_cont():
    print("Thanks for playing!")
    nextGame()


mainGame()
