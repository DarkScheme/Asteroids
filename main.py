import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print("About to create window with:", (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Window created")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    new_clock = pygame.time.Clock()
    dt = 0

    
    
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    while 1 > 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        screen.fill("black")
        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obi in asteroids:
            for sho in shots:
                if obi.collides_with(sho):
                    log_event("asteroid_shot")
                    obi.split()
                    sho.kill()

        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = new_clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()
