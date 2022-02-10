from manim import *
from matplotlib import mathtext


class Introduction(Scene):
        def construct(self):
             headline = Text('Developing graphical intuition in math')

             self.play(FadeIn(headline))
             self.wait(2)
             self.play(FadeOut(headline))


class Plot1(Scene):
        def construct(self):
            
             plane = NumberPlane(x_range=[-50,50,1],y_range=[-50,50,1] ,x_length=100,y_length=100).set_opacity(0.2)

             
             polynomialGroup = VGroup()
             labelGroup = VGroup()
             degree = 5
             for n in range(degree+1):
                 if(n%2==0):
                     clr = RED
                 else:
                     clr= BLUE
                 func =plane.plot(lambda x : x**n,color=clr)
                
                 polynomialGroup.add(func)
                 labelGroup.add(MathTex(f"y=x^{n}").shift(LEFT*6,UP*3.5))
             
             self.play(FadeIn(plane),run_time=5)
             self.play(plane.animate.add_coordinates())
             self.wait(2)

             for x in range(degree): 
                 self.play(Transform(polynomialGroup[x],polynomialGroup[x+1]),Transform(labelGroup[x],labelGroup[x+1]),run_time=4)
                 self.wait(2)   
                 self.remove(polynomialGroup[x],labelGroup[x])

          
             
