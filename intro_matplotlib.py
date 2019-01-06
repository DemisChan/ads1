"""A set of exercises with matplotlib"""


def draw_co2_plot():
    """
    Here is some chemistry data

      Time (decade): 0, 1, 2, 3, 4, 5, 6
      CO2-concentration (ppm): 250, 265, 272, 260, 300, 320, 389

    Create a line graph of CO2 versus time, the line should be a blue dashed
    line. Add a title and axis titles to the plot.
    """

    import matplotlib.pyplot as plt
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [250, 265, 272, 260, 300, 320, 389]
    plt.plot(x, y, '--', color='blue')
    plt.title('Chemistry Data')
    plt.xlabel('Time (decade)', fontsize=14)
    plt.ylabel('CO2 concentration (ppm)', fontsize=14)
    plt.show()


def draw_equations_plot():
    """
    Plot the following lines on the same plot

      y=cos(x) coloured in red with dashed lines
      y=x^2 coloured in blue with linewidth 3
      y=exp(-x^2) coloured in black

    Add a legend, title for the x-axis and a title to the curve, the x-axis
    should range from -4 to 4 (with 50 points) and the y axis should range
    from 0 to 2. The figure should have a size of 8x6 inches.
    """

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-4, 4, 50)
    plt.figure(figsize=(8, 6))
    plt.plot(x, np.cos(x), '--', color='red', label='cos(x)')
    plt.plot(x, x**2, color='blue', linewidth=3, label='x^2')
    plt.plot(x, np.exp(-x**2), color='black', label='exp(-x^2)')
    plt.subplot().set_xlim(-4, 4)
    plt.subplot().set_ylim(0, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.yticks([0.25, 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2.])
    plt.legend()
    plt.show()


