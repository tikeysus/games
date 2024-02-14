import pygame 
pygame.init() 

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Image Loader")

maratik = pygame.image.load("/Users/tikeysus/Documents/slovo_pacana_stickers/dengi_est.webp")
background = pygame.image.load("/Users/tikeysus/Documents/slovo_pacana_stickers/main_poster.jpg")
ak_47 = pygame.image.load("/Users/tikeysus/Documents/slovo_pacana_stickers/AK47.png")

scaled_maratik = pygame.transform.scale(maratik, (200, 200))
scaled_background = pygame.transform.scale(background, (600, 800))
scaled_ak = pygame.transform.scale(ak_47, (95, 245))

run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    screen.blit(scaled_maratik, (0, 0))
    screen.blit(scaled_background,(0, 0))
    
    screen.blit(scaled_ak, (50, 565))
    screen.blit(scaled_ak, (200, 565))
    screen.blit(scaled_ak, (350, 565))
    screen.blit(scaled_ak, (500, 565))
    


    pygame.display.flip() 
