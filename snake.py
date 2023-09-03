from turtle import Turtle

position_1 = [(0, 0), (-20, 0), (-40, 0)]
Move_distance = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in position_1:  # Loop through the positions
            self.increase_body(position)

    def increase_body(self, position):
        body_part = Turtle("square")
        body_part.penup()
        body_part.color("pink")
        body_part.goto(position)  # Set the snake's initial position
        self.body.append(body_part)

    def extend(self):
        self.increase_body(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def up(self):
        if self.head.heading() != 270:  # Prevent going directly back into itself
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
