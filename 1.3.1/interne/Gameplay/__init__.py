def entities(largeur, hauteur, fenetre):
    from interne.Gameplay.User_Ennemis import User, tools, Mob, Score
    global Player, Ennemis, inst_score
    fenetre.fill((255,255,255))
    tools()

    Player = User(largeur, hauteur)
    Ennemis = Mob(largeur, hauteur)  # ← Instance unique
    inst_score = Score()
    
    print("User lancé")
    
    
    
    
    
    

def update(fenetre,events, largeur, hauteur):
    from interne.Gameplay.User_Ennemis import User, Mob
    fenetre.fill((255,255,255))
    
    Player.Write_User(fenetre)
    Player.move(largeur, hauteur)
    
    Ennemis.update_spawn(fenetre, largeur, hauteur, inst_score, Player, Ennemis)
    
    inst_score.affichage(fenetre,largeur, hauteur)
    inst_score.logic_lvl(Player, Ennemis, inst_score)
    
    #Game_over(Player, Ennemis)
    
    
    
            