lista = [1,1,2]
krotka = (1,1,2)

zbior = {3,1,2}

def setup ():
    frameRate(60)
    rectMode(CENTER)
    size(300,300)
    global x
    global y
    x = 0
    y = 0
def draw():
    global x
    x = x + 1 
    global y
    y = y + 1
    rect(height/2,width/2,x,y)
    if x > width:
        exit()
    
def mousePressed():
    #loop()
    #noLoop()
    #redraw()
    pass
    
       
    
    

    
