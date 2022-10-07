import turtle
import math
import time
import random
import uvodna_obrazovka
import fightgamehp








def fightgame2():
    Player_Health = 150
    Player_Damage = 7
    Easy_Health = 120
    Easy_Damage = 5
    Medium_Health = 150
    Medium_Damage = 7
    Hard_Health = 200
    Hard_Damage = 9
    widthdmg= 10
    ewidthdmg= -20
    mwidthdmg= 10
    hwidthdmg= 60
    
    
    while Easy_Health > 0 and Player_Health >0:           
        fightgamehp.canvas()

        if Player_Health == 150 : 
            fightgamehp.PlayerHP()  
            plyer_loss = turtle.Turtle(shape="square", visible=False)
            plyer_loss.color('black')
            plyer_loss.pensize("25")
            plyer_loss.shape("square")
            plyer_loss.penup()
            plyer_loss.goto(widthdmg,25)
            plyer_loss.pendown()        

        if Easy_Health == 120:
            fightgamehp.EasyHP()
            easy_loss = turtle.Turtle(shape="square", visible=False)
            easy_loss.color('black')
            easy_loss.pensize("25")
            easy_loss.shape("square")
            easy_loss.penup()
            easy_loss.goto(ewidthdmg,-16)
            easy_loss.pendown()

        if Easy_Health > 0:
            Edamage = random.randint(1, 10) * Easy_Damage
            Player_Health -= Edamage
            time.sleep(.5)     
            print("Máš " + str(Player_Health) + " životov.")
            widthdmg -= (Edamage-10)
            plyer_loss.goto (widthdmg,25)

        if Player_Health > 0:
            Pdamage = random.randint(1, 10) * Player_Damage
            Easy_Health -=  Pdamage
            time.sleep(.5)    
            print("Boss má " + str(Easy_Health) + " životov.")
            ewidthdmg -= (Pdamage-10)
            easy_loss.goto (ewidthdmg,-16)

        if Player_Health <= 0:
            won1=False
            print ("Prehral si ")
            plyer_loss.goto(-200,25)

        elif Easy_Health <= 0:
            won1=True
            print ("Vyhral si")
            easy_loss.goto(-200,-16)


    #tohle je strašná prasárna
    if won1 == True :
                time.sleep(.5) 
                continue1 = input("Ak chcete pokračovať zadajte 1, ak nie zadajte 0:\n")
                if continue1 == "1":
                    Player_Health=150
                    widthdmg = 10                    
                    while Medium_Health > 0 and Player_Health >0:
                        if Player_Health == 150 :           
                            fightgamehp.PlayerHP()

                        if Medium_Health == 150:
                            fightgamehp.MediumHP()

                        plyer_loss = turtle.Turtle(shape="square", visible=False)
                        plyer_loss.color('black')
                        plyer_loss.pensize("25")
                        plyer_loss.shape("square")
                        plyer_loss.penup()
                        plyer_loss.goto(widthdmg,25)
                        plyer_loss.pendown()

                        medium_loss = turtle.Turtle(shape="square", visible=False)
                        medium_loss.color('black')
                        medium_loss.pensize("25")
                        medium_loss.shape("square")
                        medium_loss.penup()
                        medium_loss.goto(mwidthdmg,-16)
                        medium_loss.pendown()

                        Mdamage = random.randint(1, 10) * Medium_Damage
                        Player_Health -= Mdamage
                        time.sleep(.5) 
                        print("Máš " + str(Player_Health) + " životov.")
                        widthdmg -= (Mdamage-10)
                        plyer_loss.goto (widthdmg,25)

                        if Player_Health > 0:

                            Pdamage = random.randint(1, 10) * Player_Damage
                            Medium_Health -=  Pdamage
                            time.sleep(.5) 
                            print("Boss má " + str(Medium_Health) + " životov.")
                            mwidthdmg -= (Pdamage-10)
                            medium_loss.goto (mwidthdmg,-16)

                        if Player_Health <= 0:
                            won2=False
                            print ("Prehral si ")
                            plyer_loss.goto(-200,25)
                        elif Medium_Health <= 0:
                            won2=True
                            print ("Vyhral si")
                            medium_loss.goto(-200,-16)

                    if won2 == True:
                        time.sleep(.5) 
                        continue2=input("Ak chcete pokračovať zadajte 1, ak nie zadajte 0:\n")
                        if continue2=="1":
                            Player_Health=150
                            widthdmg = 10
                            while Hard_Health > 0 and Player_Health >0:
                                if Player_Health == 150 :           
                                    fightgamehp.PlayerHP()

                                if Hard_Health == 200:
                                    fightgamehp.HardHP()

                                plyer_loss = turtle.Turtle(shape="square", visible=False)
                                plyer_loss.color('black')
                                plyer_loss.pensize("25")
                                plyer_loss.shape("square")
                                plyer_loss.penup()
                                plyer_loss.goto(widthdmg,25)
                                plyer_loss.pendown()

                                hard_loss = turtle.Turtle(shape="square", visible=False)
                                hard_loss.color('black')
                                hard_loss.pensize("25")
                                hard_loss.shape("square")
                                hard_loss.penup()
                                hard_loss.goto(hwidthdmg,-16)
                                hard_loss.pendown()

                                Hdamage = random.randint(1, 10) * Hard_Damage
                                Player_Health -= Hdamage
                                time.sleep(.5) 
                                print("Máš " + str(Player_Health) + " životov.")
                                widthdmg -= (Hdamage-10)
                                plyer_loss.goto (widthdmg,25)

                                if Player_Health > 0:

                                    Pdamage = random.randint(1, 10) * Player_Damage
                                    Hard_Health -=  Pdamage
                                    time.sleep(.5) 
                                    print("Boss má " + str(Hard_Health) + " životov.")
                                    hwidthdmg -= (Pdamage-10)
                                    hard_loss.goto (hwidthdmg,-16)

                                if Player_Health <= 0:
                                    won3=False
                                    print ("Prehral si ")
                                    plyer_loss.goto(-200,25)
                                elif Hard_Health <= 0:
                                    won3=True
                                    print ("Vyhral si")
                                    hard_loss.goto(-200,-16)

                            if won3 == True: 
                                continue3=input("Gratulujem, vyhral si! Ak chceš hrať znovu zadaj 1, ak nie zadaj 0:\n")
                                if continue3== "1":
                                    fightgame2()
                                else:
                                    uvodna_obrazovka.menu()

                            elif won3== False: 
                                loss3 =input("Ak chceš hrať znovu zadaj 1, ak nie zadaj 0 : \n")
                                if loss3 == "1":
                                    fightgame2()     
                                else:
                                    uvodna_obrazovka.menu()

                        else:
                            uvodna_obrazovka.menu()

                    elif won2== False: 
                        loss2 =input("Ak chceš hrať znovu zadaj 1, ak nie zadaj 0 : \n")
                        if loss2 == "1":
                            fightgame2()     
                        else:
                            uvodna_obrazovka.menu()

                else:
                    uvodna_obrazovka.menu()

    elif won1 == False:
        loss1 =input("Ak chceš hrať znovu zadaj 1, ak nie zadaj 0 : \n")
        if loss1 == "1":
            fightgame2()     
        else:
                uvodna_obrazovka.menu()


if __name__ == "__main__":
    fightgame2()





#skoncil si s health barom medium bosa uz len hard bossa treba dokoncit 