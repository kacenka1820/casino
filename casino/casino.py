import random
    
red = 18/37
black = 18/37

money = int(input("Vlož peníze: "))

while True: 
    bet = int(input("Kolik chceš vsadit? "))

    
    color = input("Vyber si barvu mezi červenou a černou (anglicky): ")

    if color == 'red':  
        if random.random() <= red:
            money + 2*bet
            print("Padla červená, VYHRÁL SI")
            print("Zbývající peníze", money + 2*bet)
        else:
            money - bet
            print("Padla černá, PROHRÁL SI")
            print("Zbývající peníze", money - bet )
            

    elif color == 'black':
        if random.random() <= black:
            money + 2*bet
            print("Padla černá Vyhráli jste")
            print("Zbývající peníze", money + 2*bet)
        else:
            money - bet
            print("Padla červená. PROHRÁL SI")
            print("Zbývající peníze", money - bet)
        
    while money > 0:   
        conti = input("Chcete hrát dál? ")
        if conti.lower() != 'ne':
            break
        else:
            print("Konec hry")
                

