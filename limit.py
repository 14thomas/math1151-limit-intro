from manim import *

custom_color = "#9fa2e5"
custom_light = "#bdc0eb"
custom_dark = "#272a6d"
custom_pink = "#ffc3c3"

class IntroScene(Scene):
    def construct(self):
        title = Text("Introduction to Limits", font_size=48, color=custom_color)
        self.play(Write(title))
        self.wait(5)
        self.play(FadeOut(title))

        # Original equation
        title2 = MathTex(r"f(x) = \frac{x^2 + 2}{x^2 + 1}").scale(0.8)
        self.play(Write(title2))
        self.wait(3)

        # Move the equation to a target position
        target_position = title2.copy()
        target_position.to_edge(UP + RIGHT)
        target_position.shift(LEFT + DOWN)
        self.play(Transform(title2, target_position), run_time=0.9)
        self.wait(1)
        
        plane = NumberPlane(
            x_range=[-10, 10, 2],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0
            }
        )
        plane.add_coordinates()

        self.play(FadeIn(plane))

        cubic_function = lambda x: (x ** 2 + 2) / (x ** 2 + 1)
        curve = plane.plot(cubic_function, color=custom_color, x_range=[-10, 10]) 
        self.play(FadeIn(curve))

        start_x = 0.3
        limit_x = 8
        moving_dot = Dot(plane.c2p(start_x, cubic_function(start_x)), color=custom_pink)
        self.play(FadeIn(moving_dot))
        path = plane.plot(cubic_function, x_range=[start_x, limit_x], color=custom_pink)
        
        y_line = DashedLine(
            start=plane.c2p(-10, 1),
            end=plane.c2p(10, 1),
            color=custom_light,
            dash_length=0.2
        )
        self.play(FadeIn(y_line))

        self.play(MoveAlongPath(moving_dot, path, rate_func=linear), run_time=5.5)




        eqn2 = MathTex(r"f(\infty) = \frac{\infty^2 + 2}{\infty^2 + 1}").scale(0.8).move_to(title2)
        eqn3 = MathTex(r"f(\infty) = 1").scale(0.8).move_to(title2)

        self.play(ReplacementTransform(title2, eqn2), run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(eqn2, eqn3), run_time=1)
        self.wait(1)
        question_mark = MathTex(r"?").scale(0.8).next_to(eqn3, DOWN, buff=0.3)
        self.play(Write(question_mark), run_time=1)

        self.wait(2)