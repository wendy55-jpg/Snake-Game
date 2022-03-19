from turtle import Turtle
SEGMENT_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in SEGMENT_POSITION:
           self.add_seg(position)

    def add_seg(self, position):
        new_seg = Turtle("square")
        new_seg.color("cyan")
        new_seg.penup()
        new_seg.goto(position)
        self.segment.append(new_seg)

    def extend_tail(self):
        self.add_seg(self.segment[-1].position())

    def move(self):
        for segs in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segs - 1].xcor()
            new_y = self.segment[segs - 1].ycor()
            self.segment[segs].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)