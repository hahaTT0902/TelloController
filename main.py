import pygame
from djitellopy import Tello

pygame.init()

window_width = 400
window_height = 300
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tello Drone Controller")

tello = Tello()

tello.connect()

battery_level = tello.get_battery()
print(f"Battery level: {battery_level}%")

tello.takeoff()

# Control flags (could NOT be adjusted)
running = True
moving = False

# MAIN loop
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Moving forward")
                tello.move_forward(200)
                moving = True
            elif event.key == pygame.K_s:
                print("Moving backward")
                tello.move_back(200)
                moving = True
            elif event.key == pygame.K_a:
                print("Moving left")
                tello.move_left(200)
                moving = True
            elif event.key == pygame.K_d:
                print("Moving right")
                tello.move_right(200)
                moving = True
            elif event.key == pygame.K_r:
                print("Moving up")
                tello.move_up(200)
                moving = True
            elif event.key == pygame.K_f:
                print("Moving down")
                tello.move_down(200)
                moving = True
            elif event.key == pygame.K_q:
                print("Rotating counter-clockwise")
                tello.rotate_counter_clockwise(45)
                moving = True
            elif event.key == pygame.K_e:
                print("Rotating clockwise")
                tello.rotate_clockwise(45)
                moving = True
            elif event.key == pygame.K_l:
                print("Landing")
                tello.land()
                running = False
    battery_text = f"Battery: {tello.get_battery()}%"
    font = pygame.font.S
