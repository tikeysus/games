import pygame 
pygame.init() 

Screen_Width = 1200
Screen_Height = 800 

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Little Demo")

screen_running = True 
 
while screen_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_running = False 
    
    screen.fill((0, 0, 0))
    
    pygame.display.update() 

pygame.quit() 

