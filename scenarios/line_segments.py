from scenarios.base_scenario import BaseScenario
import random

class LineSegments(BaseScenario):
    
    def __init__(self, *args, **kwargs,):
        # calling super first, so if we want to override things we can
        super().__init__(*args, **kwargs)
       
        # scenario specific stuff here
        self.horizontal_weight = .95
        self.run()

        self.horizontal_weight = .5
        self.run()

        self.horizontal_weight = .05
        self.run()
        
    def draw(self):
        self.tiling(0, 0, 200, 5) ## this feels like it shouldn't be part of this class, injectable?


    def tiling(self, x, y, s, l):
        if l == 0:
            if random.random() < self.horizontal_weight:
                self.turtle.penup()
                self.turtle.goto(x, y - s)
                self.turtle.pendown()
                self.turtle.goto(x, y + s)
            else:
                self.turtle.penup()
                self.turtle.goto(x - s, y)
                self.turtle.pendown()
                self.turtle.goto(x + s, y)
        else:
            s /= 2
            l -= 1
            self.tiling(x - s, y + s, s, l)
            self.tiling(x + s, y + s, s, l)
            self.tiling(x - s, y - s, s, l)
            self.tiling(x + s, y - s, s, l)

    def next_svg_name(self):
        # doing a bunch of math on the weight to make a nice filename
        # now represents a percentage of horizontal vs vertical
        filename = f"outputs/finished_pieces/line_segments_{self.iterations}_{self.horizontal_weight*100:.0f}.svg"
        self.iterations += 1
        return filename
        
        

