import math
import pyglet
import random


# IMAGE
game_window = pyglet.window.Window(800, 600)
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
player_image = pyglet.resource.image('4.png')
bullet_image = pyglet.resource.image('2.png')
asteroid_image = pyglet.resource.image('3.png')


main_batch = pyglet.graphics.Batch()
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

player_ship = pyglet.sprite.Sprite(img=player_image, x=400, y=300)


def asteroids(num: int, player_pos: list, batch=None):
    asteroid = list()
    for i in range(num):
        asteroid_x, asteroid_y = player_pos
        while distance((asteroid_x, asteroid_y), player_pos) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
            new_asteroid = pyglet.sprite.Sprite(img=asteroid_image, x=asteroid_x, y=asteroid_y, batch=batch)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = random.random() * 40
            new_asteroid.velocity_y = random.random() * 40
            asteroid.append(new_asteroid)
    return asteroid


def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def player_lives(num: int, batch=None):
    players = list()
    for i in range(num):
        new_sprite = pyglet.sprite.Sprite(img=player_image, x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        players.append(new_sprite)
    return players


# LABEL
# score_label = pyglet.text.Label(text='Score: 0', x=10, y=460)
level_label = pyglet.text.Label(text='My Amazing Game',
                                x=game_window.width // 2,
                                y=game_window.height // 2, anchor_x='center')

asteroidss = asteroids(3, player_ship.position, batch=main_batch)


@game_window.event
def on_draw():
    game_window.clear()
    score_label.draw()
    level_label.draw()
    player_ship.draw()
    main_batch.draw()


class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def check_bounds(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y


game_objects = [player_ship] + asteroidss


def update(dt):
    for obj in game_objects:
        obj.update()


pyglet.clock.schedule_interval(update, 1 / 120)


if __name__ == '__main__':
    pyglet.app.run()
