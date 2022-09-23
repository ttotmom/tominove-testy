import random
import uvodna_obrazovka
import time

def kocky():
    players= (int(input("Kolko hráčov hrá?: ")))
    od_do=(int(input("Kolko strannu kocku chcete hodit ?: ")))
    for _ in range(players):
        time.sleep(2)
        def hod_kockou(od_do): 
            return random.randint(1,od_do)
        print (hod_kockou(od_do))
    continue24=input ("Želáte si hrať znovu ? Ak áno zadajte 1, ak nie zadajte 0: ")
    if continue24 == "1": 
        kocky()
    else: 
        uvodna_obrazovka.menu()
         
        





if __name__ == "__main__":
    kocky()