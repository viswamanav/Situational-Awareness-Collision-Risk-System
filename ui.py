import pygame
import math


class Renderer:

    def __init__(self):
        self.font = pygame.font.SysFont(None, 22)

    def convert(self, x, y, zoom, offset_x, offset_y):

        CENTER_X = 500
        CENTER_Y = 350

        sx = (x - CENTER_X) * zoom + CENTER_X + offset_x
        sy = (y - CENTER_Y) * zoom + CENTER_Y + offset_y

        return sx, sy

    def draw(self, screen, sim, ships, zoom, offset_x, offset_y):

        screen.fill((15, 25, 45))

        CENTER_X = 500
        CENTER_Y = 350

        #Radar Rings
        for r in [100, 200, 300, 400]:

            pygame.draw.circle(screen,(70, 70, 70),(CENTER_X + offset_x, CENTER_Y + offset_y),int(r * zoom),1)

        #Own Ship
        x, y = self.convert(sim.own_ship.x,sim.own_ship.y,zoom,offset_x,offset_y )

        pygame.draw.circle(screen,(0, 255, 255),(int(x), int(y)),max(3, int(8 * zoom)))

        #Heading Line
        endx = x + math.cos(math.radians(sim.own_ship.heading)) * 25 * zoom
        endy = y + math.sin(math.radians(sim.own_ship.heading)) * 25 * zoom

        pygame.draw.line(screen,(0, 255, 255),(x, y),(endx, endy),2)
        # Draw Target Ships
        for ship in ships:

            x, y = self.convert(ship.x,ship.y,zoom,offset_x,offset_y)

            pygame.draw.circle(
                screen,
                ship.color,
                (int(x), int(y)),
                max(3, int(8 * zoom))
            )
            # Heading Arrow
            endx = x + math.cos(math.radians(ship.heading)) * 25 * zoom
            endy = y + math.sin(math.radians(ship.heading)) * 25 * zoom
            pygame.draw.line(screen,ship.color,(x, y),(endx, endy),2)

            # Ship ID
            txt = self.font.render(ship.ship_id,True,(255, 255, 255))

            screen.blit(txt, (x + 10, y))

        #Right info panel
        pygame.draw.rect(screen,(40, 40, 40),(760, 0, 240, 700))

        title = self.font.render(
            "Target Information",
            True,
            (0, 255, 255)
        )
        screen.blit(title, (775, 10))
        y_text = 45

        for ship in ships:

            screen.blit(
                self.font.render(
                    f"{ship.ship_id}   {ship.risk}",
                    True,
                    (255, 255, 255)
                ),
                (770, y_text)
            )
            y_text += 20

            screen.blit(
                self.font.render(
                    f"CPA : {ship.cpa:.1f}",
                    True,
                    (255, 255, 255)
                ),
                (770, y_text)
            )
            y_text += 20

            screen.blit(
                self.font.render(
                    f"TCPA : {ship.tcpa:.1f}",
                    True,
                    (255, 255, 255)
                ),
                (770, y_text)
            )
            y_text += 30
        pygame.display.flip()