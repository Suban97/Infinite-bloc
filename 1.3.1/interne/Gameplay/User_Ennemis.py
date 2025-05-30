import pygame, random, sys


def Restart(Score, Mob, User):
    tools()
    Player = User(largeur, hauteur)
    Ennemis = Mob(largeur, hauteur)  # ← Instance unique

    
def retour():
    print("return")
    return "menu"


def tools():
    global obstacles, index_prochain, delai_spawn, compteur, police
    police = pygame.font.SysFont("Arial", 24)
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
    
    text_surface = police.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + taille_x/2, y + taille_y/2))
    fenetre.blit(text_surface, text_rect)


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
        print("joueur crée")
        player = pygame.draw.rect(fenetre, (255, 0, 0), (self.carre_x, self.carre_y, self.carre_taille, self.carre_taille))
        
    def move(self, largeur, hauteur):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and self.carre_x >= 0:
            self.carre_x -= self.vitesse
            self.rect.topleft = (self.carre_x, self.carre_y)
        if touches[pygame.K_RIGHT] and self.carre_x + self.carre_taille <= largeur:
            self.carre_x += self.vitesse
            self.rect.topleft = (self.carre_x, self.carre_y)


class Mob:
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
        self.rect_obstacle = None

    def update_spawn(self, fenetre, largeur, hauteur, inst_score, Player, Ennemis):
        print("fenetre ...", fenetre)
        self.compteur += 1

        if self.compteur >= self.delai_spawn:
            if self.index_prochain >= len(self.x_SpawnEnnemis):
                self.index_prochain = 0
                self.x_SpawnEnnemis = [
                    random.randint(0, self.largeur - self.Ennemis_taille) for _ in range(10)
                ]

            x = self.x_SpawnEnnemis[self.index_prochain]
            self.obstacles.append([x, -30])
            self.index_prochain += 1
            self.compteur = 0

        # Mise à jour et dessin des obstacles
        for obstacle in self.obstacles[:]:  # copie de la liste pour suppression sécurisée
            obstacle[1] += self.Ennemis_vitesse
            self.rect_obstacle = pygame.Rect(obstacle[0], obstacle[1], self.Ennemis_taille, self.Ennemis_taille)
            pygame.draw.rect(fenetre, (0, 0, 255), self.rect_obstacle)
            #print(Ennemis.rect_obstacle)
            if Player.rect.colliderect(Ennemis.rect_obstacle):
                Game_over = True
                while Game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    
                    Text_over = police.render(f"Game over",True, (50, 50, 50))
                    fenetre.blit(Text_over, ( largeur / 2.7  , hauteur / 2.5))
                    draw_button(fenetre, "Restart", largeur /4, 340, 70, 40,(0, 0, 0), (40, 40, 0), Restart)
                    option =draw_button(fenetre, "Menu", largeur /3.5 + 100, 340, 70, 40,(0, 0, 0), (40, 40, 0), retour)
                    if option == "accueil":
                        return

                    
                    

                    #Text_over = police.render(f"Game over",True, (50, 50, 50))
                    #fenetre.blit(Text_over, ( largeur / 2.7  , hauteur / 2.5))
                    #draw_button("Restart", largeur /4, 340, 70, 40,(0, 0, 0), (40, 40, 0), Restart)
                    #option =draw_button("Menu", largeur /3.5 + 100, 340, 70, 40,(0, 0, 0), (40, 40, 0), retour)
                    #if option == "menu":
                     #   return
            

             
            # Suppression si hors écran
            if obstacle[1] > self.hauteur:
                self.obstacles.remove(obstacle)
                inst_score.score +=1
                


        
                 
            