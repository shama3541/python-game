import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers=(updatable,)
    Asteroid.containers=(asteroids,updatable,drawable)
    Player.containers =(updatable,drawable)

    player_1= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0
    
    time_elapsed=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
     
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
     
     screen.fill("black")
     dt=time_elapsed.tick(60)/1000
     updatable.update(dt)
     
     for asteroid in asteroids:
      player_1.Collision(asteroid)

      for shot in shots:
       shot.draw(screen)
       if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
     
     for sprite in drawable:
      sprite.draw(screen)
     
     pygame.display.flip()
     
     





if __name__ == "__main__":
    main()
