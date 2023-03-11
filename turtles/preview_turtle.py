from turtles.base_turtle import BaseTurtle

from turtle import Screen, Turtle

class PreviewTurtle(BaseTurtle):
    
    def __init__(self, draw_turtle=False, *args, **kwargs):
        self.draw_turtle = draw_turtle
        super().__init__(*args, **kwargs)
    
    def setup(self):
        self.screen = Screen()
        # create a screen the right size
        self.screen.setup(self.pixel_w, self.pixel_h)
        preview_turtle = Turtle()
        # maybe this should be an option? but it seems fine as is for now
        
        if not self.draw_turtle:
            preview_turtle.hideturtle()
        
        # self.screen.tracer(False)
        
        self.turtle = preview_turtle
    
    def teardown(self):
        self.screen.tracer(True)
        # stick around until user input
        self.screen.exitonclick()
    
    
if __name__ == "__main__":
    
    pt = PreviewTurtle()
    pt.setup()
    print(pt.turtle)
    print(pt.draw_turtle)
    print(pt.pixel_h, pt.pixel_w)
    pt.teardown()