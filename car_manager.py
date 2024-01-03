from turtle import Turtle
import random as rand
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = rand.randint(1, 6)
        if random_chance == 1:
            new_square = Turtle()
            new_square.shape("square")
            new_square.color(rand.choice(COLORS))
            new_square.turtlesize(1, 2)
            new_square.penup()
            new_square.goto(305, rand.randint(-250, 250))
            self.all_cars.append(new_square)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
