from abc import ABC, abstractmethod

class BaseTurtle(ABC):
    
    def __init__(self, canvas_height=6, canvas_width=9):
        self.pixel_h = self._inches_to_pixels(canvas_height)
        self.pixel_w = self._inches_to_pixels(canvas_width)
            
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def teardown(self):
        pass

    def wait(self):
        pass

    def _inches_to_pixels(self, inches):
        inches_to_pixels = 96

        return round(inches * inches_to_pixels, 3)