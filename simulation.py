from vessel import Vessel
import random

class Simulation:
    def __init__(self):
        self.running = True
        self.own_ship = Vessel("OWN", 500, 350, 0, 0, (0,255,255))
        self.targets = []
        for i in range(5):
            self.add_target()

    def add_target(self):
        ship = Vessel(
            f"T{len(self.targets)+1}",
            random.randint(50,950),
            random.randint(50,650),
            random.randint(1,3),
            random.randint(0,359),(0,255,0))
        self.targets.append(ship)

    def remove_target(self):
        if self.targets:
            self.targets.pop()

    def update(self):
        if not self.running:
            return
        for ship in self.targets:
            ship.move()
