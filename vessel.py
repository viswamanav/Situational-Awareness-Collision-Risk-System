import pygame
import math

class Vessel:
    def __init__(self, ship_id, x, y, speed, heading, color):
        self.ship_id = ship_id
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading
        self.color = color
        self.cpa = 0
        self.tcpa = 0
        self.risk = "Safe"

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.heading))
        self.y += self.speed * math.sin(math.radians(self.heading))

    def velocity(self):
        vx = self.speed * math.cos(math.radians(self.heading))
        vy = self.speed * math.sin(math.radians(self.heading))
        return vx, vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 8)
        endx = self.x + 20 * math.cos(math.radians(self.heading))
        endy = self.y + 20 * math.sin(math.radians(self.heading))
        pygame.draw.line(screen, self.color, (self.x, self.y), (endx, endy), 2)
