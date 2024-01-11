import pygame as pg
from OpenGL.GL import *
import numpy as np


class App:

    def __init__(self):

        # initilize python
        pg.init()
        pg.display.set_mode((640 , 480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        print("initilized")
        # initilize opengl
        glClearColor(0.1 , 0.2 ,0.2 ,1 )
        self.mainLoop()

    
    def mainLoop(self):
        running = True
        while running:
            # check events
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            # timing # update clock
            self.clock.tick(60)
        self.quit()


    def quit(self):
        pg.quit()

class Triangle :  
    
        def __init__(self):
            
             #x , y , z , r , g , b
            self.vertices =(
                ( 0 , 1 , 0 , 1 , 0 , 0 ),
                (-1 ,-1 , 0 , 0 , 1 , 0 ),
                ( 1 ,-1 , 0 , 0 , 0 , 1 ),
            )
            self.certices = np.array(self.vertices , dtype=np.float32)

            self.vertex._count = 3
            self.vao =glGenVertexArrays(1)
            glBindVertexArray(self.vao)
            self.vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER , self.vbo)
            glBufferData(GL_ARRAY_BUFFER , self.vertices.nbytes , self.vertices , GL_STATIC_DRAW)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0 , 3 , GL_FLOAT , GL_FALSE , 24 , ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1 , 3 , GL_FLOAT , GL_FALSE , 24 , ctypes.c_void_p(12))


        def draw(self):
            pass



if __name__ == "__main__":
    myApp = App()
