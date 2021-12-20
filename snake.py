from turtle import Turtle, Screen
import time

# Constant Starting positions:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # STEP 1: Create 3 segments that make up our snake body

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Extending the tail:
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # STEP 2: Moving the Snake
    def move(self):
        # Linking our 3 squares: we want the last square to take the position of the second last and so on.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    # Control speed:
    # def speed(self):
    #     screen = Screen()
    #     difficulty = screen.textinput(title="Difficulty", prompt="Choose a difficulty: 'Hard' || 'Easy ").lower()
    #     if difficulty == 'easy':
    #         return time.sleep(0.1)
    #     else:
    #         return time.sleep(0.05)
