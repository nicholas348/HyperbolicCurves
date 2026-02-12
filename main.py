from manim import *

class HyperbolicCurves(Scene):
    def construct(self):

        plane = NumberPlane()
        '''
        introducing hyperbolic curves
        '''
        self.play(Create(plane))
        a = ValueTracker(1)
        b=ValueTracker(1)
        formula = always_redraw(
            lambda:
            MathTex(
                fr"{a.get_value():.2f}x^2+{b.get_value():.2f}y^2=1"
            ).shift(UP)
        )
        self.play(Create(formula))
        hyperbolic_graph = always_redraw(
            lambda:
            ImplicitFunction(
                lambda x,y: a.get_value()*x**2+b.get_value()*y**2-1
            ).set_color(YELLOW)
        )
        self.play(Create(hyperbolic_graph))
        self.play(a.animate.set_value(0.5))
        x = ValueTracker(0.5)
        dot = always_redraw(
            lambda: Dot(
                plane.c2p(
                    np.cosh(x.get_value()),
                    np.sinh(x.get_value())
                )
            )
        )



        hyperbolic_curve_name = Text("双曲线").scale(2)

        """
        introducing hyperbolic function and its geometrical meaning
        """
        # the line which is vertical to number plane x axis and pass the point
        vertical_line = Line(Dot(),plane.c2p(np.cosh(x.get_value()),0))
        brace_for_vertical_line =Brace(vertical_line)
        horizontal_line = Line(ORIGIN,plane.c2p(np.cosh(x.get_value()),0))
        brace_for_horizontal_line = Brace(horizontal_line)
        lines_for_hyperbolic_functions =always_redraw(
            lambda:
            VGroup(

                #the line connecting origin to the point
                Line(plane.get_origin(),Dot()),

                #The vertical line of the object
                vertical_line,
                horizontal_line,

                # the line of the object
                brace_for_vertical_line,
                brace_for_horizontal_line,


                #the text of sinh and cosh functions
                brace_for_vertical_line.get_tex(r"\sinh a"),
                brace_for_horizontal_line.get_tex(r"\cosh a")

            )
        )
        area = always_redraw(
            lambda:
            MathTex("a").set_x().set_z()
        )
        self.play(
            Create(dot),
            Create(lines_for_hyperbolic_functions),
            Create(area)
        )
        self.wait(3)


        self.play(a.animate.set_value(-0.2))
















