import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    line_style = input("Which kind of line style would you like ? -- or - ?")
    colour_style = input("Which kind of colour would you like ? r,g or b ?")
    marker_style = input(
        "Which kind of marker style would you like ? o, s or ^ ?")
    paths['line_style'] = line_style
    paths['colour'] = colour_style
    paths['marker_style'] = marker_style
    return paths


def generate():
    n = int(input("how many likes would you like to plot?"))
    for n in range(n):
        values = data()
        x = rnd.sample(range(1, 100), 5)
        y = rnd.sample(range(1, 100), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)

    plt.show


def run():
    print("running")
    generate()
    print("done")


run()
