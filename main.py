import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    player = Player()
    car_manager = CarManager()
    score_board = Scoreboard()

    screen.onkeypress(player.move_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        if player.is_reached_end():
            player.go_to_start_position()
            car_manager.level_up()
            score_board.increase_level()
            score_board.update_level()

        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                score_board.game_over()
                game_is_on = False

    screen.exitonclick()
    print(len(car_manager.all_cars))
