small_ship = int(input("Enter coordinates: "))
big_ship =small_ship
big_ship_f = small_ship-1
big_ship_b = small_ship+1
if 1<big_ship<=9:      
    for x in range(1,11): 
        if x == big_ship:
            print( "W", end="" )
        elif x == big_ship_f:
            print("w", end="") 
        elif x == big_ship_b:
            print("w", end="")   
        else:
            print( "~", end="" )

else: 
    print("Wrog coordinates, please try again")