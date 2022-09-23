import turtle
import math
import time
import random
import uvodna_obrazovka 






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
    while Easy_Health > 0 and Player_Health >0:

        if Player_Health == 150 :           
            screen=turtle.Screen()
            screen.setup(width=300,height=100)
            screen.screensize(bg=("black"))
            plyer = turtle.Turtle(shape="square", visible=False)
            plyer.color('green')
            plyer.pensize("25")
            plyer.shape("square")
            plyer.penup()
            plyer.goto(-150,25)
            plyer.pendown()
            plyer.goto(0,25)


        plyer_loss = turtle.Turtle(shape="square", visible=False)
        plyer_loss.color('black')
        plyer_loss.pensize("25")
        plyer_loss.shape("square")
        plyer_loss.penup()
        plyer_loss.goto(widthdmg,25)
        plyer_loss.pendown()




        Edamage = random.randint(1, 10) * Easy_Damage
        Player_Health -= Edamage
        time.sleep(.5)     
        print("Máš " + str(Player_Health) + " životov.")
        widthdmg -= (Edamage-10)
        plyer_loss.goto (widthdmg,25)

        Pdamage = random.randint(1, 10) * Player_Damage
        Easy_Health -=  Pdamage
        time.sleep(.5)    
        print("Boss má " + str(Easy_Health) + " životov.")

        if Player_Health <= 0:
            won1=False
            print ("Prehral si ")
        elif Easy_Health <= 0:
            won1=True
            print ("Vyhral si")

    if won1 == True :
                time.sleep(.5) 
                continue1 = input("Ak chcete pokračovať zadajte 1, ak nie zadajte 0:\n")
                if continue1 == "1":
                    Player_Health=150
                    while Medium_Health > 0 and Player_Health >0:

                        Mdamage = random.randint(1, 10) * Medium_Damage
                        Player_Health -= Mdamage
                        time.sleep(.5) 
                        print("Máš " + str(Player_Health) + " životov.")

                        Pdamage = random.randint(1, 10) * Player_Damage
                        Medium_Health -=  Pdamage
                        time.sleep(.5) 
                        print("Boss má " + str(Medium_Health) + " životov.")

                        if Player_Health <= 0:
                            won2=False
                            print ("Prehral si ")
                        elif Medium_Health <= 0:
                            won2=True
                            print ("Vyhral si")

                    if won2 == True:
                        time.sleep(.5) 
                        continue2=input("Ak chcete pokračovať zadajte 1, ak nie zadajte 0:\n")
                        if continue2=="1":
                            Player_Health=150
                            while Hard_Health > 0 and Player_Health >0:

                                Hdamage = random.randint(1, 10) * Hard_Damage
                                Player_Health -= Hdamage
                                time.sleep(.5) 
                                print("Máš " + str(Player_Health) + " životov.")

                                Pdamage = random.randint(1, 10) * Player_Damage
                                Hard_Health -=  Pdamage
                                time.sleep(.5) 
                                print("Boss má " + str(Hard_Health) + " životov.")

                                if Player_Health <= 0:
                                    won3=False
                                    print ("Prehral si ")
                                elif Hard_Health <= 0:
                                    won3=True
                                    print ("Vyhral si")

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





