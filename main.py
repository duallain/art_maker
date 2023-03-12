


from scenarios.alignment import Alignment
from scenarios.line_segments import LineSegments
from scenarios.line_segments_variable_weight import LineSegmentsVariableWeight

if __name__ == "__main__":
    
    # should make this an argument
    previewMode = False
    
    
    # create one or more scenarios, passing the turtle in
    # should figure out a good way to make this user interactable
    Alignment(previewMode)
    LineSegments(previewMode)
    LineSegmentsVariableWeight(previewMode)
    
    
