from turtles.base_turtle import BaseTurtle

from svg_turtle import SvgTurtle


class ImageTurtle(BaseTurtle):
    
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        super().__init__(*args, **kwargs)
    
    def setup(self):
        self.turtle = SvgTurtle(self.pixel_w, self.pixel_h)

    def teardown(self):
        self.turtle.save_as(self.filename)
        
    
    
if __name__ == "__main__":
    
    it = ImageTurtle('outputs/myfake_filename.svg', 6.1, 9.3)
    it.setup()
    print(it.turtle)
    print(it.filename)
    print(it.pixel_h, it.pixel_w)
    it.teardown()