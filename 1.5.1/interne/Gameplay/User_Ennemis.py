import pygame, random, sys



def tools():
    global obstacles, index_prochain, delai_spawn, compteur, police, font
    police = pygame.font.SysFont("Arial", 24)
    font = pygame.font.SysFont(None, 20)
    obstacles = []
    index_prochain = 0
    delai_spawn = 30 # frames entre chaque apparition
    compteur = 0

def draw_button(fenetre, text, x, y, taille_x, taille_y, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+taille_x > mouse[0] > x and y+taille_y > mouse[1] > y:
        pygame.draw.rect(fenetre, active_color, (x, y, taille_x, taille_y))
        if click[0] == 1 and action:
            return action()
    else:
        pygame.draw.rect(fenetre, inactive_color, (x, y, taille_x, taille_y))
    
    text_surface = font.render(text, True, (0 ,0, 255))
    text_rect = text_surface.get_rect(center=(x + taille_x/2, y + taille_y/2))
    fenetre.blit(text_surface, text_rect)


def restart():
    return "game"

def retour():
    return "accueil"


def Game_over(Player, fenetre, largeur, hauteur, draw_button):
    print("game over")
    Game_over = True
    while Game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Text_over = police.render("Game over",True, (50, 50, 50))
        fenetre.blit(Text_over, ( largeur / 2.5 , hauteur / 3))
        re_button =draw_button(fenetre, "Restart", largeur /4.5 +100, 340, 70, 40,(0, 0, 0), (40, 40, 0), restart)
        option =draw_button(fenetre, "Menu", largeur /2 , 340, 70, 40,(0, 0, 0), (40, 40, 0), retour)
        if option == "accueil":
            return option
        elif re_button == "game":
            return re_button
    
        pygame.display.update()


class Score:
    def __init__(self):
        self.score =0
        self.lvl = 1
        self.NEXT_lvl= []
        self.multipl =0
        self.Target = True
    
    def affichage(self,fenetre, largeur, hauteur):
        texte = police.render(f"Score : {self.score}", True, (0, 0, 0))
        text_lvl = police.render(f"lvl {self.lvl}", True, (0,0,0))
        fenetre.blit(texte, (largeur - largeur +30, hauteur - hauteur +30)) 
        fenetre.blit(text_lvl, (largeur - 70, hauteur - hauteur +30))
    
    def logic_lvl(self, Player, Ennemis, inst_score):
        self.multipl +=1
        self.NEXT_lvl.append(10 *self.multipl)
        if self.Target == False and self.score not in self.NEXT_lvl:
            self.Target = True
            print("target False !")
        elif self.score in self.NEXT_lvl and self.Target == True:
                print("target True et nxt lvl !!")
                self.lvl +=1
                Player.vitesse += 0.5
                Ennemis.Ennemis_vitesse +=0.5
                if Ennemis.delai_spawn > 50:
                    Ennemis.delai_spawn -=0.5        

                self.Target = False

        

        

    def change_lvl(self, Player, Ennemis, inst_score):
        Player.vitesse += 0.5
        Ennemis.Ennemis_vitesse +=0.5
        if Ennemis.delai_spawn > 50:
            Ennemis.delai_spawn -=0.5
    
    

class User:
    def __init__(self, largeur, hauteur):
        print("class joueur lancée")
        self.carre_x = largeur - largeur /2
        self.carre_y = 400
        self.carre_taille = 30
        self.vitesse = 3
        self.rect = pygame.Rect(self.carre_x, self.carre_y, self.carre_taille, self.carre_taille)
        
    
    def Write_User(self, fenetre):
        #print("joueur crée")
        player = pygame.draw.rect(fenetre, (255, 0, 0), (self.carre_x, self.carre_y, self.carre_taille, self.carre_taille))
        
    def move(self, largeur, hauteur):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and self.carre_x >= 0:
            self.carre_x -= self.vitesse
        if touches[pygame.K_RIGHT] and self.carre_x + self.carre_taille <= largeur:
            self.carre_x += self.vitesse
        
        self.rect.update(self.carre_x, self.carre_y, self.carre_taille, self.carre_taille)



class Mob():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.Ennemis_taille = 30
        self.Ennemis_vitesse = 3
        self.x_SpawnEnnemis = [random.randint(0, largeur - self.Ennemis_taille) for _ in range(10)]
        self.obstacles = []
        self.index_prochain = 0
        self.compteur = 0
        self.delai_spawn = 30

    def update_spawn(self, fenetre, inst_score, Player, largeur, hauteur):
        self.compteur += 1

        if self.compteur >= self.delai_spawn:
            if self.index_prochain >= len(self.x_SpawnEnnemis):
                self.index_prochain = 0
                self.x_SpawnEnnemis = [
                    random.randint(0, self.largeur - self.Ennemis_taille) for _ in range(10)
                ]

            x = self.x_SpawnEnnemis[self.index_prochain]
            
            self.obstacles.append({
            "x": x,
            "y": -30,
            "rect": pygame.Rect(x, -30, self.Ennemis_taille, self.Ennemis_taille)
        })
 
            self.index_prochain += 1
            self.compteur = 0

        # Mise à jour et dessin des obstacles
        for obstacle in self.obstacles[:]:  # copie pour modification sécurisée
            obstacle["y"] += self.Ennemis_vitesse
            obstacle["rect"].y = obstacle["y"]
            #print("rect", rect_obstacle)
            
            #print(obstacle)
            pygame.draw.rect(fenetre, (0, 0, 255), obstacle["rect"])
            
            
            if Player.rect.colliderect(obstacle["rect"]):
                print("💥 COLLISION !")
                new_state = Game_over(Player, fenetre, largeur, hauteur, draw_button)
                if new_state == "accueil":
                    return new_state
                elif new_state == "game":
                    return new_state
                # Suppression si hors écran
            if obstacle["y"] > self.hauteur:
                print("suppression")
                self.obstacles.remove(obstacle)
                inst_score.score +=1
                


        
                 
            