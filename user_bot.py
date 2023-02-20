def script(check, x, y):
    if (check("level") == 1):
        if (check("gold", x, y) != 0):
            return "take"
        if (check("wall", x + 2, y)):
            return "down"
        else:
            return "right"
    elif (check("level") == 2):
        if (check("gold", x, y) != 0):
            return "take"
        if (check("wall", x + 2, y) == False and check("wall", x, y + 1)):
            return "right"
        if (check("gold", x, y+1) != 0 ):
            return "down"
        if (check("wall", x, y - 1) == False):
            return "up"
        return "right"
    elif (check("level") == 3):
        if (check("gold", x, y) != 0):
            return "take"
        if (check("wall", x-1, y) == True and check("wall", x, y-1) == False):
            return "up"
        if (check("wall", x, y-1) == True and check("wall", x+1,y) == False):
            return "right"
        if (check("wall", x-1, y-1) == True and check("wall", x,y-1) == False):
            return "up"
        if (check("wall", x+1, y) == True and check("wall", x,y+1) == False):
            return "down"
        if (check("wall", x+1, y-1) == True and check("wall", x+1,y) == False):
            return "right"
        if (check("wall", x-1, y+1) == True and check("wall", x-1,y) == False):
            return "left"
        if (check("wall", x, y+1) == True and check("wall", x-1,y) == False):
            return "left"
        if (check("wall", x+1, y+1) == True and check("wall", x,y+1) == False):
            return "down"
    elif (check("level") == 4):
        if (check("gold", x, y) != 0):
            return "take"
        """
        if (check("player", 3, 16)):
            return "right"
        if (check("player", 4, 16)):
            return "right"
        if (check("player", 10, 13)):
            return "up"
        if (check("player", 10, 12)):
            return "up"
        """
        if (x==3 and y==16):
            return "right"
        if (x==4 and y==16):
            return "right"
        if (x==10 and y==13):
            return "up"
        if (x==10 and y==12):
            return "up"
        if (check("wall", x-1, y) == True and check("wall", x, y-1) == False):
            return "up"
        if (check("wall", x, y-1) == True and check("wall", x+1,y) == False):
            return "right"
        if (check("wall", x-1, y-1) == True and check("wall", x,y-1) == False):
            return "up"
        if (check("wall", x+1, y) == True and check("wall", x,y+1) == False):
            return "down"
        if (check("wall", x+1, y-1) == True and check("wall", x+1,y) == False):
            return "right"
        if (check("wall", x-1, y+1) == True and check("wall", x-1,y) == False):
            return "left"
        if (check("wall", x, y+1) == True and check("wall", x-1,y) == False):
            return "left"
        if (check("wall", x+1, y+1) == True and check("wall", x,y+1) == False):
            return "down"


    elif (check("level") == 5):
        if (check("gold", x, y) != 0):
            return "take"
        if (check("gold",x+1,y)!=0):
            return "right"

        else:
            if (check("gold",x,y+1)!=0):
                return "down"
            else:
                if (check("gold", x-1, y) != 0):
                    return "left"
                else:
                    if (check("gold", x, y - 1) != 0):
                        return "up"
        if ( y == 15 and (check("wall",x,y-1)==False)):
            return "left"
        if (check("wall",x+1,y)==False):
            return "right"
        else:
            if (check("wall",x,y+1)==False):
                return "down"
            else:
                if (check("wall",x-1,y)==False):
                    return "left"
                else:
                    return "up"


       # if (check("wall", x + 1, y) == True and check("wall", x, y-1) == True and check("wall", x + 1, y-1) == True and check("wall", x + 1, y+1) == False and check("wall", x + 1, y-2) == True):
          #  return "down"
       # if (check("wall", x + 1, y) == False):
        #    return "right"
       # if (check("wall", x + 1, y) == False):
       #     return "right"
       # if (check("wall", x, y+1) == False):
        #    return "down"
       # if (check("wall", x+1, y) == False and check("wall", x+2, y) == False and check("wall", x+1, y+1) == False):
      #      return "right"
       # if (check("wall", x, y+1) == False  and check("wall", x, y+2) == False and check("wall", x-1, y+1) == False):
       #     return "down"
      #  if (check("wall", x-1, y) == False  and check("wall", x-2, y) == False and check("wall", x-1, y-1) == False):
      #      return "left"
     #   if (check("wall", x, y-1) == False  and check("wall", x, y-2) == False and check("wall", x+1, y-1) == False):
     #       return "up"





    return "pass"
