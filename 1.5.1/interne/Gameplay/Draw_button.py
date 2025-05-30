import pygame

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
