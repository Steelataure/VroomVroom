
xv, yv = 100, 70  # position x et y de la voiture
vyv, vxv = 0, 0   # vitesse x et y de la voiture

temps = 0  # temps en seconde

ox, oy = 2000, 2000  # position x et y de l'image 

scoreX, scoreY = 665, 268  # position x et y du score

menuX, menuY = 0 , 000  # position x et y du menu

finx, finy  = 650, 200  # position x et y de l'arriver


def setup():
    size(800,600)
    frameRate(60)
    stroke(0)
    
    global myImageBackground, myImagefond, myImage
    
    myImageBackground = loadImage("menu.png")               #Image du menu
    myImagefond = loadImage("fond.png")                     #Image du fond de jeu
    myImage = loadImage("scorduplus.png")
    

overLeftButton = False


def draw():
    global xv, yv,\
    overLeftButton, menuX, menuY,\
    myImagefond, myImageBackground, MyImage, ox, oy,\
    scoreX, scoreY
    
    background(100)
    image(myImagefond, 0, 0)
    
    move_voiture()
    hitbox()
    fin()
    bordure() 
    score()
    
    image(myImage, ox, oy)
    image(myImageBackground, menuX,menuY)
    
    if overLeftButton:
        menuX = 1000
        menuY = 1000
    
    if xv > 650 and 301 < yv < 320:
        scoreX = 300
        scoreY = 288
    
        font = createFont("ka1.ttf" , 50)                    
        textFont(font)
    

def mousePressed():
    if overLeftButton:
        menuX = 1000

def mouseClicked():
    positionbouton()

def mouseDragged():
    positionbouton()

def positionbouton():
    global overLeftButton, overRightButton
    overLeftButton = 265 < mouseX < 520 and 250 < mouseY < 345
    overRightButton = 265 < mouseX < 520 and 250 < mouseY < 345
    

def score():
    global temps, scoreX, scoreY
    
    if keyPressed or keyCode:
        temps += 0.01667
        fill(0)
        text(str(round(temps, 2)), scoreX, scoreY)
        fill(0,200,20,120)
    

def move_voiture():
    global yv, xv, vyv, vxv, temps
    
    fill(0)
    ellipse(xv, yv, 20, 20)
    
    #Bordure de l'écran
    if yv > 590:
        vyv = -2
        temps += 0.5
    if yv < 10:
        vyv = 2
        temps += 0.5
    if xv > 790:
        vxv = -2
        temps += 0.5
    if xv < 10:
        vxv = 2
        temps += 0.5
    
    # Arret de la balle progressif
    if vyv > 0:
        vyv -= 0.15
    if vyv < 0:
        vyv += 0.15
    if vxv > 0:
        vxv -= 0.15
    if vxv < 0:
        vxv += 0.15
    
    if vyv < 0.15 and vyv > 0:
        vyv = 0
    if vyv < -0.15 and vyv > 0:
        vyv = 0
    if vxv < 0.15 and vxv > 0:
        vxv = 0
    if vxv < -0.15 and vxv > 0:
        vxv = 0
    
    xv += vxv
    yv += vyv
    

def keyPressed():
    global vyv, vxv
    '''
    if key == 'z':
        vyv += -1
    if key == 's':
        vyv += 1
    if key == 'q':
        vxv += -1
    if key == 'd':
        vxv += 1                    
    if key == 'e':
        vyv += -1
        vxv += 1
    if key == 'a':
        vyv += -1
        vxv += -1
    if key == 'w':
        vyv += 1
        vxv += -1
    if key == 'c':
        vyv += 1
        vxv += 1 
    
    '''
    if key == 'w':
        vyv += -1
    if key == 's':
        vyv += 1
    if key == 'a':
        vxv += -1
    if key == 'd':
        vxv += 1
    if key == 'w':
        vyv += -1
        vxv += 1
    if key == 'e':
        vyv += -1
        vxv += -1
    if key == 'v':
        vyv += 1
        vxv += -1
    if key == 'c':
        vyv += 1
        vxv += 1
    

    
    #Les 5 valeurs personnalisables des 5 rectangles ( x , y , longueur , Largeur)
 
rect_1x = 0
rect_1y = 150
rect_1l = 450
rect_1L = 50

rect_2x = 600
rect_2y = 150
rect_2l = 450
rect_2L = 50

rect_3x = 600
rect_3y = 150
rect_3l = 50
rect_3L = 290

rect_4x = 200
rect_4y = 390
rect_4l = 400
rect_4L = 50

rect_5x = 1000
rect_5y = 1000          
rect_5l = 4500
rect_5L = 5000


def bordure():
    global xv, yv, xx, xy,\
    rect_1x, rect_1y, rect_1l, rect_1L,\
    rect_2x, rect_2y, rect_2l, rect_2L,\
    rect_3x, rect_3y, rect_3l, rect_3L,\
    rect_4x, rect_4y, rect_4l, rect_4L,\
    rect_5x, rect_5y, rect_5l, rect_5L
    
    rect(rect_1x, rect_1y, rect_1l, rect_1L)
    rect(rect_2x, rect_2y, rect_2l, rect_2L)
    rect(rect_3x, rect_3y, rect_3l, rect_3L) 
    rect(rect_4x, rect_4y, rect_4l, rect_4L)  
    rect(rect_5x, rect_5y, rect_5l, rect_5L)
    fill(0, 180, 50, 180)
    
    
    fill(255)
    rect(rect_5x, rect_5y, rect_5l, rect_5L)
    
    if xv > 650 and 301 < yv < 320:
        rect_5x = 0
        rect_5y = 0
        rect_5l = 800
        rect_5L = 600

    fill(0, 200, 20, 120)


def hitbox():
    global xv, yv, vyv, vxv, temps
    
    
    if 140 < yv < 160 and 0 < xv < 455:
        vyv = -2
        temps += 0.5
    if 140 < yv < 210 and 450 < xv < 460:
        vxv = 2
        temps += 0.5
    if 190 < yv < 210 and 0 < xv < 455:
        vyv = 2
        temps += 0.5
    
    if 140 < yv < 160 and 599 < xv < 800:
        vyv = -2
        temps += 0.5
    if 140 < yv <390 and 590 < xv < 610:
        vxv = -2
        temps += 0.5
    if 380 < yv < 400 and 199 < xv < 595:
        vyv = -2
        temps += 0.5
    if 382 < yv < 448 and 190 < xv < 200:
        vxv = -2   
        temps += 0.5                                  
    if 430 < yv < 450 and 192 < xv < 658:
        vyv = 2
        temps += 0.5
    if 140 < yv < 449 and 650 < xv < 660:
        vxv = 2
        temps += 0.5


def fin():
    global xv, yv, vyv , vxv,\
    img ,oy ,ox,\
    finx, finy
    
    fill(0, 180, 50, 180)
    rect(finx, finy, 150, 90)
    fill(70, 160, 250, 100)
    textSize(60)
    fill(0)
    stroke(220)
    
    if xv > 650 and 200 < yv < 300:    #suite à faire , Si la balle va sur la fin elle se téléporte à 25 pour l'instant
        
        oy, ox = 0, 0
        fill(0)
        
        finx, finy = 900, 0
        vyv, vxv = 0, 0
        xv, yv = 750, 550

        noLoop()
