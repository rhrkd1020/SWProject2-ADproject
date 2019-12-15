'''
게임의 상수값 설정
'''
import os

#DIRS
GAME_DIR = os.path.dirname(__file__)
CHAT_DIR = os.path.join(GAME_DIR, 'chat')
PROLOGUEIMAGE_DIR = os.path.join(GAME_DIR, 'image\\prologue')
STARTIMAGE_DIR = os.path.join(GAME_DIR, 'image\\startscreen')
QUIZ_DIR = os.path.join(GAME_DIR, 'image\\quiz')

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 960
HEIGHT =  540
FPS = 60
TITLE = "탈 국민"
BGCOLOR = DARKGREY

TILESIZE = 48
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#map setting
STAGELEVEL = 0
STAGETMX = ['showerRoom.tmx', 'fitness.tmx', 'secondfloor.tmx', '4thfloor.tmx']
STAGENAME = ['shower', 'fitness', 'secondfloor', '4thfloor']
PORTALMAP = {
    'fitness' : 1,
    'shower' : 0,
    'secondfloor' : 2,
}

#start, prologue
STARTIMAGE = os.listdir(STARTIMAGE_DIR)
PROLOGUEIMAGE = os.listdir(PROLOGUEIMAGE_DIR)

#player settings
PLAYER_SPEED = 180
PLAYER_IMG = [
    ['koomin00.png','koomin01.png','koomin00.png','koomin02.png'],
    ['koomin10.png','koomin11.png','koomin10.png','koomin12.png'],
    ['koomin20.png','koomin21.png','koomin20.png','koomin22.png'],
    ['koomin30.png','koomin31.png','koomin30.png','koomin32.png']
]
PLAYER_IMGB = [
    ['koominB00.png','koominB01.png','koominB00.png','koominB02.png'],
    ['koominB10.png','koominB11.png','koominB10.png','koominB12.png'],
    ['koominB20.png','koominB21.png','koominB20.png','koominB22.png'],
    ['koominB30.png','koominB31.png','koominB30.png','koominB32.png']
]
PLAYER_IMGNAME = [PLAYER_IMG, PLAYER_IMGB]

# Npc settings
XYCAR_IMG = ['xycar00.png','','xycar20.png']
XYCAR_IMGB = ['xycarB00.png','','xycarB20.png']
NPC_IMGNAME = [XYCAR_IMGB, XYCAR_IMG]
NPC_SPEED = 150
NPC_KNOCKBACK = 20

#Light Shadowing
SHADOW_COLOR = (20, 20, 20)
LIGHTMASK = 'light.png'
LIGHT_RADIUS = (300, 300)

#chat settings
CHAT_IMG = 'chat_main.png'
CHATTER_IMG = 'chat_name.png'

#sound setting
SOUNDLIST = ['background.mp3','prologue.mp3', 'start.mp3']
SOUNDEFFECT_LIST = ['19.ogg','14.ogg','break.wav','fun.ogg','doorlock.ogg','dooropen.ogg']
BGM = os.listdir(os.path.join(GAME_DIR, 'bgm'))
SFX = os.listdir(os.path.join(GAME_DIR, 'sfx'))

#FONTS
MAINFONT = 'font\\YoonMingukR.ttf'
CODEFONT = 'font\\D2Coding.ttc'

#Quiz setting
ENTER_IMG = 'quiz_enter.png'
SYMBOLS = [".", ",", "-", "_", "(", ")",
        "{", "}", "[", "]", "\\", "/",
        "+", " ", "!", ":", ";"]