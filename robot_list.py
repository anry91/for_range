from os import system
option = ''
robo_x = 5
gmap =[' ','💣',' ',' ',' ','🐧',' ','💣',' ',' ']
 ############   PRINT THE MAP   ############ 
hp = 100
while option != 'x':
    if hp == 0:
        system('cls')
        print('YOU LOSE')
        break
    system("cls")
    print("-"*20)
    
    for i in range(len(gmap)):
        print(gmap[i], end= " ")
    print()

    print("-"*20)

    for i in range(len(gmap)):
        print(i, end= " ") 
    print()
    print(f"HP: {hp}")
    
    print("\nCONTROLS: a - left, d - right, x - exit ")
    option = input(">>>  ")
    if option == 'a' and  0 < robo_x:
        gmap[robo_x] =' '
        robo_x -=1
        if gmap[robo_x] == '💣':
            gmap[robo_x] = "💀"
            hp -=50
        else:
            gmap[robo_x] = "🐧"
    elif option == 'd' and (len((gmap)) -1 ) > robo_x:
        gmap[robo_x] =' '
        robo_x +=1
        if gmap[robo_x] == '💣':
            gmap[robo_x] = "💀"
            hp -=50
        else:
            gmap[robo_x] = "🐧"
    elif option == 'x':
        print('Game Over')
    
    