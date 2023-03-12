from scenarios.base_scenario import BaseScenario
import random
import math

class LineSegmentsVariableWeight(BaseScenario):
    
    def __init__(self, *args, **kwargs,):
        # calling super first, so if we want to override things we can
        super().__init__(*args, **kwargs)
       
        # scenario specific stuff here
        # self.name = 'ASR' # analog shift register
        # self.funct = self.asr
        # self.run()
        
        self.name = 'sine_1'
        self.funct = self.sine
        self.cycle = 0
        self.freq = 1
        self.run()
        
        self.name = 'sine_3'
        self.funct = self.sine
        self.cycle = 0
        self.freq = 3
        self.run()
        
        self.name = 'sine_5'
        self.funct = self.sine
        self.cycle = 0
        self.freq = 5
        self.run()
        
        self.name = 'sine_7'
        self.funct = self.sine
        self.cycle = 0
        self.freq = 7
        self.run()

        
        
    def draw(self):
        self.tiling(0, 0, 200, 5, self.funct) ## this feels like it shouldn't be part of this class, injectable?

    def asr(self):
        return .5
    
    def sine(self):
        
        # calculate value for this cycle
        # wave is between zero and one
        # frequency is arbitrary, to be played with
        value = math.fabs(math.sin(self.cycle * self.freq))
        # increment cycle
        self.cycle +=1
        # return calculated value
        return value

    def tiling(self, x, y, s, l, wf):
        if l == 0:
            if random.random() < wf():
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
            self.tiling(x - s, y + s, s, l, wf)
            self.tiling(x + s, y + s, s, l, wf)
            self.tiling(x - s, y - s, s, l, wf)
            self.tiling(x + s, y - s, s, l, wf)

    def next_svg_name(self):
        # doing a bunch of math on the weight to make a nice filename
        # now represents a percentage of horizontal vs vertical
        filename = f"outputs/finished_pieces/line_segments_variable_{self.iterations}_{self.name}.svg"
        self.iterations += 1
        return filename
        
        

