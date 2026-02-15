
from manim import *

from util_functions.optics_reflections import intersection

config.max_files_cached = 5000

class HyperbolicCurves(Scene):
    def construct(self):


        plane = NumberPlane()
        '''
        introducing hyperbolic curves
        '''
        #showing the hyperbolic curves

        x_coord = ValueTracker(1)
        y_coord=ValueTracker(1)
        initial_formula = MathTex("x^2+y^2=1")
        self.play(Write(initial_formula))
        self.wait(1)
        self.play(initial_formula.animate.shift(UP*2))

        formula = always_redraw(
            lambda:
            MathTex(
                fr"{x_coord.get_value():.2f}x^2+{y_coord.get_value():.2f}y^2=1"
            ).shift(UP*2) if y_coord.get_value() > 0 else MathTex(
                fr"{x_coord.get_value():.2f}x^2-{-y_coord.get_value():.2f}y^2=1"
            ).shift(UP*2)
        )
        hyperbolic_graph = always_redraw(
            lambda:
            ImplicitFunction(
                lambda x,y: x_coord.get_value()*x**2+y_coord.get_value()*y**2-1
            ).set_color(YELLOW)

        #adjusting the value of a and b
        )
        static_formula = MathTex(
            fr"1.00x^2+1.00y^2=1"
        ).shift(UP*2)
        self.play(Create(plane),Create(hyperbolic_graph))
        self.wait(1)
        self.play(Transform(initial_formula, static_formula))
        self.remove(initial_formula)
        self.add((formula))
        self.wait(1)
        self.play(
            x_coord.animate.set_value(0.5),
            y_coord.animate.set_value(1.3)
            ,run_time=2
        )
        self.wait(1)
        self.play(
            x_coord.animate.set_value(1.2),
            y_coord.animate.set_value(0.3),run_time=2
        )
        self.wait(1)

        self.play(
            x_coord.animate.set_value(0.2),
            y_coord.animate.set_value(0.2),run_time=2
        )
        self.wait(1)
        self.play(
            x_coord.animate.set_value(1),
            y_coord.animate.set_value(1),run_time=2
        )
        self.wait(3)
        parameter = ValueTracker(0.5)
        dot = always_redraw(
            lambda: Dot(
                plane.c2p(
                    np.cosh(parameter.get_value()),
                    np.sinh(parameter.get_value())
                )
            )
        )
        self.play(y_coord.animate.set_value(0))
        self.play(y_coord.animate.set_value(-1))



        hyperbolic_curve_name = Text("双曲线").scale(2)
        self.play(
            FadeOut(formula),
            Write(hyperbolic_curve_name)
        )
        self.wait()
        self.play(Unwrite(hyperbolic_curve_name))





        """
        introducing hyperbolic function and its geometrical meaning
        """
        axes = Axes(
            x_length=14,
            y_length=8
        )
        # the line which is vertical to number plane x axis and pass the point
        vertical_line = always_redraw(
            lambda:
            Line(dot.get_center(), plane.c2p(np.cosh(parameter.get_value()), 0),color=YELLOW)
        )
        horizontal_line = always_redraw(
            lambda :
            Line(
                ORIGIN,
                plane.c2p(
                    np.cosh(parameter.get_value()), 0)
            , color=YELLOW
            )
        )
        origin_to_dot = always_redraw(
            lambda: Line(plane.get_origin(), dot.get_center(), color=YELLOW)
        )

        brace_v = always_redraw(lambda: Brace(vertical_line, RIGHT))
        brace_h = always_redraw(
            lambda:
            Brace(horizontal_line, DOWN) if parameter.get_value() > 0 else
            Brace(horizontal_line, UP)
        )

        label_sinh = always_redraw(
            lambda: MathTex(r"\sinh a").next_to(brace_v, RIGHT, buff=0.1)
        )
        label_cosh = always_redraw(
            lambda: MathTex(r"\cosh a").next_to(brace_h, DOWN, buff=0.1)
            if parameter.get_value() > 0
            else MathTex(r"\cosh a").next_to(brace_h, UP, buff=0.1)
        )

        # Group them for the Create animation
        lines_for_hyperbolic_functions = VGroup(
            origin_to_dot,
            vertical_line,
            horizontal_line,
            brace_v,
            brace_h,
            label_sinh,
            label_cosh
        )
        area = always_redraw(
            lambda:
            MathTex("a").
            set_x(
                2 * np.sinh(
                    parameter.get_value()
                )/(3*parameter.get_value())).
            set_y(
                2*(
                    np.cosh(
                    parameter.get_value()
                    )-1
                )/(3*parameter.get_value())
            )
        )
        hyperbolic_graph_blue = ImplicitFunction(
                lambda x, y:   x ** 2 - y ** 2 - 1
            ).set_color(BLUE)


        self.play(
            FadeOut(plane),
            FadeIn(axes),
            ReplacementTransform(
                hyperbolic_graph,
                hyperbolic_graph_blue
            )
        )
        self.wait(1)

        self.play(
            Create(dot),
            Create(lines_for_hyperbolic_functions),
            Create(area)

        )
        self.wait(1)


        self.play(parameter.animate.set_value(1.2),run_time=2)
        self.wait(1)
        self.play(parameter.animate.set_value(0.5),run_time=2)
        self.wait(1)
        self.play(parameter.animate.set_value(-1.4),run_time=2)
        self.wait(1)
        hyp_formula = VGroup(
            MathTex(r"\sinh x = {e^x-e^{-x}\over2}"),
            MathTex(r"\cosh x = {e^x+e^{-x}\over2}"),
        ).arrange(DOWN).shift(UP*2+RIGHT*5)
        self.play(Create(hyp_formula))
        self.wait(2)
        self.play(
            FadeOut(hyp_formula),
            FadeOut(lines_for_hyperbolic_functions),
            FadeOut(area),
            FadeOut(dot)
        )



        """
        optics:light reflection
        """
        foci1 = Dot(axes.c2p(np.sqrt(2),0),color=RED)
        foci2 = Dot(axes.c2p(-np.sqrt(2),0),color=RED)
        self.play(Create(foci1),Create(foci2))
        self.wait(1)

        theta = [i for i in range(-30,35,5)]

        theoretical_light = VGroup()
        real_light = VGroup()
        reflected_light = VGroup()

        screen_left_edge_scene = np.array([-config.frame_width / 2, 0, 0])
        x_left_math = axes.p2c(screen_left_edge_scene)[0]


        for angle in theta:
            # A. Setup Math
            slope = np.tan(np.deg2rad(angle))

            # B. Calculate Intersection (Math Coords)
            # Use your utility function to find where the ray hits the hyperbola
            intersect_coords = intersection(slope)  # returns [x, y]
            x_int, y_int = intersect_coords

            # C. Calculate Start Point on Left Wall (Math Coords)
            # Use the line equation: y = slope * (x - x_focus)
            y_start_math = slope * (x_left_math - np.sqrt(2))

            # D. Convert ALL points to Scene Coords (c2p)
            # This ensures the scaling matches perfectly
            p_focus_scene = axes.c2p(np.sqrt(2), 0)
            p_second_focus_scene = axes.c2p(-np.sqrt(2), 0)
            p_intersect_scene = axes.c2p(x_int, y_int)
            p_start_scene = axes.c2p(x_left_math, y_start_math)

            # E. Create Lines
            # Theoretical: From Focus to Intersection
            theo_line = DashedLine(p_focus_scene, p_start_scene, color=WHITE)
            theoretical_light.add(theo_line)

            # Real: From Left Wall to Intersection
            real_line = Line(p_start_scene, p_intersect_scene, color=WHITE)
            real_light.add(real_line)

            reflected_line = Line(p_intersect_scene, p_second_focus_scene, color=WHITE)
            reflected_light.add(reflected_line)

        self.play(LaggedStart(

            *[Create(theoretical_light[i]) for i in range(len(theoretical_light))]
            )
        )
        self.play(
            LaggedStart(
                *[
                    Succession(
                        Create(real_light[i]),
                        Create(reflected_light[i])
                    )
                    for i in range(len(theoretical_light))
                ],
                lag_ratio=0.1  # Adjust this to control the delay between each pair
            )
        )
        self.wait(2)
        self.play(
            FadeOut(real_light),
            FadeOut(reflected_light),
            FadeOut(theoretical_light),
            FadeOut(axes),
            FadeOut(foci1),
            FadeOut(foci2),
            hyperbolic_graph_blue.animate.shift(LEFT*3)
        )
        hyper_tesselation = ImageMobject("tess_5_4.gif").scale(2).shift(RIGHT*3)
        hyper_explain = Text("双曲几何").next_to(hyper_tesselation, DOWN)

        self.play(
            FadeIn(hyper_tesselation),
            FadeIn(hyper_explain),
        )
        self.wait(10)























