import pygame
from simulation import Simulation
from risk import RiskAnalyzer
from ui import Renderer

pygame.init()

screen=pygame.display.set_mode((1000,700))
pygame.display.set_caption("Situational Awareness")

clock=pygame.time.Clock()

sim=Simulation()
risk=RiskAnalyzer()
ui=Renderer()
zoom = 1.0
offset_x = 0
offset_y = 0
dragging = False
last_mouse = (0, 0)

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        
        # Zoom using mouse wheel
        if event.type == pygame.MOUSEWHEEL:

            if event.y > 0:
                zoom *= 1.1

            if event.y < 0:
                zoom /= 1.1

            zoom = max(0.5, min(zoom, 4))


        # Start dragging
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                dragging = True
                last_mouse = pygame.mouse.get_pos()


        # Stop dragging
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                dragging = False


        # Pan
        if event.type == pygame.MOUSEMOTION and dragging:

            mx, my = pygame.mouse.get_pos()

            dx = mx - last_mouse[0]
            dy = my - last_mouse[1]

            offset_x += dx
            offset_y += dy

            last_mouse = (mx, my)

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_SPACE:
                sim.running=not sim.running

            if event.key==pygame.K_a:
                sim.add_target()

            if event.key==pygame.K_d:
                sim.remove_target()

    sim.update()

    ships=risk.analyze(sim.own_ship,sim.targets)

    ui.draw(screen, sim, ships, zoom, offset_x, offset_y)

    clock.tick(60)

pygame.quit()
