# Créé par jenny, le 10/03/2024 en Python
# Créé par jenny, le 25/02/2024 en Python 3.7

"""
Programme du tron
nom(s), prÃ©nom(s), classe(s)
"""
import pygame, sys
from random import *
import csv

#constantes de la fenÃªtre d'affichage
LARGEUR=1000       #hauteur de la fenÃªtre
HAUTEUR=600      #largeur de la fenÃªtre
ROUGE=(255,0,0)     # dÃ©finition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)


#Utilisation de la bibliothÃ¨que pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenÃªtre
font = pygame.font.SysFont('comicsans', 20)     #choix de la police de caractÃ¨res
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//2
motoY=HAUTEUR//2
motoX1=LARGEUR//4
motoY1=HAUTEUR//4
x=LARGEUR//2
y=HAUTEUR//2
x1=LARGEUR//4
y1=HAUTEUR//4
direction = 'haut'
direction1 = 'z'
tempsPartie=0
tempsPartie1=0
pointV=0
pointB=0
chrono = pygame.time.get_ticks()
chrono1 = pygame.time.get_ticks()

#variable leaderboard
text=''
text1=''
tempsTotal=0
time=0
rank=0
rank1=0
y=200
#initialisation des images
surface = pygame.Surface((640,360),pygame.SRCALPHA)
image0 =pygame.transform.scale (pygame.image.load("menu.png"),(LARGEUR,HAUTEUR))
image1 =pygame.transform.scale (pygame.image.load("select_mode.png"),(LARGEUR,HAUTEUR))
image2 =pygame.transform.scale (pygame.image.load("settings.png"),(LARGEUR,HAUTEUR))
image3 =pygame.transform.scale (pygame.image.load("leaderboard.png"),(LARGEUR,HAUTEUR))
image4 =pygame.transform.scale (pygame.image.load("pause.png"),(LARGEUR,HAUTEUR))
image5=pygame.transform.scale (pygame.image.load("game_over.png"),(LARGEUR,HAUTEUR))
image6=pygame.transform.scale (pygame.image.load("won p1.png"),(LARGEUR,HAUTEUR))
image7=pygame.transform.scale (pygame.image.load("won p2.png"),(LARGEUR,HAUTEUR))

#lopp
loop=False
loop1=False
loop2=False
loop3=False
loop4=False
loop5=False
loop6=False
loop7=False
loop8=False
loop9=False
loop10=False

#click
click=False
click1=False
click2=False
click3=False

def menu():
    global click, click1
    global loop1, loop2, loop3
    while True:
        fenetre.blit(image0,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(380, 340, 270, 50)
        button_2 = pygame.Rect(345, 405, 310, 50)
        button_3 = pygame.Rect(260, 470, 500, 50)
        button_4 = pygame.Rect(375, 535, 270, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                click1=False
                loop1=True
                mode()
        if button_2.collidepoint((mx, my)):
            if click:
                loop2=True
                settings()
        if button_3.collidepoint((mx, my)):
            if click:
                loop3=True
                leaderboard()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(surface, (255, 0, 0), button_1)
        pygame.draw.rect(surface, (255, 0, 0), button_2)
        pygame.draw.rect(surface, (255, 0, 0), button_3)
        pygame.draw.rect(surface, (255, 0, 0), button_4)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def mode():
    global click, click1
    global loop, loop1, loop4
    while loop1:
        fenetre.blit(image1,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_5 = pygame.Rect(225, 400, 575, 90)
        button_6 = pygame.Rect(225, 500, 575, 90)
        button_7 = pygame.Rect(22, 22, 40, 40)
        if button_5.collidepoint((mx, my)):
            if click1:
                click1=False
                loop1=False
                loop4=True
                game()

        if button_6.collidepoint((mx, my)):
            if click1:
                click1=False
                loop1=False
                loop=True
                game1()

        if button_7.collidepoint((mx, my)):
            if click1:
                click1=False
                click=False
                loop1=False
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_5)
        pygame.draw.rect(surface, (255, 0, 0), button_6)
        pygame.draw.rect(surface, (255, 0, 0), button_7)

        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        pygame.display.update()

def settings():
    global click, click2
    global loop2
    while loop2:
        fenetre.blit(image2,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_8 = pygame.Rect(22, 22, 40, 40)

        if button_8.collidepoint((mx, my)):
            if click2:
                click=False
                click2=False
                loop2=False
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_8)

        click2 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click2 = True

        pygame.display.update()

def leaderboard():
    global click, click2
    global loop3, loop9
    global text, text1, text2
    global file
    global rank
    global y
    y=170
    with open("score.cvs", "r") as f1, open("rank.cvs", "r") as f2, open("score_2.cvs", "r") as f4, open("rank_2.cvs", "r") as f6:
                lecture_fichier1 = csv.DictReader(f1,delimiter=',')
                lecture_fichier2 = csv.DictReader(f2,delimiter=' ')
                lecture_fichier4 = csv.DictReader(f4,delimiter=',')
                lecture_fichier6 = csv.DictReader(f6,delimiter=' ')
                rank = []
                for ligne in lecture_fichier2:
                    rank.append(dict(ligne))
                f2.close()
                score = []
                for ligne in lecture_fichier1:
                    score.append(dict(ligne))
                f1.close()
                score.sort(key=lambda x: x ['score'], reverse=True)
                print(score)
                rank2 = []
                for ligne in lecture_fichier6:
                    rank2.append(dict(ligne))
                f6.close()
                score2 = []
                for ligne in lecture_fichier4:
                    score2.append(dict(ligne))
                f4.close()
                score2.sort(key=lambda x: x ['score'], reverse=True)

    fenetre.blit(image3,(0,0))
    for i in score:
        f1 = font.render(i['score'], True, (255, 255, 255))
        f3= font.render(i['name'], True, (255, 255, 255))
        fenetre.blit(f1,(300,y))
        fenetre.blit(f3,(400,y))
        y+=40
    y=170
    for i in rank :
        f2 = font.render(i['rank'], True, (255, 255, 255))
        fenetre.blit(f2,(200,y))
        y+=40
    y=170

    for j in score2:
        f4 = font.render(j['score'], True, (255, 255, 255))
        f5= font.render(j['name'], True, (255, 255, 255))
        fenetre.blit(f4,(650,y))
        fenetre.blit(f5,(750,y))
        y+=40
    y=170
    for j in rank2 :
        f6 = font.render(j['rank'], True, (255, 255, 255))
        fenetre.blit(f6,(550,y))
        y+=40

    while loop3:

        mx, my = pygame.mouse.get_pos()

        button_9 = pygame.Rect(22, 22, 40, 40)

        if button_9.collidepoint((mx, my)):
            if click2:
                click=False
                click2=False
                loop3=False
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_9)

        click2 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click2 = True

        pygame.display.update()

def game_over():
    global click, click1, click3
    global loop1, loop4, loop5
    global motoX, motoY
    global tempsPartie
    global direction
    global chrono
    global time
    print('perdu')
    print('temps partie',tempsPartie)
    while loop5:

        fenetre.blit(image5,(0,0))
        time=tempsPartie
        time = font.render(str(time), True, (255, 0, 0))
        fenetre.blit(time,(350,200))

        mx, my = pygame.mouse.get_pos()

        button_12 = pygame.Rect(260, 350, 450, 60)
        button_13 = pygame.Rect(175, 430, 650, 60)
        button_14 = pygame.Rect(350, 520, 300, 60)

        if button_12.collidepoint((mx, my)):
            if click3:
                click3=False
                loop5=False
                loop4=True
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                direction='haut'
                tempsPartie=0
                time=0
                game()

        if button_13.collidepoint((mx, my)):
            if click3:
                click1=False
                click3=False
                loop5=False
                loop1=True
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                direction='haut'
                tempsPartie=0
                time=0
                mode()

        if button_14.collidepoint((mx, my)):
            if click3:
                click=False
                click3=False
                loop5=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                direction='haut'
                tempsPartie=0
                time=0
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_12)
        pygame.draw.rect(surface, (255, 0, 0), button_13)
        pygame.draw.rect(surface, (255, 0, 0), button_14)

        click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True

        pygame.display.update()

def win_V():
    global click, click1, click3
    global loop1, loop, loop6
    global motoX, motoY, motoX1, motoY1
    global tempsPartie
    global direction, direction1
    global chrono
    global tempsTotal
    global pointB, pointV
    print('perdu')
    print('temps partie',tempsPartie)
    while loop6:

        fenetre.blit(image6,(0,0))
        time=tempsTotal
        time = font.render(str(time), True, (255, 0, 0))
        fenetre.blit(time,(300,275))

        mx, my = pygame.mouse.get_pos()

        button_15 = pygame.Rect(260, 350, 450, 60)
        button_16 = pygame.Rect(175, 430, 650, 60)
        button_17 = pygame.Rect(350, 520, 300, 60)

        if button_15.collidepoint((mx, my)):
            if click3:
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop6=False
                loop=True
                game1()

        if button_16.collidepoint((mx, my)):
            if click3:
                click1=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop6=False
                loop1=True
                mode()

        if button_17.collidepoint((mx, my)):
            if click3:
                click=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop6=False
                menu()


        pygame.draw.rect(surface, (255, 0, 0), button_15)
        pygame.draw.rect(surface, (255, 0, 0), button_16)
        pygame.draw.rect(surface, (255, 0, 0), button_17)

        click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True

        pygame.display.update()

def win_B():
    global click, click1, click3
    global loop1, loop, loop7
    global motoX, motoY, motoX1, motoY1
    global tempsPartie
    global direction, direction1
    global chrono
    global tempsTotal
    global pointV, pointB
    print('perdu')
    print('temps partie',tempsPartie)
    while loop7:

        fenetre.blit(image7,(0,0))
        time=tempsTotal
        time = font.render(str(time), True, (255, 0, 0))
        fenetre.blit(time,(300,275))

        mx, my = pygame.mouse.get_pos()

        button_18 = pygame.Rect(260, 350, 450, 60)
        button_19 = pygame.Rect(175, 430, 650, 60)
        button_20 = pygame.Rect(350, 520, 300, 60)

        if button_18.collidepoint((mx, my)):
            if click3:
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop7=False
                loop=True
                game1()

        if button_19.collidepoint((mx, my)):
            if click3:
                click1=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop7=False
                loop1=True
                mode()

        if button_20.collidepoint((mx, my)):
            if click3:
                click=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop7=False
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_18)
        pygame.draw.rect(surface, (255, 0, 0), button_19)
        pygame.draw.rect(surface, (255, 0, 0), button_20)

        click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True

        pygame.display.update()

def pause():
    global click, click1, click3
    global loop1, loop, loop9
    global motoX, motoY, motoX1, motoY1
    global tempsPartie
    global direction, direction1
    global chrono
    global tempsTotal
    global pointV, pointB
    print('perdu')
    print('temps partie',tempsPartie)
    while loop9:

        fenetre.blit(image4,(0,0))
        time=tempsTotal
        time = font.render(str(time), True, (255, 0, 0))
        fenetre.blit(time,(300,275))

        mx, my = pygame.mouse.get_pos()

        button_21 = pygame.Rect(300, 350, 450, 50)
        button_22 = pygame.Rect(300, 410, 450, 50)
        button_23= pygame.Rect(160, 470, 650, 50)
        button_24= pygame.Rect(300, 535, 400, 50)

        if button_21.collidepoint((mx, my)):
            if click3:
                click3=False
                loop9=False
                loop=True
                game1()

        if button_22.collidepoint((mx, my)):
            if click3:
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop9=False
                loop=True
                game1()

        if button_23.collidepoint((mx, my)):
            if click3:
                click1=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop9=False
                loop1=True
                mode()

        if button_24.collidepoint((mx, my)):
            if click3:
                click=False
                click3=False
                motoX=LARGEUR//2
                motoY=HAUTEUR//2
                motoX1=LARGEUR//4
                motoY1=HAUTEUR//4
                direction='haut'
                direction1='z'
                tempsPartie=0
                tempsTotal=0
                pointB=0
                pointV=0
                loop9=False
                menu()

        pygame.draw.rect(surface, (255, 0, 0), button_21)
        pygame.draw.rect(surface, (255, 0, 0), button_22)
        pygame.draw.rect(surface, (255, 0, 0), button_23)
        pygame.draw.rect(surface, (255, 0, 0), button_24)

        click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True

        pygame.display.update()

def dessineDecor():#SPAWN DES MOTOS
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-3, HAUTEUR-3],1)
    for i in range(randint(15,70)):
        obsx=randint(0, LARGEUR)
        obsy=randint(0, HAUTEUR)
        obsx1=randint(0, LARGEUR)
        obsy1=randint(0, HAUTEUR)
        r=randint(5, 25)
        l=randint(5, 50)
        L=randint(5, 25)
        if (motoX+10)!=obsx or (motoX+10)!=obsy or (motoX+10)!=obsx1 or (motoX+10)!=obsy1:
            pygame.draw.circle(fenetre, VERT, (obsx,obsy), r)      #cercle plein aux coord x,y de rayon 10
            pygame.draw.rect(fenetre, BLEU, [obsx1, obsy1, l, L],0)  #rectangle plein aux coord x,y

def dessineDecor1():# SPAWN DES MOTOS
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-3, HAUTEUR-3],1)
    for i in range(randint(25,50)):
        obsx=randint(0, LARGEUR)
        obsy=randint(0, HAUTEUR)
        obsx1=randint(0, LARGEUR)
        obsy1=randint(0, HAUTEUR)
        r=randint(5, 25)
        l=randint(5, 50)
        L=randint(5, 25)
        if (motoX+10)!=obsx or (motoX+10)!=obsy or (motoX+10)!=obsx1 or (motoX+10)!=obsy1:
            if (motoX1+10)!=obsx or (motoX1+10)!=obsy or (motoX1+10)!=obsx1 or (motoX1+10)!=obsy1:
                pygame.draw.circle(fenetre, VERT, (obsx,obsy), r)      #cercle plein aux coord x,y de rayon 10
                pygame.draw.rect(fenetre, BLEU, [obsx1, obsy1, l, L],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnÃ©es x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(afficheTexte,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto si c'est sssspossible
    """
    global motoX,motoY,x,y
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX     #a completer
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1     #a completer
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), VERT)
    return touche

def deplacementmoto1():
    """
    deplace la moto si c'est possible
    """
    global motoX1,motoY1,x1,y1
    touche1=False
    if direction1=='z':
        x1=motoX1
        y1=motoY1-1
        touche1=collisionMur(x1,y1)
    elif direction1=='s':
        x1=motoX1     #a completer
        y1=motoY1+1
        touche1=collisionMur(x1,y1)
    elif direction1=='d':
        x1=motoX1+1     #a completer
        y1=motoY1
        touche1=collisionMur(x1,y1)
    elif direction1=='q':
        x1=motoX1-1
        y1=motoY1
        touche1=collisionMur(x1,y1)
    if touche1==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX1=x1
        motoY1=y1
    fenetre.set_at((x1, y1), BLEU)
    return touche1

def restart():
    global loop, loop8
    global motoX, motoY, motoX1, motoY1
    global direction, direction1
    while loop8:
        motoX=LARGEUR//2
        motoY=HAUTEUR//2
        motoX1=LARGEUR//4
        motoY1=HAUTEUR//4
        direction='haut'
        direction1='z'
        loop8=False
        loop=True
        game1()

def game():
    fenetre.fill((0,0,0))
    dessineDecor()
    global deplacementmoto
    global loop4, loop5, loop9
    global tempsPartie
    global direction
    global chrono
    global text1
    global ligne
    global rank
    rank=0
    chrono = pygame.time.get_ticks()
    while loop4==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop4 = False            #fermeture de la fenÃªtre (croix rouge)
            if event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
                if event.key == pygame.K_ESCAPE or event.unicode == 'x': #touche q pour quitter
                    loop4 = False
                    loop9=True
                    pause()
                #fenetre.set_at((200, 200), color)

        keys = pygame.key.get_pressed()         #recupÃ©ration des touches appuyÃ©es en continu
        if keys[pygame.K_UP]:    #est-ce la touche UP
            direction = 'haut'
        elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
            direction = 'bas'
        elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
            direction = 'droite'
        elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
            direction = 'gauche'

        #fenetre.fill((0,0,0))   #efface la fenÃªtre, non utilisÃ© ici

        if deplacementmoto()==True:
            loop4=False
            loop5=True
            text1 = input("nom en 3 caractères majuscules")
            text1=text1.upper()
            compteur=0
            for n in range(0,len(text1)):
                compteur+=1
            if compteur!=3:
                text1 = input("nom en 3 caractères majuscules")
                text1=text1.upper()
            with open("score.cvs", "a") as fichier1:
                fichier1.write("\n")
                fichier1.write(str(tempsPartie))
                fichier1.write(",")
                fichier1.write(text1)
                fichier1.close()
            with open("score.cvs", "r") as fichier1, open("rank.cvs", "w") as fichier2:# reste a ranger dans l'ordre
                fichier2.write(str("rank"))
                fichier2.write(str("\n"))
                for ligne in fichier1:
                    rank+=1
                    fichier2.write(str(rank))
                    fichier2.write(str("."))
                    fichier2.write(str("\n"))
                fichier2.close()
                fichier1.close()
            game_over()
        frequence.tick(60)
        pygame.display.update() #mets Ã  jour la fenÃªtre graphique
        tempsPartie=(pygame.time.get_ticks() - chrono) / 1000

def game1():
    fenetre.fill((0,0,0))
    dessineDecor1()
    global deplacementmoto, deplacementmoto1
    global loop, loop6, loop7, loop8, loop9
    global tempsPartie1
    global direction, direction1
    global motoX, motoY, motoX1, motoY1
    global chrono1
    global pointB, pointV
    global tempsTotal
    global text, ligne
    global rank
    rank=1
    chrono1 = pygame.time.get_ticks()
    while loop==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False            #fermeture de la fenÃªtre (croix rouge)
            if event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
                if event.key == pygame.K_ESCAPE or event.unicode == 'x': #touche q pour quitter
                    loop = False
                    loop9=True
                    pause()
                #fenetre.set_at((200, 200), color)

        keys = pygame.key.get_pressed()         #recupÃ©ration des touches appuyÃ©es en continu
        if keys[pygame.K_UP]:    #est-ce la touche UP
            direction = 'haut'
        elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
            direction = 'bas'
        elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
            direction = 'droite'
        elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
            direction = 'gauche'

        if keys[pygame.K_z]:    #est-ce la touche UPs
            direction1 = 'z'
        elif keys[pygame.K_s]:  #est-ce la touche DOWN
            direction1 = 's'
        elif keys[pygame.K_d]:  #est-ce la touche RIGHT
            direction1 = 'd'
        elif keys[pygame.K_q]:  #est-ce la touche LEFT
            direction1 = 'q'


        #fenetre.fill((0,0,0))   #efface la fenÃªtre, non utilisÃ© ici

        if deplacementmoto()==True:
            pointB+=1
            tempsTotal+=tempsPartie1
            loop=False
            loop8=True
            restart()
        if deplacementmoto1()==True:
            pointV+=1
            tempsTotal+=tempsPartie1
            loop=False
            loop8=True
            restart()
        if pointV==3:
            loop=False
            loop6=True
            text = input("nom en 3 caractères majuscules")
            text=text.upper()
            compteur=0
            for n in range(0,len(text)):
                compteur+=1
            if compteur!=3:
                text = input("nom en 3 caractères majuscules")
                text=text.upper()
            with open("score_2.cvs", "a") as fichier1:
                fichier1.write("\n")
                fichier1.write(str(tempsTotal))
                fichier1.write(",")
                fichier1.write(text)
                fichier1.close()
            with open("score_2.cvs", "r") as fichier1, open("rank_2.cvs", "w") as fichier2:# reste a ranger dans l'ordre
                fichier2.write(str("rank"))
                fichier2.write(str("\n"))
                for ligne in fichier1:
                    fichier2.write(str(rank))
                    fichier2.write(str("."))
                    fichier2.write(str("\n"))
                    rank+=1
                fichier2.close()
                fichier1.close()
            win_V()
        if pointB==3:
            loop=False
            loop7=True
            text = input("nom en 3 caractères majuscules")
            text=text.upper()
            compteur=0
            for n in range(0,len(text)):
                compteur+=1
            if compteur!=3:
                text = input("nom en 3 caractères majuscules")
                text=text.upper()
            with open("score_2.cvs", "a") as fichier1:
                fichier1.write("\n")
                fichier1.write(str(tempsTotal))
                fichier1.write(",")
                fichier1.write(text)
                fichier1.close()
            with open("score_2.cvs", "r") as fichier1, open("rank_2.cvs", "w") as fichier2:# reste a ranger dans l'ordre
                fichier2.write(str("rank"))
                fichier2.write(str("\n"))
                for ligne in fichier1:
                    fichier2.write(str(rank))
                    fichier2.write(str("."))
                    fichier2.write(str("\n"))
                    rank+=1
                fichier2.close()
                fichier1.close()
            win_B()
        frequence.tick(60)
        pygame.display.update() #mets Ã  jour la fenÃªtre graphique
        tempsPartie1=(pygame.time.get_ticks() - chrono1) / 1000

menu()