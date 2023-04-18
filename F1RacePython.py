import pygame
import math

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

track_img = pygame.image.load('track.png')
car_img = pygame.image.load('car.png')
car2_img = pygame.image.load('car2.png')

car_x = 800
car_y = 100
car_speed = 0
car_angle = -90

car2_x = 800
car2_y = 165
car2_speed = 0
car2_angle = -90

clock = pygame.time.Clock()

# Añadir variables para el cronómetro y el medidor de velocidad
start_time = pygame.time.get_ticks()
elapsed_time = 0
font = pygame.font.Font(None, 30)

# Bucle principal del juego
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        car_speed += 0.1
    elif keys[pygame.K_DOWN]:
        car_speed -= 0.1
    if keys[pygame.K_w]:
        car2_speed += 0.1
    elif keys[pygame.K_s]:
        car2_speed -= 0.1

    if keys[pygame.K_LEFT]:
        car_angle += 2
    elif keys[pygame.K_RIGHT]:
        car_angle -= 2
    if keys[pygame.K_a]:
        car2_angle += 2
    elif keys[pygame.K_d]:
        car2_angle -= 2

    # Verificar si se ha presionado la tecla de espacio para reiniciar el juego
    if keys[pygame.K_SPACE]:
        car_x = 800
        car_y = 100
        car_speed = 0
        car_angle = -90
        car2_x = 800
        car2_y = 165
        car2_speed = 0
        car2_angle = -90
        start_time = pygame.time.get_ticks()
        elapsed_time = 0
        
    # Actualizar la posición del primer coche
    car_x += car_speed * math.sin(math.radians(car_angle))
    car_y += car_speed * math.cos(math.radians(car_angle))

    # Actualizar la posición del segundo coche
    car2_x += car2_speed * math.sin(math.radians(car2_angle))
    car2_y += car2_speed * math.cos(math.radians(car2_angle))

    # Verificar que el coche 1 no salga de la pantalla
    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_img.get_width():
        car_x = screen_width - car_img.get_width()
    if car_y < 0:
        car_y = 0
    elif car_y > screen_height - car_img.get_height():
        car_y = screen_height - car_img.get_height()

    # Verificar que el segundo coche no salga de la pantalla
    if car2_x < 0:
        car2_x = 0
    elif car2_x > screen_width - car2_img.get_width():
        car2_x = screen_width - car2_img.get_width()
    if car2_y < 0:
        car2_y = 0
    elif car2_y > screen_height - car2_img.get_height():
        car2_y = screen_height - car2_img.get_height()

    # Dibujar el fondo de la pista y el coche
    screen.blit(track_img, (0, 0))
    screen.blit(pygame.transform.rotate(car_img, car_angle), (car_x, car_y))
    screen.blit(pygame.transform.rotate(car2_img, car2_angle), (car2_x, car2_y))

    # Actualizar el cronómetro y el medidor de velocidad
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    speed_text = font.render(f"Vel 1: {round(car_speed, 2)}Km/h", True, blue)
    speed_text2 = font.render(f"Vel 2: {round(car2_speed, 2)}Km/h", True, red)
    time_text = font.render(f"Tiempo: {round(elapsed_time, 2)}s", True, black)
    restart_text = font.render(f"Press [space] to restart the game", True, black)
    
    screen.blit(speed_text, (10, 10))
    screen.blit(speed_text2, (200, 10))
    screen.blit(time_text, (10, 30))
    screen.blit(restart_text, (10, 50))
    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
