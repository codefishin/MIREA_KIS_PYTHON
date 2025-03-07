def script(check, x, y):
    if check("gold", x, y) != 0: return "take"

    if check("level") == 1:
        if check("wall", x + 2, y) == 1:
            return "down"
        return "right"
    if check("level") == 2:
        if check("gold", x + 1, y) != 0: return "right"
        if check("gold", x, y + 1) != 0: return "down"
        if check("gold", x, y - 1) != 0: return "up"
        if check("gold", x + 2, y) != 0: return "right"
        if check("gold", 1, y - 1) == 0 and check("wall", x, y - 1) == False: return "up"
        return "right"
    
    if check("level") == 3: # var 1
        if (check("wall", x, y + 1) == True or check("wall", x, y - 1) == True) and check("wall", x + 1, y) == False and check("gold", 1, 16) != 0: return "right"
        if (check("wall", x - 1, y) == True or check("wall", x + 1, y) == True) and check("wall", x, y - 1) == False and check("gold", 1, 16) != 0: return "up"
        if (check("wall", x - 1, y) == True or check("wall", x + 1, y) == True) and check("wall", x, y - 1) == False and check("gold", 1, 16) != 0: return "up"
        if check("gold", x, y - 3) != 0 or check("gold", x, y - 2) != 0: return "up"
        if check("gold", x, y - 1) != 0: return "up"
        if check("gold", x, y + 1) != 0: return "down"
        if check("gold", x + 1, y) != 0: return "right"
        if check("wall", x + 1, y) == True and check("wall", x, y + 1) == False: return "down"
        if check("gold", 1, 16) != 0: return "left"
        if check("gold", 26, 16) != 0: return "right"
        if check("gold", 26, 23) != 0: return "down"
        if check("gold", 19, 23) != 0: return "left"
        if check("gold", 19, 1) != 0: return "up"
        # моё лицо когда перебор координат
        if check("gold", 26, 1) != 0: return "right"
        if check("gold", 26, 8) != 0: return "down"
        if check("gold", 1, 8) != 0: return "left"
        if check("gold", 1, 1) != 0: return "up"
        if check("gold", 8, 1) != 0: return "right"
        return "down"
    if check("level") == 3: # var 2, по умнее типо
        if check('wall', x, y + 1) and check('wall', x - 1, y): return 'up'
        if check('wall', x, y - 1) and check('wall', x - 1, y): return 'right'
        if check('wall', x, y + 1) and check('wall', x + 1, y): return 'left'
        if check('wall', x, y - 1) and check('wall', x + 1, y): return 'down'
        if check('wall', x - 1, y): return 'up'
        if check('wall', x + 1, y): return 'down'
        if check('wall', x, y + 1): return 'left'
        if check('wall', x, y - 1): return 'right'
        if check('wall', x - 1, y - 1): return 'up'
        if check('wall', x + 1, y - 1): return 'right'
        if check('wall', x - 1, y + 1): return 'left'
        if check('wall', x + 1, y + 1): return 'down'
    if check("level") == 4:
        if check("wall", x - 1, y) == True and check("wall", x , y + 1) == False and check("gold", 8, 16) != 0: return "down"
        if check("wall", x, y + 1) == True and check("wall", x + 1, y) == False and check("gold", 8, 16) != 0: return "right"
        if check("wall", x, y - 1) == False and check("wall", x + 1, y) == True and check("gold", 8, 16) != 0: return "up"
        if check("wall", x + 1, y) == False and (check("wall", x + 1, y + 1) == True or check("wall", x + 1, y - 1) == True) and check("gold", 8, 16) != 0: return "up"
        if check("gold", 8, 16) != 0: return "down"
        if check("wall", x - 1, y) == False and check("wall", x, y - 1) == True and check("gold", 1, 16) != 0: return "left"
        if check("wall", x - 1, y) == False and (check("wall", x + 1, y - 1) == True or check("wall", x - 1, y - 1) == True) and check("gold", 1, 16) != 0: return "left"
        if check("gold", 1, 16) != 0: return "down"
        if check("wall", x + 1, y) == False and check("wall", x, y + 1) == True and check("gold", 26, 23) != 0: return "right"
        if check("wall", x + 1, y) == True and check("wall", x, y - 1) == False and check("gold", 26, 23) != 0: return "up"
        if check("wall", x + 1, y) == False and check("wall", x + 1, y + 1) == True and check("gold", 26, 23) != 0: return "right"
        if check("wall", x + 1, y) == False and check("gold", 26, 23) != 0: return "down"
        if check("gold", 26, 16) != 0: return "up"
        if check("gold", 19, 16) != 0: return "left"
        if check("wall", x, y - 1) == True and check("gold", 26, 1) != 0: return "right"
        if check("wall", x, y - 1) == False and check("gold", 26, 1) != 0: return "up"
        
        if check("gold", 26, 1) != 0: return "right"
        if check("gold", 26, 8) != 0: return "down"
        if check("gold", 19, 8) != 0: return "left"
        if check("gold", 19, 1) != 0: return "up"
        
        if check("wall", x - 1, y) == True and check("wall", x, y + 1) == False and check("gold", 17, 7) != 0: return "down"
        if (check("wall", x - 1, y + 1) or check("wall", x - 1, y - 1)) == True and check("wall", x, y + 1) == False and check("gold", 17, 7) != 0: return "down"
        if check("wall", x + 1, y) == False and check("wall", x, y + 1) == True and check("gold", 17, 7) != 0: return "right"
        if check("gold", 17, y - 1) != 0: return "up"
        if check("wall", x, y + 1) == False and check("wall", x - 1, y + 1) == True and check("gold", 17, 7) != 0: return "down"
        if check("wall", x, y + 1) == False and check("wall", x - 1, y) == True and check("gold", 17, 7) != 0: return "down"
        if check("wall", x - 1, y) == False and check("wall", x - 1, y - 2) == True and check("gold", 17, 7) != 0: return "left"
        if check("wall", x, y - 1) and check("gold", 17, 7) != 0: return "left"
        if check("gold", 17, 7) != 0: return "up"
        if check("gold", 10, 7) != 0: return "left"
        if check("gold", 10, 17) != 0: return "down"
        if check("gold", 17, 17) != 0: return "right"
        return "left"
    if check("level") == 5: # FVVV THIS
        if check("gold", x + 1, y): return "right"
        if check("gold", x - 1, y): return "left"
        if check("gold", x, y + 1): return "down"
        if check("gold", x, y - 1): return "up"

        if check("gold", x + 2, y): return "right"
        if check("gold", x - 2, y): return "left"
        if check("gold", x, y + 2): return "down"
        if check("gold", x, y - 2): return "up" 

        
        # RNG RNG RNG
        if check("wall", x, y - 1) and check("wall", x, y + 1) and check("wall", x - 1, y): return "right"
        if check("wall", x, y - 1) and check("wall", x, y + 1) and check("wall", x + 1, y): return "left"
        if check("wall", x + 1, y - 1) and check("wall", x, y - 1): return "left"
        if check("wall", x, y - 1) and check("wall", x, y + 1): return "right"
        if check("wall", x - 1, y - 1) and check("wall", x - 1, y) and check("wall", x, y - 1): return "right"
        if check("wall", x + 1, y) and check("wall", x - 1, y - 1) and check("wall", x - 1, y + 1): return "left"
        if check("wall", x - 1, y - 1) and check("wall", x - 1, y) and check("wall", x, y - 1): return "right"
        if check("wall", x + 1, y - 1) and check("wall",x, y - 1) and check("wall", x + 1, y): return "left"
        if check("wall", x, y - 1) and check("wall", x - 1, y): return "right"
        if check("wall", x, y - 1) and check("wall", x - 1, y - 1): return "right"
        if check("wall", x + 1, y - 1) and check("wall",x, y - 1) and check("wall", x + 1, y): return "left"

        if check("wall", x + 1, y) and check("wall", x + 1, y - 1) and check("wall", x, y - 1): return "up"
        if check("wall", x + 1, y) and check("wall", x + 1, y - 1) and check("wall", x, y - 1): return "up"
        if check("wall", x - 1, y) and check("wall", x + 1, y) and check("wall", x + 1, y - 1): return "down"
        if check("wall", x, y + 1) and check("wall", x - 1, y + 1): return "up"
        if check("wall", x - 1, y) and check("wall", x + 1, y): return "up"
        if check("wall", x - 1, y) and check("wall", x + 1, y) and check("wall", x, y - 1): return "down"
        if check("wall", x - 1, y) and check("wall", x + 1, y) and check("wall", x, y + 1): return "up"

        return "right"
    return "pass"
