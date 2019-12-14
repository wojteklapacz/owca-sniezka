from superwires import games, color
import random
import time

games.init(screen_width=1280, screen_height=850, fps=75)

class Player(games.Sprite):
    """Postać gracza"""
    image = games.load_image("owca.png")

    def __init__(self):
        """Inicjalizacja obiektu gracza"""
        super(Player, self).__init__(image=Player.image,
                                     x=games.mouse.x,
                                     bottom=games.screen.height)
        self.score = games.Text(value=0, size=50, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """Zmiana pozycji przez mysz"""
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.points()

    def points(self):
        """Sprawdź czy złapał śnieżki"""
        for snowball in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width - 1
            snowball.Kolizja()
        if self.score.value == 20:
            Snowball.speed = 7

        if self.score.value == 40:
            Snowball.speed = 9

        if self.score.value == 60:
            Snowball.speed = 11

        if self.score.value == 80:
            Snowball.speed = 13

        if self.score.value == 100:
            Snowball.speed = 15

        if self.score.value == 120:
            Snowball.speed = 17

        if self.score.value == 160:
            Snowball.speed = 20

        if self.score.value == 200:
            Snowball.speed = 25

        if self.score.value == 250:
            Snowball.speed = 30

        if self.score.value == 300:
            Snowball.speed = 33

        if self.score.value == 350:
            Snowball.speed = 36

        if self.score.value == 400:
            Snowball.speed = 40

        if self.score.value == 430:
            Snowball.speed = 44

        if self.score.value == 450:
            Snowball.speed = 50

        if self.score.value == 500:
            Snowball.speed = 55

        if self.score.value == 600:
            Snowball.speed = 60

        if self.score.value == 650:
            Snowball.speed = 100


class Snowball(games.Sprite):
    """Śnieżki"""
    image = games.load_image("śnieżka.png")
    speed = 5

    def __init__(self, x=random.randrange(15, games.screen.width-15), y=2):
        """Inicjalizacja obiektu Snowball"""
        super(Snowball, self).__init__(image=Snowball.image,
                                       x=x,
                                       y=y,
                                       dy=Snowball.speed,)

    def update(self):
        """Sprawdzenie czy śnieżka dotknęła brzegu ekranu"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def Kolizja(self):
        """Zniszcz przy zderzeniu"""
        self.destroy()

    def end_game(self):
        """Zakończ grę."""
        end_message = games.Message(value="Game over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=4*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


def ticker():
    while True:
        time.sleep(2)
        snowball = Snowball()
        games.screen.add(snowball)

def main():
    """Uruchomienie gry"""
    wall_image = games.load_image("ścianka.jpg", transparent=False)
    games.screen.background = wall_image

    player = Player()
    games.screen.add(player)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

# start
main()

