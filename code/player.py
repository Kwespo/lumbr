import pygame
import tree as treeF
import math

"""
Making the script for the player class. 
"""

class Player:
    def __init__(self, sprite = 'assets/Tiles/player.png',x = 0, y = 0, angle = 0, speed = 5, chopRange = 20, attackDamage = 100):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.chopRange = chopRange
        self.sprite = pygame.image.load('assets/Tiles/player.png').convert_alpha()
        self.attackDamage = attackDamage

    def inMap(self, mX, mY, x, y):
            if x+16 < mX and x > 0 and y+16 < mY and y > 0:
                return True
            else:
                return False

    def create(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)

    def chop_Tree(self):
        for tree in range(len(treeF.Tree.trees)):
            try:
                tree_x, tree_y = treeF.Tree.trees[tree][0]
                distance = math.sqrt((tree_x - self.x) ** 2 + (tree_y - self.y) ** 2) < self.chopRange
                if distance:
                    print('Chopping tree...')
                    treeF.Tree.tree_Health(treeF.Tree.trees[tree][1], self.attackDamage, tree)
            except:
                print('No trees in range...')

    def playerAction(self, keyPress, mX, mY):
        if keyPress[pygame.K_RIGHT]:
            if self.inMap(mX, mY, self.x, self.y):
                self.angle = 90
                self.x += self.speed
            else:
                self.x, self.y = mX//2, mY//2
        if keyPress[pygame.K_LEFT]:
            if self.inMap(mX, mY, self.x, self.y):
                self.angle = 270
                self.x -= self.speed
            else:
                self.x, self.y = mX//2, mY//2
        if keyPress[pygame.K_UP]:
            if self.inMap(mX, mY, self.x, self.y):
                self.angle = 0
                self.y -= self.speed
            else:
                self.x, self.y = mX//2, mY//2
        if keyPress[pygame.K_DOWN]:
            if self.inMap(mX, mY, self.x, self.y):
                self.angle = 180
                self.y += self.speed
            else:
                self.x, self.y = mX//2, mY//2
        if keyPress[pygame.K_SPACE]:
            self.chop_Tree()