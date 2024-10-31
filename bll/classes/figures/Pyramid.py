import math
from bll.classes.figures.BaseFigure import BaseFigure

class Pyramid(BaseFigure):
    def __init__(self, radius: int):
        super().__init__(radius)
        self.radius = radius

    def get_two_d_art(self):
        result = ""
        for h in range(-self.radius, self.radius):
            row = ""
            for w in range(-self.radius, self.radius):
                dist = math.sqrt(h ** 2 + w ** 2)
                if dist < self.radius - 0.5:
                    row += "*"
                elif dist < self.radius:
                    row += "."
                else:
                    row += " "
            result += row + "\n"
        return result

    def get_three_d_art(self):
        result = ""
        levels = self.radius
        for i in range(levels):
            padding = ' ' * (levels - i - 1)  
            main_layer = '*' * (2 * i + 1)   
            side_layer = '/' if i < levels - 1 else '' 
            
            layer = f"{padding}{main_layer} {side_layer}"
            result += layer + "\n"

        return result
