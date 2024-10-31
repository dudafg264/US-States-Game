import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
right = 0
states = turtle.Turtle()
states.hideturtle()
states.penup()

data_states = pandas.read_csv("50_states.csv")

game_is_on = True
while game_is_on == True:

    if right == 60:
        turtle.write("You already got the 60 states!", align="center", font=("Arial", 16, "normal"))
        break

    turtle.clear()
    answer_state = screen.textinput(title=f"Guess the State {right}/60", prompt="What is another state's name?")
    real_answer = answer_state.title()

    if answer_state is None:
        break

    elif real_answer in data_states.state.values:
        turtle.write(f"Right! {real_answer} is a state.", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)

        state_data = data_states[data_states.state == real_answer]
        x = int(state_data.x.values[0])
        y = int(state_data.y.values[0])
        right += 1
        states.goto(x, y)
        states.write(real_answer,  font=("Arial", 10, "normal"))

    else:
        turtle.write("Try again!", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)



turtle.mainloop()