import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'pear.mp3')   ####self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'Lotan says pear.mp3')   #### self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.Sound(self.path + 'theme.mp3')


        pg.mixer.music.load(self.path + "Call me Tami.mp3")
        pg.mixer.music.play(5) # repeat 5 times
        pg.mixer.music.queue(self.path + "abc with clear.mp3")   # queue test2.wav after test.wav plays 5 times
        clock = pg.time.Clock()
        clock.tick(10)

        self.npc_shot.set_volume(0.5)