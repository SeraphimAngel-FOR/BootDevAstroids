import pygame
import sys
from asteroidfield import *
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  # renamed from Asteroid
    shots = pygame.sprite.Group()  
    # set containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable  # removed parentheses
    Shot.containers = (shots, updatable, drawable)

    # Create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = 0
    font = pygame.font.Font(None, 36)
    # Create the asteroid field (BEFORE the game loop)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, color=0)
        text_surface = font.render(f'Score: {score}', True, (255, 255, 255))  # White color
        screen.blit(text_surface, (SCREEN_WIDTH - text_surface.get_width() - 10, 10))
        for obj in updatable:
            obj.update(dt)
    
    # Check collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                print(f"Your score was {score}!")
                sys.exit()
    
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    score += 1
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000.0
if __name__ == "__main__":
    main()