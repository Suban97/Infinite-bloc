import pygame, sys, random

pygame.init()







def Setup_game(): # Définiera les variables du start_game du jeux
    
    #Globalise les variables qui seront réutilisées par la suite
    
    # Fenetre
    global largeur, hauteur, fenetre, clock
    
    # Textuel
    global police, font, WHITE
    
    # Fonctionnement
    global score, lvl, NEXT_lvl, multipl
    # Joueur
    global carre_x, carre_y, carre_taille, vitesse
    # Obstacles
    global xspawn, Ennemis_taille, obstacles, index_prochain, delai_spawn, compteur, vitesse_Ennemis
    # Fonctionnement des niveaux
    global Target
    
    # Fenêtre
    largeur, hauteur = 350, 650
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Infinite Bloc Action - Evitez les blocs !!!")
    clock = pygame.time.Clock()
    
    # Textuel
    police = pygame.font.SysFont("Arial", 24)    
    font = pygame.font.SysFont(None, 20)
    WHITE = (250, 250, 250)


    # Fonctionnement
    score =0
    lvl = 1
    NEXT_lvl= []
    multipl =0


    # Joueur
    carre_x = largeur - largeur / 2
    carre_y = 400
    carre_taille = 30
    vitesse = 3


    # Obstacles
    xspawn = [random.randint(0, largeur - 30) for _ in range(10)]  # 10 positions aléatoires
    Ennemis_taille = 30

    obstacles = []
    index_prochain = 0
    delai_spawn = 30 # frames entre chaque apparition

    compteur = 0
    vitesse_Ennemis = 3




    Target = True # fonctionnement des niveaux
    
    
    start_game()



def retour():
    print("return")
    return "menu"



def change_lvl():
    global vitesse, vitesse_Ennemis, delai_spawn
    vitesse += 0.5
    vitesse_Ennemis +=0.5
    if delai_spawn > 50:
        delai_spawn -=0.5
    
    print("Speed !!!")






def draw_button(text, x, y, taille_x, taille_y, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+taille_x > mouse[0] > x and y+taille_y > mouse[1] > y:
        pygame.draw.rect(fenetre, active_color, (x, y, taille_x, taille_y))
        if click[0] == 1 and action:
            return action()
    else:
        pygame.draw.rect(fenetre, inactive_color, (x, y, taille_x, taille_y))
    
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + taille_x/2, y + taille_y/2))
    fenetre.blit(text_surface, text_rect)




    
def Restart():
    Setup_game()
    start_game()


def start_game():
    global multipl, score, lvl, Next_lvl, police, carre_x, carre_y, carre_taille, vitesse, xspawn, Ennemis_taille, obstacles, index_prochain, delai_swpan, Target, compteur
    while True: # Boucle de jeu
        clock.tick(60)  # 60 FPS
        fenetre.fill((255, 255, 255))

        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        multipl += 1
        NEXT_lvl.append(10 * multipl)
        
        
        texte = police.render(f"Score : {score}", True, (0, 0, 0))
        text_lvl = police.render(f"lvl {lvl}", True, (0,0,0))
     
        #textes addaptatifs --> Fenetre // insertion
        fenetre.blit(texte, (largeur - largeur +30, hauteur - hauteur +30)) 
        fenetre.blit(text_lvl, (largeur - 70, hauteur - hauteur +30))
        
        
        if Target == False and score not in NEXT_lvl:
            Target = True
            print("target False !")
        
        if score in NEXT_lvl and Target == True:
                print("target True et nxt lvl !!")
                lvl +=1
                change_lvl()
                Target = False
            
            
            
        # Mouvements du joueur
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and carre_x >= 0:
            carre_x -= vitesse
        if touches[pygame.K_RIGHT] and carre_x + carre_taille <= largeur:
            carre_x += vitesse
            
            
            
        # Apparition progressive des ennemis
        compteur += 1
        if compteur >= delai_spawn and index_prochain < len(xspawn):
            x = xspawn[index_prochain]
            obstacles.append([x, hauteur-hauteur -30])  # position initiale de l'obstacle
            index_prochain += 1
            compteur = 0
            
            
            
        
        if compteur >= delai_spawn:
            if index_prochain >= len(xspawn):  # Si tous les obstacles ont été créés
                


                index_prochain = 0  # On recommence à zéro pour repartir à la première position
                # Tu peux aussi générer de nouvelles positions aléatoires pour xspawn si tu veux plus de variété.
                xspawn = [random.randint(0, largeur - Ennemis_taille) for _ in range(10)]  # Liste de 10 nouvelles positions aléatoires
                
                
                
            
            x = xspawn[index_prochain]  # Récupère la prochaine position pour un ennemi
            obstacles.append([x, 0])  # Ajoute l'ennemi à la liste
            index_prochain += 1  # On passe à l'index suivant
            compteur = 0  # Réinitialise le compteur pour repartir de zéro
            
            
            
        # Dessin du joueur
        player = pygame.draw.rect(fenetre, (255, 0, 0), (carre_x, carre_y, carre_taille, carre_taille))



        # Dessin des obstacles
        for obstacle in obstacles:
            obstacle[1] += vitesse_Ennemis  # descente
            rect_obstacle = pygame.Rect(obstacle[0], obstacle[1], Ennemis_taille, Ennemis_taille)
            pygame.draw.rect(fenetre, (0, 0, 255), rect_obstacle)
            
            
            
            # Collision
            if player.colliderect(rect_obstacle):
                Game_over = True
                while Game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    Text_over = police.render(f"Game over",True, (50, 50, 50))
                    fenetre.blit(Text_over, ( largeur / 2.7  , hauteur / 2.5))
                    draw_button("Restart", largeur /4, 340, 70, 40,(0, 0, 0), (40, 40, 0), Restart)
                    option =draw_button("Menu", largeur /3.5 + 100, 340, 70, 40,(0, 0, 0), (40, 40, 0), retour)
                    if option == "menu":
                        return
                    pygame.display.update()
            
            if obstacle[1] > hauteur:  
                obstacles.remove(obstacle)
                score += 1
                
                

        pygame.display.update()


if __name__ == "__main__":
    Setup_game()

