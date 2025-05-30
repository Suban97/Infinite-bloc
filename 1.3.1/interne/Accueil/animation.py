import pygame

carre = []
print("anima global")

def carre_function(): # crée la liste
    global carre
    carre = []
    print("animation carre function")
    for _ in range(200):
        carre.append(spawn_carre())



def spawn_carre(): #s'occupe de l'emplacement et de la vitesse 
    from random import randint
    return [randint(0, 800), randint(-150,0), randint(-2,2), randint(3,4), randint(2,7)]  # x, y viteese(x), vitesse(y), taille


def move_carre(fenetre): # s'occupe de l'apparition, du deplacement et de la dispariton hors de la fenetre
    for P in carre:
        P[0] += P[2] # x += vitesse(x)
        P[1] += P[3] # y += vitesse(y)
        pygame.draw.rect(fenetre, (0, 0, 255), (P[0], P[1], P[4], P[4]))


        if P[0] > 800 or P[0] < 0 or P[1] > 600 or P[1] < 0: #en gros si hors de l'ecran ...
            carre.remove(P) # supprime
            carre.append(spawn_carre()) # remplace

