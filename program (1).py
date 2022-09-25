def turn_right():
    turn_left()
    turn_left()
    turn_left()
count=0   
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        count+=1
        if count==4:
            turn_left()
            
    elif front_is_clear():
        move()
        count=0
    else:
        turn_left()
        count=0
        
        
        
      
     