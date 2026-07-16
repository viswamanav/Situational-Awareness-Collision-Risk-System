import math

class RiskAnalyzer:

    def analyze(self, own_ship, targets):
        data = []

        for ship in targets:

            rx = ship.x - own_ship.x
            ry = ship.y - own_ship.y

            ovx, ovy = own_ship.velocity()
            tvx, tvy = ship.velocity()

            rvx = tvx - ovx
            rvy = tvy - ovy

            vr2 = rvx*rvx + rvy*rvy

            if vr2 == 0:
                tcpa = 0
            else:
                tcpa = -(rx*rvx + ry*rvy)/vr2

            cx = rx + rvx*tcpa
            cy = ry + rvy*tcpa

            cpa = math.sqrt(cx*cx + cy*cy)

            ship.cpa = cpa
            ship.tcpa = tcpa

            if cpa < 60 and tcpa > 0:
                ship.risk = "Danger"
                ship.color = (255,0,0)
            elif cpa < 120 and tcpa > 0:
                ship.risk = "Warning"
                ship.color = (255,255,0)
            else:
                ship.risk = "Safe"
                ship.color = (0,255,0)

            data.append(ship)

        return data
