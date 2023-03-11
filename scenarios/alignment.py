from scenarios.base_scenario import BaseScenario

class Alignment(BaseScenario):
    
    def __init__(self, *args, **kwargs,):
        # calling super first, so if we want to override things we can
        super().__init__(*args, **kwargs)
       
        # scenario specific stuff here
        self.offset = 2
        self.run()
        self.offset = 5
        self.run()

        
    def draw(self):
        self.turtle.penup()
        self.turtle.goto(-self.width+self.offset, self.height-self.offset,)

        self.turtle.pendown()
        
        # drawing a simple rectangle
        self.turtle.goto(-self.width+self.offset, -self.height+self.offset,)
        self.turtle.goto(self.width-self.offset, -self.height+self.offset,)

    def next_svg_name(self):
        filename = f"outputs/tools/simple_alignment_square_{self.offset}.svg"
        self.iterations += 1
        return filename
        
        

