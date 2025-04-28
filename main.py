import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()

    while True:
        dt = pygame.time.Clock().tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        for draw in drawable:
            draw.draw(screen)
        
        updatable.update(dt)
        for asteroid in asteroids:
            asteroid.update(dt)

            if asteroid.collision_detection(player):
                print("Game over!")
                pygame.quit()
                return
            
            for shot in shots:
                if asteroid.collision_detection(shot):
                    shot.kill()
                    asteroid.split()
                    
       
        pygame.display.flip()
    

if __name__ == "__main__":
    main()