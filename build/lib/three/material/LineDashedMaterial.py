from OpenGL.GL import *
from three.core import OpenGLUtils
from three.material import LineBasicMaterial

class LineDashedMaterial(LineBasicMaterial):
        
    def __init__(self, color=[1,1,1], alpha=1, lineWidth=4, dashLength=0.50, gapLength=0.25, useVertexColors=False):

        super().__init__(color=color, alpha=alpha, lineWidth=lineWidth, useVertexColors=useVertexColors)

        self.setUniform( "bool", "useDashes", 1 )
        self.setUniform( "float", "dashLength", dashLength )
        self.setUniform( "float", "gapLength", gapLength )
