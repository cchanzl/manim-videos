#!/usr/bin/env python

from manimlib.imports import *
from operator import add
import random
import numpy as np


# To watch one of these scenes, run the following:
# python -m manim act_claims_tri.py con_tri -r 1080
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


# Import the data for the triangle
with open("claims.csv") as file_in:
    lines = []
    for line in file_in:
        line = line.rstrip('\n')
        lines.append(line)

#Create each individual scenes
class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 1
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

class OpeningScene(Scene):
    def construct(self):
        grid=ScreenGrid(rows=16, columns=28)
        # self.add(grid)

        v1 = np.array([-5.5, -3.00, 0])
        v2 = np.array([-5.5, 3.55, 0])
        v3 = np.array([5.5, 3.55, 0])
        v4 = np.array([-5.35, -3.00, 0])
        v5 = np.array([5.5, 3.45, 0])
        v6 = np.array([5.5, -3.00, 0])

        tri1 = Polygon(v1, v2, v3)
        tri2 = Polygon(v4, v5, v6)
        tri2.set_color(GREEN)

        self.play(ShowCreation(tri1))
        self.play(ShowCreation(tri2))
        self.wait()

        txt1 = TextMobject("Actuarial")
        txt2 = TextMobject("Claims")
        txt3 = TextMobject("Triangle")
        txt1.set_color(YELLOW)
        txt2.set_color(YELLOW)
        txt3.set_color(YELLOW)
        txt_title = VGroup(txt1, txt2, txt3)
        txt_title.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_title.move_to(np.array([0.5, 0.5, 0]))
        txt_title.scale(4)

        self.play(Write(txt_title))

        self.wait(2)

class OpeningScene2(Scene):
    def construct(self):
        grid = ScreenGrid(rows=16, columns=28)
        # self.add(grid)

        tri = np.arange(-1.75, 3.75, 0.5).tolist()
        ny = 0
        list = []
        for y in tri:
            ny = ny + 1
            for x in range(-5, -5+ny):
                rectangle = Rectangle(height=0.5, width=1, stroke_opacity = 0.15)
                rectangle.move_to(np.array([x,y,0])   )
                list.append(rectangle)
        triangle = VGroup(*list)
        self.play(FadeIn(triangle))

        txt1 = TextMobject("Actuarial")
        txt2 = TextMobject("Claims")
        txt3 = TextMobject("Triangle")
        txt_title = VGroup(txt1, txt2, txt3)
        txt_title.set_color(GREEN)
        txt_title.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_title.move_to(np.array([-0.5, 0.1, 0]))
        txt_title.scale(3.75)

        self.play(Write(txt_title))

        self.wait(2)

class cont_page(Scene):
    def construct(self):
        grid = ScreenGrid(rows=16, columns=28)
        # self.add(grid)
        txt1 = TextMobject("1. Constructing a claims paid triangle")
        txt2 = TextMobject("2. Constructing a claims paid development triangle")
        txt3 = TextMobject("3. Other types of triangles")

        txt_cont = VGroup(txt1, txt2, txt3)
        txt_cont.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_cont.move_to(np.array([0,0.5,0]))
        txt_cont.scale(1.2)

        self.play(Write(txt_cont))

        self.wait(9)

class life_cycle(Scene):
    def construct(self):
        grid = ScreenGrid(rows=26, columns=26)
        # self.add(grid)

        txt0 = TextMobject("Underwriting Year: Year in which the policy was written by the insurer")
        txt0.move_to(np.array([0, 0, 0]))
        txt0.scale(0.75)
        self.play(Write(txt0))
        self.wait(3)

        txt1a = TextMobject("Accident Year: Year in which the loss occurred")
        txt1a.move_to(np.array([0, 0, 0]))
        txt1a.scale(0.75)
        self.play(Transform(txt0, txt1a))

        self.wait(3)

        txt1b = TextMobject("AY2009")
        txt1b.move_to(np.array([-6.05, 2.75, 0]))
        txt1b.scale(0.5)
        self.play(Transform(txt0, txt1b))
        self.wait(1)

        year = TextMobject("Calendar Year")
        year.scale(0.5)
        year.move_to(np.array([-4.5, 3.73, 0]))
        self.play(FadeIn(year))

        listx =[]
        for x, yr in zip(range(-5, 5), range(2009, 2020)):
            vector = np.array([x, 3.35, 0])  # x, y, z
            txt = TextMobject(str(yr))
            txt.move_to(vector)
            txt.scale(0.5)
            listx.append(txt)
        calyr = VGroup(*listx)
        self.play(FadeIn(calyr))

        listx = []
        for x in range(-5, 5):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 2.75, 0]))
            listx.append(rectangle)
        triangle = VGroup(*listx)
        self.play(FadeIn(triangle))
        self.wait(1)

        clm_list1 = lines[0].split(",")
        clm_list2 = lines[1].split(",")

        vector1 = np.array([-5, 2.75, 0])  # x, y, z
        clm1 = TextMobject(str(clm_list1[0]))
        clm1.move_to(vector1)
        clm1.scale(0.7)
        self.play(FadeIn(clm1))
        self.wait(2)

        arrow1 = Arrow(UP, DOWN*0.5) # specify the location of the two ends.
        a_vec1 = np.array([-5, 1.75, 0])  # x, y, z
        arrow1.move_to(a_vec1)
        self.play(GrowArrow(arrow1))

        txt1 = TextMobject("For this policy (\\#1), a loss occurred")
        txt2 = TextMobject("in AY2009 and the insurer paid")
        txt3 = TextMobject("an initial amount of \\$2,000.")
        txt_09 = VGroup(txt1, txt2, txt3)
        txt_09.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_09.move_to(np.array([-3.75,0.5,0]))
        txt_09.scale(0.6)
        self.play(Write(txt_09))
        self.wait(2)

        clm2 = TextMobject(str(clm_list1[1]))
        clm2.move_to(np.array([-4, 2.75, 0]))
        clm2.scale(0.7)
        self.play(FadeIn(clm2))
        self.wait(3)

        listx =[]
        for x, clm in zip(range(-3, 5), clm_list1[2:]):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 2.75, 0]))
            txt.scale(0.7)
            listx.append(txt)
        clm3 = VGroup(*listx)
        self.play(FadeIn(clm3))
        self.wait(1)

        arrow2 = Arrow(UP, DOWN*2) # specify the location of the two ends.
        arrow2.move_to(np.array([-1, 1, 0]))
        arrow2.align_to(arrow1, UP) # top edge lines ups with arrow1's top edge.
        self.play(GrowArrow(arrow2))

        txt1 = TextMobject("For the same policy, it was known")
        txt2 = TextMobject("later in 2013 that the initial sum")
        txt3 = TextMobject("paid was insufficient. The insurer")
        txt4 = TextMobject("paid out a further \\$400.")
        txt_13 = VGroup(txt1, txt2, txt3, txt4)
        txt_13.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_13.move_to(np.array([-1,-1.2,0]))
        txt_13.scale(0.6)
        self.play(Write(txt_13))
        self.wait(2)

        arrow3 = Arrow(UP, DOWN*3.5) # specify the location of the two ends.
        arrow3.move_to(np.array([4, 0.6, 0]))
        arrow3.align_to(arrow2, UP)
        self.play(GrowArrow(arrow3))
        self.wait(2)

        txt1 = TextMobject("9 years after the loss occurred, there is")
        txt2 = TextMobject("no further development in this claim.")
        txt3 = TextMobject("This loss has reached its ultimate")
        txt4 = TextMobject("loss amount of \\$2,400.")
        txt_18 = VGroup(txt1, txt2, txt3, txt4)
        txt_18.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_18.move_to(np.array([4,-2.7,0]))
        txt_18.scale(0.6)
        self.play(Write(txt_18))
        self.wait(2)

        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(txt_09), FadeOut(txt_13), FadeOut(txt_18))
        self.wait(2)

        txt1 = TextMobject("Policy \\#2", tex_to_color_map={"text": YELLOW})
        txt1.move_to(np.array([-5, 1.5, 0]))
        txt1.scale(0.5)

        listx = []
        for x in range(-5, 5):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 0.9, 0]))
            listx.append(rectangle)
        row2 = VGroup(*listx)
        self.play(FadeIn(row2), FadeIn(txt1))
        self.wait(2)

        listx =[]
        for x, clm in zip(range(-5, 5), clm_list2):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 0.9, 0]))
            txt.scale(0.7)
            listx.append(txt)
        claims2 = VGroup(*listx) # For policy #2
        self.play(FadeIn(claims2))
        self.wait(1)

        listx = []
        for x, clm in zip(range(-5, 5), clm_list1):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 2.75, 0]))
            txt.scale(0.7)
            listx.append(txt)
        claims1 = VGroup(*listx) # For policy #1
        self.play(FadeIn(claims1))
        self.wait(1)

        self.play(FadeOut(clm1), FadeOut(clm2), FadeOut(clm3))

        listx = []
        claims_top = [a + b for a, b in zip((int(i) for i in clm_list1), (int(i) for i in clm_list2))]
        for x, clm in zip(range(-5, 5), claims_top):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 2.75, 0]))
            txt.scale(0.7)
            listx.append(txt)
        claims_sum = VGroup(*listx) # For policy #1
        self.play(Transform(claims1, claims_sum),FadeOut(claims2))
        self.wait(1)

        count = 0
        for pol in range(2, 10):
            policy = "Policy \\#" + str(pol+1)
            txt2 = TextMobject(policy)
            txt2.move_to(np.array([-5, 1.5, 0]))
            txt2.scale(0.5)

            listx = []
            for x, clm in zip(range(-5, 5), lines[pol].split(",")):
                txt = TextMobject(str(clm))
                txt.move_to(np.array([x, 0.9, 0]))
                txt.scale(0.7)
                listx.append(txt)
            claims_rand = VGroup(*listx)  # For policy #3 onwards
            self.play(Transform(txt1, txt2), FadeIn(claims_rand))

            claims_top = [a + b for a, b in zip((int(i) for i in lines[pol].split(",")), claims_top)]

            listx = []
            for x, clm in zip(range(-5, 5), claims_top):
                txt = TextMobject(str(clm))
                txt.move_to(np.array([x, 2.75, 0]))
                txt.scale(0.7)
                listx.append(txt)
            claims_sum = VGroup(*listx)
            self.play(Transform(claims1, claims_sum), FadeOut(claims_rand))
            self.wait(0.35)

        self.play(FadeOut(row2), FadeOut(txt1))

        tri = np.arange(-1.75, 3.25, 0.5).tolist()
        listx = []
        for y, yr in zip(tri, ["2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"]):
            calyr = "AY" + yr
            txt1b = TextMobject(calyr)
            txt1b.move_to(np.array([-6.05, y, 0]))
            txt1b.scale(0.5)
            listx.append(txt1b)
        cal_yr = VGroup(*listx)

        ny = 0
        list = []
        for y in tri:
            ny = ny + 1
            for x in range(-5, -5+ny):
                rectangle = Rectangle(height=0.5, width=1)
                rectangle.move_to(np.array([x,y,0]))
                list.append(rectangle)
        triangle = VGroup(*list)
        self.play(FadeIn(triangle), FadeIn(cal_yr))
        self.wait(3)

class con_tri(Scene):
    def construct(self):
        grid = ScreenGrid(rows=30, columns=30)
        # self.add(grid)

        year = TextMobject("Calendar Year")
        year.scale(0.5)
        year.move_to(np.array([-4.5, 3.73, 0]))

        tri = np.arange(-1.75, 3.25, 0.5).tolist()
        listx = []
        for y, yr in zip(tri, ["2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009"]):
            calyr = "AY" + yr
            txt1b = TextMobject(calyr)
            txt1b.move_to(np.array([-6.05, y, 0]))
            txt1b.scale(0.5)
            listx.append(txt1b)
        cal_yr = VGroup(*listx)

        list3 =[]
        for x, yr in zip(range(-5, 5), range(2009, 2020)):
            txt = TextMobject(str(yr))
            txt.move_to(np.array([x, 3.35, 0]))
            txt.scale(0.5)
            list3.append(txt)
        dev_year = VGroup(*list3)

        ny = 0
        list = []
        for y in tri:
            ny = ny + 1
            for x in range(-5, -5+ny):
                rectangle = Rectangle(height=0.5, width=1)
                rectangle.move_to(np.array([x,y,0]) )
                list.append(rectangle)
        triangle = VGroup(*list)
        self.play(FadeIn(dev_year), FadeIn(triangle), FadeIn(cal_yr), FadeIn(year))

        ny = 0
        listx = []
        tri = np.arange(2.75, -2.25, -0.5).tolist()
        start = 0
        end = 10
        latest_diag = []
        count = -1
        for y in tri:
            ny = ny - 1

            claims_sum = (int(i) for i in lines[start].split(","))
            for line in range(start+1, end):
                claims_sum = [a + b for a, b in zip((int(i) for i in lines[line].split(",")), claims_sum)]
            start = start + 10
            end = end + 10

            for x, clm in zip(range(-5, 6+ny), claims_sum):
                txt = TextMobject(str(clm))
                txt.move_to(np.array([x, y, 0]) )
                txt.scale(0.7)
                listx.append(txt)
            claims_row = VGroup(*listx)
            self.play(Transform(claims_row, claims_row))

            latest_diag.append(claims_sum[count])
            count = count - 1

        self.wait(5)
        claims_sum = (int(i) for i in lines[start].split(","))
        for line in range(start+1, end):
            claims_sum = [a + b for a, b in zip((int(i) for i in lines[line].split(",")), claims_sum)]

        latest_diag.append(claims_sum[count])
        self.wait(1)

        listx = []
        tri = np.arange(2.75, -2.75, -0.5).tolist()
        xaxis = np.arange(5, -6, -1).tolist()
        lat_diag = np.arange(0, 11, 1).tolist()
        for x, y, z in zip(xaxis, tri, lat_diag):
            txt = TextMobject(str(latest_diag[z]))
            txt.move_to(np.array([x, y, 0]))
            txt.scale(0.7)
            txt.set_color(GREEN)
            listx.append(txt)
        claims_19 = VGroup(*listx)

        txt_AY2019 = TextMobject("AY2019")
        txt_AY2019.move_to(np.array([-6.05, -2.25, 0]))
        txt_AY2019.scale(0.5)
        txt_AY2019.set_color(GREEN)

        txt_2019 = TextMobject("2019")
        txt_2019.move_to(np.array([5, 3.35, 0]))
        txt_2019.set_color(GREEN)
        txt_2019.scale(0.5)

        txt1 = TextMobject("For every new calendar year of information, we can append")
        txt2 = TextMobject("the additional information to the latest diagonal.")
        txt5 = VGroup(txt1, txt2)
        txt5.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt5.move_to(np.array([0,-3.2,0]))
        txt5.set_color(GREEN)
        txt5.scale(1)

        self.play(FadeIn(claims_19), FadeIn(txt_AY2019), FadeIn(txt_2019), Write(txt5)) # FadeIn for the latest diagonal
        self.wait(13)

        txt_final = TextMobject("And we have constructed our first paid triangle!")
        txt_final.move_to(np.array([0,-3,0]))
        txt_final.scale(1)

        txt_2019.set_color(WHITE)
        txt_AY2019.set_color(WHITE)
        claims_19.set_color(WHITE)

        x = 6
        list = []
        tri = np.arange(2.75, -2.75, -0.5).tolist()
        for y in tri:
            x = x - 1
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x,y,0]))
            list.append(rectangle)
        triangle = VGroup(*list)

        self.play(Transform(txt5, txt_final), ShowCreation(triangle))
        self.wait(3)

        txt_nxt_step = TextMobject("The next step is to understand claims development triangle...")
        txt_nxt_step.move_to(np.array([0,-3,0]))
        txt_nxt_step.scale(1)

        self.play(Transform(txt5, txt_nxt_step))
        self.wait(3)

        self.play(FadeOut(txt5))

class dev_tri(Scene):
    def construct(self):
        grid = ScreenGrid(rows=16, columns=28)
        # self.add(grid)

        year = TextMobject("Calendar Year")
        year.scale(0.5)
        year.move_to(np.array([-4.5, 3.73, 0]))

        tri = np.arange(-2.25, 3.25, 0.5).tolist()
        listx = []
        for y, yr in zip(tri, ["2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009"]):
            calyr = "AY" + yr
            txt1b = TextMobject(calyr)
            txt1b.move_to(np.array([-6.05, y, 0]))
            txt1b.scale(0.5)
            listx.append(txt1b)
        cal_yr = VGroup(*listx)

        listx = []
        for x, yr in zip(range(-5, 6), range(2009, 2020)):
            txt = TextMobject(str(yr))
            txt.move_to(np.array([x, 3.35, 0]))
            txt.scale(0.5)
            listx.append(txt)
        dev_year = VGroup(*listx)

        ny = 0
        listx = []
        for y in tri:
            ny = ny + 1
            for x in range(-5, -5+ny):
                rectangle = Rectangle(height=0.5, width=1)
                rectangle.move_to(  np.array([x,y,0])  )
                listx.append(rectangle)
        triangle = VGroup(*listx)

        ny = 0
        listx = []
        total_claims = []
        tri = np.arange(2.75, -2.75, -0.5).tolist()
        start = 0
        end = 10
        for y in tri:
            ny = ny - 1

            claims_sum = (int(i) for i in lines[start].split(","))
            for line in range(start+1, end):
                claims_sum = [a + b for a, b in zip((int(i) for i in lines[line].split(",")), claims_sum)]
            total_claims.append(claims_sum)
            start = start + 10
            end = end + 10

            for x, clm in zip(range(-5, 7+ny), claims_sum):
                txt = TextMobject(str(clm))
                txt.move_to(np.array([x, y, 0]))
                txt.scale(0.7)
                listx.append(txt)

        claims_tri = VGroup(*listx)
        self.play(FadeIn(triangle), FadeIn(year), FadeIn(cal_yr), FadeIn(dev_year), FadeIn(claims_tri))
        self.wait(2)

        claims_sum_09 = total_claims[0]

        listx = []
        for x, clm in zip(range(-5, 7), claims_sum_09):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 2.75, 0])) # x, y, z
            txt.scale(0.7)
            listx.append(txt)
        claims_top = VGroup(*listx)

        txt1b = TextMobject("AY2009")
        txt1b.move_to(np.array([-6.05, 2.75, 0]))
        txt1b.scale(0.5)

        listx = []
        for x in range(-5, 6):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 2.75, 0])) # x, y, z
            listx.append(rectangle)
        top_row = VGroup(*listx)

        self.play(FadeOut(claims_tri), FadeIn(claims_top), FadeOut(triangle), FadeOut(cal_yr), FadeIn(txt1b), FadeIn(top_row))
        self.wait(2)

        pointer = CurvedArrow(start_point=5 * LEFT, end_point=4 * LEFT)
        pointer.move_to(np.array([-4.5, 2.25, 0]))
        self.play(ShowCreation(pointer))
        self.wait(1)

        arrow1 = Arrow(UP, DOWN*0.5) # specify the location of the two ends.
        arrow1.move_to(np.array([-4.5, 1.5, 0]))

        txt1 = TextMobject("Claims development factor is defined as how")
        txt2 = TextMobject("much the claim has moved from one calendar")
        txt3 = TextMobject("year to the subsequent calendar year.")
        txt_dev = VGroup(txt1, txt2, txt3)
        txt_dev.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_dev.move_to(np.array([-3,0.25,0]))
        txt_dev.scale(0.6)
        self.play(GrowArrow(arrow1), Write(txt_dev))
        self.wait(1)

        claims_09 = (int(i) for i in lines[0].split(","))
        for line in range(1, 10):
            claims_09 = [a + b for a, b in zip((int(i) for i in lines[line].split(",")), claims_09)]

        ratio = '{0:.3f}'.format(total_claims[0][1]/total_claims[0][0])

        text_dev = TexMobject("\\text{", "Claims Development Factor}", "=", "{", total_claims[0][1],"\\over", total_claims[0][0], "}", "=", ratio)
        text_dev[4].set_color(GREEN)
        text_dev[6].set_color(YELLOW)
        text_dev.move_to(np.array([0,-1.5,0]))

        top = TextMobject( str(total_claims[0][1]) )
        top.set_color(GREEN)
        top.scale(0.7)
        top.move_to(np.array([-4,2.75,0]))

        bottom = TextMobject( str(total_claims[0][0]) )
        bottom.set_color(YELLOW)
        bottom.scale(0.7)
        bottom.move_to(np.array([-5,2.75,0]))

        self.play(FadeIn(text_dev), FadeIn(top), FadeIn(bottom))
        self.wait(2)

        row2_head = TextMobject("Claims Development Factor")
        row2_head.move_to(np.array([-4, 1.5, 0]))
        row2_head.scale(0.5)

        listx = []
        for x in range(-5, 5):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 0.9, 0]))
            listx.append(rectangle)
        row2 = VGroup(*listx)

        ratio = TextMobject(str(ratio))
        ratio.scale(0.7)
        ratio.move_to(np.array([-5,0.9,0]))

        self.play(FadeIn(row2), FadeIn(row2_head), FadeIn(ratio), FadeOut(txt_dev), FadeOut(arrow1))
        self.wait(3)

        dev_09 = []
        for i in range(0, 10):
            dev_factor = claims_09[i + 1] / claims_09[i]
            dev_09.append(dev_factor)

        listx = []
        for i, x in zip(range(1, 10), range(-4, 5)):
            development = TextMobject( str( '{0:.3f}'.format(dev_09[i]) ) )
            development.move_to(np.array([x,0.9,0]))
            development.scale(0.7)
            listx.append(development)

            pointer1 = CurvedArrow(start_point=5 * LEFT, end_point=4 * LEFT)
            pointer1.move_to(np.array([x+0.5, 2.25, 0]))

            text_dev2 = TexMobject("\\text{", "Claims Development Factor}", "=", "{", claims_09[i+1], "\\over", claims_09[i], "}", "=", '{0:.3f}'.format(dev_09[i]))
            text_dev2[4].set_color(GREEN)
            text_dev2[6].set_color(YELLOW)
            text_dev2.move_to(np.array([0, -1.5, 0]))

            top2 = TextMobject(str(claims_09[i+1]))
            top2.set_color(GREEN)
            top2.scale(0.7)
            top2.move_to(np.array([x+1, 2.75, 0]))

            bottom2 = TextMobject(str(claims_09[i]))
            bottom2.set_color(YELLOW)
            bottom2.scale(0.7)
            bottom2.move_to(np.array([x, 2.75, 0]))

            self.play(FadeIn(development), Transform(pointer, pointer1), Transform(text_dev, text_dev2), Transform(top, bottom2), Transform(bottom, top2))
            self.wait(2)
        development1 = VGroup(*listx)

        self.wait(1)
        self.play(FadeOut(top), FadeOut(bottom), FadeOut(pointer), FadeOut(text_dev))
        self.wait(1)

        listx = []
        for x in range(-5, 5):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 2.75, 0]))
            listx.append(rectangle)
        row3 = VGroup(*listx)

        listx = []
        for i, x in zip(range(0, 10), range(-5, 5)):
            dev = TextMobject( str( '{0:.3f}'.format(dev_09[i]) ) )
            dev.move_to(np.array([x,2.75,0]))
            dev.scale(0.7)
            listx.append(dev)
        development2 = VGroup(*listx)

        listx = []
        for x, yr in zip(range(-5, 6), range(0, 12)):
            if yr == 10:
                txt = TextMobject(str("Tail"))
            else:
                txt = TextMobject(str(yr), ":", str(yr+1))
            txt.move_to(np.array([x, 3.35, 0]))
            txt.scale(0.5)
            listx.append(txt)
        dev_year2 = VGroup(*listx)

        year2 = TextMobject("Development Period")
        year2.scale(0.5)
        year2.move_to(np.array([-4.25, 3.73, 0]))

        self.play(FadeOut(row2), FadeOut(development1), FadeOut(ratio), FadeOut(row2_head),
                  FadeIn(cal_yr), FadeIn(triangle),
                  Transform(year, year2), Transform(top_row, row3), Transform(claims_top, development2), Transform(dev_year, dev_year2))
        self.wait(3)

        ny = 0
        count = 0
        tri = np.arange(2.25, -2.75, -0.5).tolist()
        for y in tri:
            listx = []
            count = count + 1
            ny = ny - 1
            for x in range(-5, 5+ny):
                txt = TextMobject( str(   '{0:.3f}'.format(total_claims[count][x+6]/total_claims[count][x+5])    ) )
                txt.move_to(np.array([x, y, 0]))
                txt.scale(0.7)
                listx.append(txt)
            claims_dev = VGroup(*listx)
            self.play(FadeIn(claims_dev))
        self.wait(1)

        txt_dev_1 = TextMobject("We have now constructed a complete")
        txt_dev_2 = TextMobject("paid development factor triangle...")
        txt_dev1 = VGroup(txt_dev_1, txt_dev_2)
        txt_dev1.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_dev1.move_to(np.array([0,-3,0]))
        txt_dev1.scale(1)
        self.play(ShowCreation(txt_dev1))
        self.wait(3)
        self.play(FadeOut(txt_dev1))

class incurred(Scene):
    def construct(self):
        grid = ScreenGrid(rows=16, columns=28)
        # self.add(grid)

        txt1b = TextMobject("AY2009")
        txt1b.move_to(np.array([-6.05, 2.75, 0]))
        txt1b.scale(0.5)

        year = TextMobject("Calendar Year")
        year.scale(0.5)
        year.move_to(np.array([-4.5, 3.73, 0]))

        title_txt = TextMobject("Claims Paid")
        title_txt.scale(0.5)
        title_txt.bg = SurroundingRectangle(title_txt,color=BLACK,fill_color=YELLOW, fill_opacity=.5)
        title = VGroup(title_txt, title_txt.bg)
        title.move_to(np.array([-6.25, 3.35, 0]))

        listx = []
        for x in range(-5, 6):
            rectangle = Rectangle(height=0.5, width=1)
            rectangle.move_to(np.array([x, 2.75, 0]))
            listx.append(rectangle)
        top_row = VGroup(*listx)

        clm_list1 = list(int(i) for i in lines[0].split(","))

        listx =[]
        for x, clm in zip(range(-5, 7), clm_list1):
            txt = TextMobject(str(clm))
            txt.move_to(np.array([x, 2.75, 0]))
            txt.scale(0.7)
            listx.append(txt)
        clm3 = VGroup(*listx)

        listx =[]
        for x, yr in zip(range(-5, 6), range(2009, 2020)):
            txt = TextMobject(str(yr))
            txt.move_to(np.array([x, 3.35, 0]))
            txt.scale(0.5)
            listx.append(txt)
        calyr = VGroup(*listx)
        self.play(FadeIn(calyr), FadeIn(txt1b), FadeIn(year), FadeIn(top_row), FadeIn(clm3), FadeIn(title))
        self.wait(3)

        bottom = []
        inc_title = []
        os = 1.2
        inc = -1.8
        for y in (os, inc):
            if y == os:
                title_txt = TextMobject("Claims OS")
                title_txt.scale(0.5)
                title_txt.bg = SurroundingRectangle(title_txt, color=BLACK, fill_color=BLUE, fill_opacity=.5)
            else:
                title_txt = TextMobject("Claims Inc.")
                title_txt.scale(0.5)
                title_txt.bg = SurroundingRectangle(title_txt, color=BLACK, fill_color=GREEN, fill_opacity=.5)
                inc_title.append(title_txt)
                inc_title.append(title_txt.bg)
            title2 = VGroup(title_txt, title_txt.bg)
            title2.move_to(np.array([-6.25, y+0.6, 0]))
            bottom.append(title2)

            listx =[]
            for x, yr in zip(range(-5, 6), range(2009, 2020)):
                txt = TextMobject(str(yr))
                txt.move_to(np.array([x, y+0.6, 0]))
                txt.scale(0.5)
                listx.append(txt)
            calyr = VGroup(*listx)
            bottom.append(calyr)

            txt2b = TextMobject("AY2009")
            txt2b.move_to(np.array([-6.05, y, 0]))
            txt2b.scale(0.5)
            bottom.append(txt2b)

            listx = []
            for x in range(-5, 6):
                rectangle = Rectangle(height=0.5, width=1)
                rectangle.move_to(np.array([x, y, 0]))
                listx.append(rectangle)
            sec_row = VGroup(*listx)
            bottom.append(sec_row)
        os_inc = VGroup(*bottom)

        self.play(FadeIn(os_inc))
        self.wait(3)

        os_list = [200, 200, 200, 400, 0, 0, 0, 0, 0, 0, 0]
        inc_list = [a + b for a, b in zip(clm_list1, os_list)]

        fadeo = []
        for i in (os, inc):
            if i == os:
                txt = TextMobject(str(os_list[0]))
            else:
                txt = TextMobject(str(inc_list[0]))
            txt.move_to(np.array([-5, i, 0]))
            txt.scale(0.7)
            self.play(FadeIn(txt))
            self.wait(1)

            arrow1 = Arrow(UP, DOWN*0.05) # specify the location of the two ends.
            arrow1.move_to(np.array([-5, i-0.6, 0]) )
            self.play(GrowArrow(arrow1))

            if i == os:
                txt1 = TextMobject("For this policy (\\#1), the insurer set")
                txt2 = TextMobject("aside another \\$200 in outstanding")
                txt3 = TextMobject("reserves on top of what was paid out.")
            else:
                txt1 = TextMobject("The total claims incurred for")
                txt2 = TextMobject("this policy is the sum of claims")
                txt3 = TextMobject("paid and claims outstanding.")
            txt_09 = VGroup(txt1, txt2, txt3)
            txt_09.arrange(DOWN, center=False, aligned_edge=LEFT)
            txt_09.move_to(np.array([-5,i-1.4,0]))
            txt_09.scale(0.5)
            fadeo.append(arrow1)
            fadeo.append(txt_09)
            self.play(Write(txt_09))
            self.wait(3)

        gone = VGroup(*fadeo)
        self.wait(2)

        for x, clm in zip(range(-4, -1), range(0, 10)):
            listx = []
            for i in (os, inc):
                if i == os:
                    txt = TextMobject(str(os_list[clm+1]))
                else:
                    txt = TextMobject( str(inc_list[clm+1]) )
                txt.move_to(np.array([x, i, 0]))
                txt.scale(0.7)
                listx.append(txt)
            claims2 = VGroup(*listx) # For policy #2
            self.play(FadeIn(claims2))
            self.wait()

        arrow2 = Arrow(UP, DOWN * 0.05)  # specify the location of the two ends.
        arrow2.move_to(np.array([-2, os-0.6, 0]))
        self.play(GrowArrow(arrow2))

        txt1 = TextMobject("The insurer received updated information")
        txt2 = TextMobject("in 2012, resulting in an increase")
        txt3 = TextMobject("in claims outstanding by \\$200.")

        txt_13 = VGroup(txt1, txt2, txt3)
        txt_13.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_13.move_to(np.array([-0.5, os-1.4, 0]))
        txt_13.scale(0.5)
        self.play(Write(txt_13))
        self.wait(3)

        for x, clm in zip(range(-1, 6), range(3, 10)):
            listx = []
            for i in (os, inc):
                if i == os:
                    txt = TextMobject(str(os_list[clm+1]))
                else:
                    txt = TextMobject( str(inc_list[clm+1]) )
                txt.move_to(np.array([x, i, 0]))
                txt.scale(0.7)
                listx.append(txt)
            claims2 = VGroup(*listx)
            self.play(FadeIn(claims2))
            self.wait()

        arrow3 = Arrow(UP, DOWN * 0.05)  # specify the location of the two ends.
        arrow3.move_to(np.array([5, os-0.6, 0]))
        self.play(GrowArrow(arrow3))

        txt1 = TextMobject("The outstanding claim reserve eventually")
        txt2 = TextMobject("reduces to zero, as the insurer has paid out")
        txt3 = TextMobject("fully and dont expect any more movement.")

        txt_19 = VGroup(txt1, txt2, txt3)
        txt_19.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_19.move_to(np.array([4.6, os - 1.4, 0]))
        txt_19.scale(0.5)
        self.play(Write(txt_19))
        self.wait(3)

        txt_dev_1 = TextMobject("The same steps can be repeated for other claims")
        txt_dev_2 = TextMobject("to eventually form an incurred claims triangle.")
        txt_dev1 = VGroup(txt_dev_1, txt_dev_2)
        txt_dev1.arrange(DOWN, center=False, aligned_edge=LEFT)
        txt_dev1.move_to(np.array([0, -3, 0]))
        txt_dev1.scale(1)
        self.play(FadeOut(arrow1), FadeOut(txt_09))
        self.play(ShowCreation(txt_dev1))
        self.wait(3)

class final_scene(Scene):
    def construct(self):
        grid = ScreenGrid(rows=16, columns=28)
        # self.add(grid)

        eqn1 = TexMobject(
            "{Ultimate} = \\lefteqn{\\underbrace{\\phantom{Paid + Outstanding}}_{Incurred}}Paid + \\overbrace{Outstanding + IBNR}^{Unpaid}",
        )

        eqn1.to_edge(DOWN)
        self.play(Write(eqn1))
        self.wait(15)


