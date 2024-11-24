import numpy as np
import matplotlib.pyplot as plt

class FunctionPlotter:
    """
    A class for plotting mathematical functions with interactive coordinate display.

    Attributes:
        func (callable): The mathematical function to plot.
        x_range (tuple): The range of x values as (min, max).
        num_points (int): Number of points to generate for the plot.
        title (str): The title of the plot.
        save_as (str): File name to save the plot as an image.
    """

    def __init__(self, func, x_range=(-10, 10), num_points=1000, title=None, save_as=None):
        """
        Initializes the FunctionPlotter instance.

        @param func: callable
            The mathematical function to be plotted (e.g., np.sin, np.exp).
        @param x_range: tuple, optional
            The range of x values for the plot, specified as (min, max). Default is (-10, 10).
        @param num_points: int, optional
            The number of points to generate in the x range. Default is 1000.
        @param title: str, optional
            Title of the plot. Default is the function's name.
        @param save_as: str, optional
            File name for saving the plot. If None, the plot will not be saved.
        """
        self.func = func
        self.x_range = x_range
        self.num_points = num_points
        self.title = title or f"Plot of {func.__name__}"
        self.save_as = save_as

    def generate_points(self):
        """
        Generates x and y points for the given function over the specified range.

        @return: tuple
            A tuple containing arrays of x and y points.
        @raise ValueError:
            If the function cannot be evaluated for the generated x points.
        """
        try:
            x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
            y = self.func(x)
            return x, y
        except Exception as e:
            raise ValueError(f"Error in processing the function: {e}")

    def plot(self):
        """
        Creates an interactive plot of the function, with coordinates displayed on mouse hover.

        @raise ValueError:
            If an error occurs while generating points or plotting.
        """
        try:
            x, y = self.generate_points()

            # Create the plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, label=f"{self.func.__name__}(x)", color="blue", linewidth=2)
            ax.axhline(0, color='black', linewidth=1, linestyle="--", alpha=0.7)
            ax.axvline(0, color='black', linewidth=1, linestyle="--", alpha=0.7)
            ax.set_title("Math Plotter", fontsize=14, fontweight="bold")  # تغییر به نام پکیج شما
            ax.set_xlabel("x", fontsize=12)
            ax.set_ylabel("f(x)", fontsize=12)
            ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
            ax.legend(fontsize=12, loc="best")

            # # Interactive coordinate display
            def on_move(event):
                if event.inaxes:
                    xcoord = event.xdata
                    ycoord = event.ydata
                    ax.set_title(f"Coordinates: x={xcoord:.2f}, y={ycoord:.2f}", fontsize=14, fontweight="bold")
                    fig.canvas.draw()

            # Connect the event to the plot
            fig.canvas.mpl_connect('motion_notify_event', on_move)

            # Show or save the plot
            if self.save_as:
                plt.savefig(self.save_as, dpi=300)
                print(f"Plot saved as '{self.save_as}'.")
            else:
                plt.show()

        except ValueError as e:
            print(e)


# Example mathematical functions
def quadratic_function(x):
    """
    Example of a quadratic function.

    @param x: array-like
        Input values.
    @return: array-like
        Output values of the quadratic function.
    """
    return -x


def sine_function(x):
    """
    Example of a sine function.

    @param x: array-like
        Input values.
    @return: array-like
        Output values of the sine function.
    """
    return np.sin(x)


def exponential_function(x):
    """
    Example of an exponential function.

    @param x: array-like
        Input values.
    @return: array-like
        Output values of the exponential function.
    """
    return np.exp(x)


# Main execution
if __name__ == "__main__":
    # Plot an example function
    FunctionPlotter(quadratic_function, x_range=(-1, 1), title="Math Plotter").plot()
