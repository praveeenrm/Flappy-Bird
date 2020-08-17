from os import path

from datetime import datetime
now = datetime.now()
day_or_night = now.strftime("%p")


# Settings
TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 600
FPS = 120


# Colors defined in RGB - Red, Green, Blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Image Folder
game_folder = path.dirname(__file__)
image_foler = path.join(game_folder, 'assets')

# Icon image
icon_image = path.join(image_foler, 'icon.png')

# Images / Sprites
bg_image_day = path.join(image_foler, 'background-day.png')
bg_image_night = path.join(image_foler, 'background-night.png')
bird_image = path.join(image_foler ,'yellowbird-midflap.png')
floor_image = path.join(image_foler ,'base.png')
pipe_image = path.join(image_foler, 'pipe-green.png')
pipe_image_inverse = path.join(image_foler, 'pipe-green_copy.png')

bird_image_1 = path.join(image_foler ,'yellowbird-downflap.png')
bird_image_2 = path.join(image_foler ,'yellowbird-midflap.png')
bird_image_3 = path.join(image_foler ,'yellowbird-upflap.png')

game_over_image = path.join(image_foler ,'gameover.png')

message_image = path.join(image_foler, 'message.png')

# Sound Folder
sound_folder = path.join(game_folder, 'sound')
flap_music = path.join(sound_folder, 'sfx_wing.wav')
death_music = path.join(sound_folder, 'sfx_die.wav')
score_music = path.join(sound_folder, 'sfx_point.wav')
bg_music = path.join(sound_folder, 'happy_tune.ogg')


# varibales
# X - pipe top heights
# Y - pipe down heights
X = [50, 100, 150, 200, 250, 300, 350, 10, 80, 180, 220, 320, 280]
Y = [350, 300, 250, 200, 150, 100, 50, 390, 320, 220, 180, 80, 120]

