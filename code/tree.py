import pygame
import DEBUG as dbg


class Tree():
    def __init__(self, sprite = 'assets/Tiles/tree.png', x = 0, y = 0, health = 100):
        self.health = health
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.sprite = pygame.image.load('assets/Tiles/tree.png').convert_alpha()


    walkThrough = False
    trees = []
    health = 100


    def debugging(self):
        if dbg.debug:
            dbg.log(f'tree list: {self.trees}\n')
            # print(self.trees)


    def create(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)

    def tree_Health(self,damage, treeNum):
        if dbg.debug:
            dbg.log(f'Tree health: {self.health}\nDamage: {damage}\n')
            # print('Tree health:', self.health, 'Location:', self.location)

        self.health -= damage
        if self.health <= 0:
            self.walkThrough = True
            self.trees.pop(treeNum)

