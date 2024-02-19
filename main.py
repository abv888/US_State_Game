import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
screen.setup(width=725, height=491)
image = "resources/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()

data_frame = pd.read_csv("resources/50_states.csv")
states = data_frame.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States guessed",
        prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_series = data_frame[data_frame.state == answer_state]
        t.goto(int(answer_series.x), int(answer_series.y))
        t.write(answer_state)

screen.exitonclick()
