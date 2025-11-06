import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 바닥에 공 배치
    global balls
    balls = [Ball(random.randint(100, 1600-100), 60, 0) for _ in range(20)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pair("boy:ball", boy, None)
    for ball in balls:
        game_world.add_collision_pair("boy:ball", None, ball)

    game_world.add_collision_pair("grass:ball", grass, None)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)

def update():
    game_world.update()

    # boy 와 공들 충돌 처리
    # 여러 객체들을 충돌처리하다보면 코드가 늘어진다. 충돌검사를 위한 데이터구조를 만든다. (dict 사용)
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

