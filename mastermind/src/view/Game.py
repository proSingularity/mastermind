'''
Created on 28.07.2017

@author: Mirco
'''

import pygame
from util import Settings
from ViewSettings import COLORS_TO_RGB
from ViewSettings import BLOCK_SIZE as block_size
from view import ViewSettings
from view.Stone import Stone

def drawColorChoices(surface, color_choices_stones):
    counter = 1
    for color in Settings.COLORS:
        stone = Stone(COLORS_TO_RGB[color], block_size, block_size,
                      surface.get_width() / (len(Settings.COLORS) + 1) * counter - block_size / 2,
                      surface.get_height() * 0.8)
        surface.blit(stone.image,
            (surface.get_width() / (len(Settings.COLORS) + 1) * counter - block_size / 2,
             surface.get_height() * 0.8))
        color_choices_stones.append(stone)
        counter += 1

def drawRowOfStones(surface, current_row_of_sprites):
    for i in xrange(Settings.STONE_NUMBER):
        stone = Stone(COLORS_TO_RGB['black'],
            block_size, block_size)
        surface.blit(stone.image,
            (surface.get_width() / (Settings.STONE_NUMBER + 1) * (i + 1) - block_size / 2,
            surface.get_height() * 0.4))
        current_row_of_sprites.append(stone)

def handleMouseButtonUp(code_given_in_colors, color_choices_stones, current_row_of_sprites):
    if len(code_given_in_colors) < Settings.STONE_NUMBER:
        pos = pygame.mouse.get_pos()
        clicked_stones = [s for s in color_choices_stones if s.rect.collidepoint(pos)]
        if clicked_stones:
            clicked_stone = clicked_stones[0]
            if Settings.DEBUG_LEVEL >= 1:
                print('clicked stone: ', clicked_stone, ViewSettings.RGB_TO_COLORS[clicked_stone.color])
            # TODO: color central stones in color of clicked_stone
            # current_row_of_sprites[len(code_given_in_colors)].set_color(clicked_stone.color)
            # pygame.display.update()
            
            code_given_in_colors.append(ViewSettings.RGB_TO_COLORS[clicked_stone.color])
            if Settings.DEBUG_LEVEL >= 1:
                print('code_given_in_colors = ', code_given_in_colors)
            
    elif True:
        pass  # TODO:
       

def drawEncrypterScreen(surface,color_choices_stones, current_row_of_sprites):
            surface.fill(COLORS_TO_RGB['white'])
            drawColorChoices(surface, color_choices_stones)
            drawRowOfStones(surface, current_row_of_sprites)


def drawStartScreen(surface, font):
    screen_text = font.render('Hit Enter to Start', True, COLORS_TO_RGB['black'])
    surface.blit(screen_text, [surface.get_width()/2, surface.get_height()/2])


def handleStartScreen(surface, font, is_show_start_screen, color_choices_stones, current_row_of_sprites):
    '''
    Draws start screen until Return key was hit. Then draw board for encrypter.
    @return: False if Return key was hit, else True
    '''
    drawStartScreen(surface, font)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            drawEncrypterScreen(surface, color_choices_stones, current_row_of_sprites)
            return False
    return True

def game_loop(surface):
    color_choices_stones = []
    current_row_of_sprites = []
    code_given_in_colors = []
                            
    gameExit = False
    is_show_start_screen = True
    font = pygame.font.SysFont(None, 25)
    
    while not gameExit:
        if is_show_start_screen:
            is_show_start_screen = handleStartScreen(surface, font, is_show_start_screen,
                              color_choices_stones, current_row_of_sprites)
                    
        else:
            for event in pygame.event.get():
                if Settings.DEBUG_LEVEL >= 2 and event.type != pygame.MOUSEMOTION:
                    print(event)
                if event.type == pygame.QUIT:
                    gameExit = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    handleMouseButtonUp(code_given_in_colors, color_choices_stones, current_row_of_sprites)
        pygame.display.update()

def getConfiguredMainSurface():
    surface = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS)
    surface.fill(COLORS_TO_RGB['white'])
    pygame.display.set_caption('Mastermind. App by ProSingularity.')
    return surface



# main
pygame.init()
surface = getConfiguredMainSurface()
game_loop(surface)
pygame.quit()
quit()
