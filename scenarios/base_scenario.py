from abc import ABC, abstractmethod

from turtles.image_turtle import ImageTurtle
from turtles.preview_turtle import PreviewTurtle


class BaseScenario(ABC):
    
    def __init__(self, previewMode, canvas_height=6, canvas_width=9):
        self.previewMode = previewMode
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        
        self.iterations = 0

        
    def get_turtle(self):
        if self.previewMode:
            # passing in all the args b/c base class isn't quite working as expected with args
            # need to figure this out
            self.turtleClass = PreviewTurtle(False, self.next_svg_name(), self.canvas_height, self.canvas_width)
        else:
            self.turtleClass = ImageTurtle(self.next_svg_name(), self.canvas_height, self.canvas_width)
            
        self.turtleClass.setup()
        self.turtle = self.turtleClass.turtle
        self.width = self.turtleClass.pixel_w / 2
        self.height = self.turtleClass.pixel_h / 2
    
    def run(self):
        self.get_turtle()
        self.draw()
        self.turtleClass.wait()
        self.turtleClass.teardown()
    
    
    def next_svg_name(self):
        pass