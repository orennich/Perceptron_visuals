from manim import *
from perceptron import perceptron

# create the perceptron object, classify the points
obj = perceptron(2)
obj.classify()

class Perceptron(Scene):
    def construct(self):
        
        dots = []
        for set in [0,1]:
            color = '#00FF00' if set == 1 else '#FF0000'
            for i in range(len(obj.data[set][0])):
                point = [obj.data[set].T[i][0], obj.data[set].T[i][1], 0]
                d = Dot(point, radius=0.05, color=color)
                dots.append(d)
                
        group = VGroup(*dots)
        self.add(group)
        
        self.play(FadeIn(group))
        
        
        
        
        
        grid = Axes(
            x_range=[-1, 1, 0.2],  # step size determines num_decimal_places.
            y_range=[-1, 1, 0.2],
            x_length=6,
            y_length=6,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.2, 0.2),
                "font_size": 20,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Perceptron Algorithm Visualization",
            include_underline=False,
            font_size=32,
        )
        
        self.add(title, grid)
        self.play(Create(title), Create(grid))
        self.wait()
        
        
        
        # create a mobject for the theta vector
        theta_mobj = Arrow(ORIGIN, [0,0,0], buff=0)
        self.add(theta_mobj)
        self.play(Create(theta_mobj))
        
        classifier = None
        
        text = Tex('')
        text.next_to(grid, RIGHT, buff=0.5)
        self.add(text)
        
        
        
        
        
        
        
        
        text2 = Tex("Update Theta", font_size=22, color=WHITE)
        text2.next_to(grid, RIGHT, buff = 0.75)
        self.add(text2)
        
        text1 = Tex("Find an Unclassified Point", font_size=22, color=WHITE)
        text1.next_to(text2, UP, buff = 0.5)
        self.add(text1)
        
        titletext = Tex("Perceptron Algorithm:", font_size=30, color=WHITE)
        titletext.next_to(text1, UP)
        
        
        text3 = Tex("Draw New Linear Classifier", font_size=22, color=WHITE)
        text3.next_to(text2, DOWN, buff = 0.5)
        self.add(text3)
        self.play(
            FadeIn(text1),
            FadeIn(text2),
            FadeIn(text3),
        )
        
        
        
        
        
        for i in range(1, len(obj.theta)):
            # for each theta in obj.theta
            # and update vector in obj.updates
            # plot the current classifier guess, then the update step, then the updated classifier guess.
            
            framebox1 = SurroundingRectangle(text1, buff = .1)
            framebox2 = SurroundingRectangle(text2, buff = .1)
            framebox3 = SurroundingRectangle(text3, buff = .1)
            
            self.play(FadeIn(framebox1))
            
            
            unclassified_dot = Dot([obj.updates[i][0], obj.updates[i][1], 0], radius=0.05, color='#FFFF00')
            self.add(unclassified_dot)
            self.play(Create(unclassified_dot))
            
            self.wait(0.5)
            self.play(
                ReplacementTransform(framebox1, framebox2),
            )
            self.wait(0.5)
            
            
            
            new_theta_mobj = Arrow(ORIGIN, [obj.theta[i][0], obj.theta[i][1], 0], buff=0)
            self.play(
                ReplacementTransform(theta_mobj, new_theta_mobj),
            )
            theta_mobj = new_theta_mobj
            
            self.wait(0.5)
            
            
            self.play(ReplacementTransform(framebox2, framebox3))

            if i == 1:
                classifier = grid.plot(lambda x: 0, color=WHITE)
            
            new_classifier = grid.plot(lambda x: (-obj.theta[i][0]/obj.theta[i][1])*x, color=BLUE)
            self.play(
                ReplacementTransform(classifier, new_classifier),
            )
            classifier = new_classifier
            
            self.remove(framebox3)
            self.remove(unclassified_dot)
            
            
            
            if i == 2:
                break
            
            
            
            
        
        
        
        
        # arrow1 = Arrow(ORIGIN, [2, 2, 0], buff=0)
        # arrow2 = Arrow(ORIGIN, [3, 2, 0], buff=0)
        # numberplane = NumberPlane()
        # origin_text = Text('(0, 0)').next_to(dot, DOWN)
        # tip_text = Text('(2, 2)').next_to(arrow1.get_end(), RIGHT)
        # self.add(numberplane, dot, arrow1, origin_text, tip_text)
        

#        self.wait()
#        self.play(
#            ReplacementTransform(arrow1, arrow2),
#        )
