from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3))
stone = Material(diffuse = (0.4, 0.4, 0.4))
grass = Material(diffuse = (0.3, 1, 0.3))
snow = Material(diffuse=(0.867, 0.852, 0.848))
black_plastic = Material(diffuse=(0.109375, 0.10546875, 0.10546875))
carrot = Material(diffuse=(0.90625, 0.33984375, 0.1015625))
white_eye = Material(diffuse=(1, 1, 1))
black_eye = Material(diffuse=(0, 0, 0))

rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

rtx.scene.append( Sphere(V3(0,-2,-10), 2, snow)  )
rtx.scene.append( Sphere(V3(0,0,-10), 1.5, snow)  )
rtx.scene.append( Sphere(V3(0,2,-10), 1, snow)  )

rtx.scene.append( Sphere(V3(0,-2,-8), 0.15, black_plastic)  )
rtx.scene.append( Sphere(V3(0,0,-8.5), 0.15, black_plastic)  )
rtx.scene.append( Sphere(V3(0,-.6,-8.5), 0.15, black_plastic)  )

rtx.scene.append( Sphere(V3(0, 1.9,-9), 0.075, carrot)  ) #Nariz
rtx.scene.append( Sphere(V3(-0.1, 1.5,-9.15), 0.05, black_plastic)  )
rtx.scene.append( Sphere(V3(0.1, 1.5,-9.15), 0.05, black_plastic)  )
rtx.scene.append( Sphere(V3(0.3, 1.55,-9.15), 0.05, black_plastic)  )
rtx.scene.append( Sphere(V3(-0.3, 1.55,-9.15), 0.05, black_plastic)  )

rtx.scene.append( Sphere(V3(-0.2, 2.3,-9.1), 0.08, white_eye)  )
rtx.scene.append( Sphere(V3(0.2, 2.3,-9.1), 0.08, white_eye)  )
rtx.scene.append( Sphere(V3(-0.2, 2.3,-9), 0.04, black_eye)  )
rtx.scene.append( Sphere(V3(0.2, 2.3,-9), 0.04, black_eye)  )

rtx.glRender()

rtx.glFinish("output.bmp")