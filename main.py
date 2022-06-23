import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# print(answer_state)

# with open("50_states.csv") as states:
#     print(states)

US_states = pandas.read_csv("50_states.csv")
# print(US_states)

all_states = US_states.state.to_list()

done_states = []
action = True

while action:
    answer_state = (screen.textinput(title=f"{len(done_states)}/50 states Correctly", prompt="What's another state's name?")).title()

    if answer_state == "Exit":

        # missing_states = []
        # for states in all_states:
        #     if states not in done_states:
        #         missing_states.append(states)

        missing_states = [states for states in all_states if states not in done_states]
        unknown_states = pandas.DataFrame(missing_states)
        unknown_states.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in done_states:
            done_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = US_states[US_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item())
        # print(done_states)

        if len(done_states) == len(all_states):
            action = False








