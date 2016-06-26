import pygame
from pygame.sprite import Group
from button import Button
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make play button
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats,play_button, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #Make a ship
    ship = Ship(ai_settings,screen)    
    #Make a group to store bullets and aliens
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption("Alien Invasion")

    #Create instance to store game statistics
    stats = GameStats(ai_settings)
    
    #Set background color
    bg_color = (230, 230, 230)

    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Start main loop for game.

    while True:
        gf.check_events(ai_settings,screen,ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    

run_game()
