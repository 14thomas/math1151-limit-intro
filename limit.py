from manim import *

custom_color = "#9fa2e5"
custom_light = "#bdc0eb"
custom_dark = "#272a6d"
custom_pink = "#ffc3c3"

class IntroScene(Scene):
    def construct(self):
        title = Text("Introduction to Limits", font_size=48, color=custom_color)
        self.play(Write(title))
        self.wait(0.7)
        self.play(FadeOut(title))

        plane = NumberPlane(
            x_range=[-10, 10, 2],
            y_range=[-10, 10, 2],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.6
            }
        )
        self.play(FadeIn(plane))

        cubic_function = lambda x: 0.5 * (x - 1) * (x - 3) * (x + 1)

        limit_x = 2.1547

        cubic_curve_before = plane.plot(cubic_function, color=custom_color, x_range=[-10, limit_x - 0.1]) 
        cubic_curve_after = plane.plot(cubic_function, color=custom_color, x_range=[limit_x + 0.1, 10])

        limit_point = plane.c2p(limit_x, cubic_function(limit_x))
        limit_dot = Circle(radius=0.1, color=custom_color, fill_opacity=0)
        limit_dot.move_to(limit_point)

        start_x = -0.81
        moving_dot = Dot(plane.c2p(start_x, cubic_function(start_x)), color=custom_pink)
        self.play(FadeIn(cubic_curve_before, cubic_curve_after, limit_dot, moving_dot))

        path = plane.plot(cubic_function, x_range=[start_x, limit_x], color=custom_pink)
        
        self.play(MoveAlongPath(moving_dot, path, rate_func=rush_from), run_time=5)

        self.wait(2)