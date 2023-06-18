import random
import keyboard
import pygame.mixer

pygame.display.set_caption("invoker game")
pygame.display.set_mode((700, 1020))

win = pygame.display.get_surface()

pygame.mixer.init()
pygame.mixer.music.load("invoker_game/sounds/dota_2 First Blood.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

incorrect_sounds = [
    pygame.mixer.Sound("invoker_game/sounds/Invo_pain.mp3.mpeg"),
    pygame.mixer.Sound("invoker_game/sounds/Invo_pain_2.mp3.mpeg"),
    pygame.mixer.Sound("invoker_game/sounds/Invo_pain_3.mp3.mpeg"),
]

for sound in incorrect_sounds:
    sound.set_volume(0.3)

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
points = 0

tornado_image = pygame.image.load("invoker_game/images/tornado_img.jpg")
cold_snap_image = pygame.image.load("invoker_game/images/cold_snap_img.jpg")
meteor_image = pygame.image.load("invoker_game/images/chaos_meteor_img.jpg")
ice_wall_image = pygame.image.load("invoker_game/images/ice_wall_img.jpg")
emp_image = pygame.image.load("invoker_game/images/emp_img.jpg")
blast_image = pygame.image.load("invoker_game/images/blast_img.jpg")
ghost_walk_image = pygame.image.load("invoker_game/images/ghost_walk_img.jpg")
sun_strike_image = pygame.image.load("invoker_game/images/sun_strike_img.jpg")
forge_spirit_image = pygame.image.load("invoker_game/images/forge_spirit_img.jpg")
alacrity_image = pygame.image.load("invoker_game/images/alacrity_img.jpg")
quas_img = pygame.image.load("invoker_game/images/quas_img.jpg")
exort_img = pygame.image.load("invoker_game/images/exort_img.jpg")
wex_img = pygame.image.load("invoker_game/images/wex_img.jpg")

skill_img = pygame.transform.scale(pygame.image.load("invoker_game/images/skill2.png"), (128, 128))
skillramka_img = pygame.transform.scale(pygame.image.load("invoker_game/images/skillramka.png"), (128, 128))
skillramka_img.set_alpha(100)
skillramka_inactive_img = pygame.transform.scale(pygame.image.load("invoker_game/images/skillramka.png"), (128, 128))
bg_img = pygame.transform.scale(pygame.image.load("invoker_game/images/bg.png"), (2048/2, 1536/2))
hud_img = pygame.transform.scale(pygame.image.load("invoker_game/images/hud.png"), (3317/4.5, 845/2.7))

win.blit(forge_spirit_image, (0, 0))
hand = ["q", "w", "e"]


def quas(e):
    hand[0] = hand[1]
    hand[1] = hand[2]
    hand[2] = "q"


def wex(e):
    hand[0] = hand[1]
    hand[1] = hand[2]
    hand[2] = "w"


def exort(e):
    hand[0] = hand[1]
    hand[1] = hand[2]
    hand[2] = "e"


score = 0
lvl = 1


def ult(e):
    try:
        global score
        if sorted([i for i in spells[0].keys]) == sorted(hand):
            spells.remove(spells[0])
            score += 30
        else:
            score -= 20
            random.choice(incorrect_sounds).play()
    except Exception as ee:
        print(ee)


keyboard.on_press_key("q", quas)
keyboard.on_press_key("w", wex)
keyboard.on_press_key("e", exort)
keyboard.on_press_key("r", ult)


def spawnSpell():
    r = random.randint(1, 10)
    match r:
        case 1:
            spells.append(Spell(random.randint(0, 572), -128, tornado_image, "qww"))
        case 2:
            spells.append(Spell(random.randint(0, 572), -128, cold_snap_image, "qqq"))
        case 3:
            spells.append(Spell(random.randint(0, 572), -128, meteor_image, "eew"))
        case 4:
            spells.append(Spell(random.randint(0, 572), -128, ice_wall_image, "qqe"))
        case 5:
            spells.append(Spell(random.randint(0, 572), -128, emp_image, "www"))
        case 6:
            spells.append(Spell(random.randint(0, 572), -128, blast_image, "qwe"))
        case 7:
            spells.append(Spell(random.randint(0, 572), -128, ghost_walk_image, "qqw"))
        case 8:
            spells.append(Spell(random.randint(0, 572), -128, sun_strike_image, "eee"))
        case 9:
            spells.append(Spell(random.randint(0, 572), -128, forge_spirit_image, "eeq"))
        case 10:
            spells.append(Spell(random.randint(0, 572), -128, alacrity_image, "wew"))


spell_cd = 433
speed = 0.8
current_frame = 0


run = True


class Spell:
    def __init__(self, x, y, image, keys):
        self.x = x
        self.y = y
        self.image = image
        self.keys = keys


spells = []
while run:
    spell_cd = int(433/(1+lvl/10))
    speed = 0.8+lvl/10
    if score >= 100:
        lvl = (score//100)+1
    else:
        lvl = 1

    win.blit(bg_img, (-150, 0))
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            run = False
            pygame.mixer.music.stop()
    current_frame += 1
    if current_frame >= spell_cd:
        current_frame = 0
        spawnSpell()
    for spell in spells:
        win.blit(spell.image, (spell.x, spell.y))
        if (spell == spells[0]):
            win.blit(skillramka_inactive_img, (spell.x, spell.y))
        else:
            win.blit(skillramka_img, (spell.x, spell.y))
        spell.y += speed

        if spell.y > 750:
            score -= 30
            spells.remove(spell)
            random.choice(incorrect_sounds).play()

    win.blit(hud_img, (-20, 740))

    if hand[0] == "q":
        win.blit(quas_img, (105, 825))
    if hand[0] == "w":
        win.blit(wex_img, (105, 825))
    if hand[0] == "e":
        win.blit(exort_img, (105, 825))
    if hand[1] == "q":
        win.blit(quas_img, (286, 825))
    if hand[1] == "w":
        win.blit(wex_img, (286, 825))
    if hand[1] == "e":
        win.blit(exort_img, (286, 825))
    if hand[2] == "q":
        win.blit(quas_img, (444+23, 825))
    if hand[2] == "w":
        win.blit(wex_img, (444 + 23, 825))
    if hand[2] == "e":
        win.blit(exort_img, (444 + 23, 825))
    win.blit(skill_img, (444 + 23, 825))
    win.blit(skill_img, (286, 825))
    win.blit(skill_img, (105, 825))

    win.blit(my_font.render('Счёт:', False, (235, 255, 90)), (10, 0))
    win.blit(my_font.render(str(score), False, (255, 255, 0)), (95, 0))
    win.blit(my_font.render('Сложность:', False, (235, 75, 70)), (480, 0))
    win.blit(my_font.render(str(lvl), False, (255, 0, 0)), (650, 0))

    pygame.display.flip()
