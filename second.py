import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Second App")

font = pygame.font.Font(None, 36)
text = font.render("This is the second app", True, (255, 255, 255))
text_rect = text.get_rect(center=(200, 150))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()

