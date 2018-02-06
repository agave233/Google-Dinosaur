import pygame

def get(sprite):
    sprite_std = []
    sprite_down = []
    block = []
    bird = []

    rect = (0, 104, 2300, 26)
    floor = sprite.subsurface(rect)
    rect = (0, 0, 80, 80)
    restart = sprite.subsurface(rect)
    rect = (180, 0, 80, 96)
    cloud = sprite.subsurface(rect)
    rect = (260, 0, 96, 96)
    bird.append(sprite.subsurface(rect))
    rect = (352, 0, 96, 96)
    bird.append(sprite.subsurface(rect))
    rect = (450, 0, 32, 80)
    block.append(sprite.subsurface(rect))
    rect = (482, 0, 64, 80)
    block.append(sprite.subsurface(rect))
    rect = (546, 0, 108, 80)
    block.append(sprite.subsurface(rect))
    rect = (654, 0, 48, 96)
    block.append(sprite.subsurface(rect))
    rect = (702, 0, 102, 96)
    block.append(sprite.subsurface(rect))
    rect = (804, 0, 144, 96)
    block.append(sprite.subsurface(rect))

    rect = (1676, 0, 88, 96)
    sprite_std.append(sprite.subsurface(rect))
    rect = (1764, 0, 88, 96)
    sprite_std.append(sprite.subsurface(rect))
    rect = (1852, 0, 88, 96)
    sprite_std.append(sprite.subsurface(rect))
    rect = (1940, 0, 88, 96)
    sprite_std.append(sprite.subsurface(rect))
    rect = (2028, 0, 88, 96)
    dead = sprite.subsurface(rect)
    rect = (2204, 40, 120, 56)
    sprite_down.append(sprite.subsurface(rect))
    rect = (2321, 40, 120, 56)
    sprite_down.append(sprite.subsurface(rect))

    return sprite_std,sprite_down,block,bird,floor,dead,restart