import pygame, sys


print("Accueil lancé")
#from interne.Gameplay import Setup_game, start_game
pygame.init()




    


def setup_main_menu():
    font =pygame.font.SysFont("Arial",36)
    TitreFont =pygame.font.SysFont("Comic Sans MS", 100)
    
    
    Titre = ["Infinite Bloc"]
    buttons =[("▶ JOUER", 250), ("⚙ OPTIONS", 330), ("✖ QUITTER", 410)] 
    selected =0
    
    Blue = (0, 0, 255)


    carre = []
    for _ in range(200):
        carre.append(create_carre())
        
    


    
    

setup_main_menu()
    
def  
    while True:
        from random import randint:
            return [randint(0, 800), randint(-150,0), randint(-2,2), randint(3,4), randint(2,7)]  # x, y viteese(x), vitesse(y), taille

        clock.tick(60)
        fenetre.fill((150, 150, 190))
        
        
        
        for i, (text, y) in enumerate(buttons):
            if i == selected: color = (0,0,0)
            else: color =(255,255,255)
            Label = font.render(text, True, color)
            rect = Label.get_rect(center=(400, y))
            fenetre.blit(Label, rect)
        
        Titre =TitreFont.render("Infinite Bloc", True, (0, 0, 30))
        fenetre.blit(Titre, (100, 50))
        
        for P in carre:
            P[0] += P[2]
            P[1] += P[3]
            pygame.draw.rect(fenetre, Blue, (P[0], P[1], P[4], P[4]))
            if P[0] > 800 or P[0] < 0 or P[1] > 600 or P[1] < 0:
                carre.remove(P)
                carre.append(create_carre())
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(buttons)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(buttons)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        return Go_gameplay()
                    elif selected == 1:
                        print("Afficher les options")
                    elif selected == 2:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        



Main_page()



