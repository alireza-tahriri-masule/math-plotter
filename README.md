# **Math Plotter Documentation** 📊  

Math Plotter is a Python package designed to make mathematical function visualization simple, interactive, and effective. It supports dynamic coordinate display, allows customization, and can save high-quality images for reports or presentations.  

---

## **Features**  

- **Plot Mathematical Functions**: Supports any function defined in Python (e.g., trigonometric, exponential, or user-defined).  
- **Interactive Visualization**: Hover over the graph to display precise `x` and `y` coordinates dynamically.  
- **Customizable**: Define the function, set the range, adjust the resolution, and more.  
- **Export Plots**: Save your graphs as high-quality image files.  

---

## **Installation**  

1. Ensure Python 3.x is installed on your system.  
2. Install required dependencies using pip:  
   ```bash
   pip install numpy matplotlib
   ```  

---

## **How to Use Math Plotter**  

### **Initialization**  
The `FunctionPlotter` class allows you to define and plot mathematical functions. Here are the key parameters you can use:  

| **Parameter**   | **Type**   | **Description**                                           | **Default**       |  
|------------------|------------|-----------------------------------------------------------|-------------------|  
| `func`           | `callable` | The function to plot (e.g., `np.sin`, `np.exp`).          | Required          |  
| `x_range`        | `tuple`    | The range of x values as `(min, max)`.                   | `(-10, 10)`       |  
| `num_points`     | `int`      | Number of points to generate for the plot.               | `1000`            |  
| `title`          | `str`      | Title of the plot. Defaults to the function's name.      | `"Plot of func"`  |  
| `save_as`        | `str`      | File name to save the plot (optional).                   | `None`            |  

---

### **Running the Script**  
1. Save the code in a file named `main.py`.  
2. Open a terminal or command prompt and execute the following command:  
   ```bash
   python main.py
   ```  
   This will display an interactive plot. If `save_as` is specified, the plot will also be saved as an image.  

---

## **Example Usage**  

### **1. Plot a Quadratic Function**  
```python
from math_plotter import FunctionPlotter

# Define a quadratic function
def quadratic(x):
    return x**2

# Create and display the plot
FunctionPlotter(
    func=quadratic,
    x_range=(-10, 10),
    title="Quadratic Function"
).plot()
```  

### **2. Plot a Sine Wave**  
```python
import numpy as np
from math_plotter import FunctionPlotter

# Define a sine wave
def sine_wave(x):
    return np.sin(x)

# Plot and save the sine wave
FunctionPlotter(
    func=sine_wave,
    x_range=(-2 * np.pi, 2 * np.pi),
    title="Sine Wave",
    save_as="sine_wave.png"
).plot()
```  

### **3. Plot an Exponential Function**  
```python
import numpy as np
from math_plotter import FunctionPlotter

# Define an exponential function
def exponential(x):
    return np.exp(x)

# Display the exponential plot
FunctionPlotter(
    func=exponential,
    x_range=(-2, 2),
    title="Exponential Growth"
).plot()
```  

---

## **Understanding the Code**  

### **Key Method: `plot`**  

The `plot` method combines data generation and visualization while adding interactivity.  

1. **Data Generation**:  
   The `generate_points` method computes `x` and `y` values using the function and range:  
   ```python
   def generate_points(self):
       x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
       y = self.func(x)
       return x, y
   ```  

2. **Interactive Plotting**:  
   The `plot` method dynamically updates the plot title to display `x` and `y` coordinates based on mouse position:  
   ```python
   def on_move(event):
       if event.inaxes:
           xcoord = event.xdata
           ycoord = event.ydata
           ax.set_title(f"Coordinates: x={xcoord:.2f}, y={ycoord:.2f}")
           fig.canvas.draw()
   fig.canvas.mpl_connect('motion_notify_event', on_move)
   ```  

3. **Saving the Plot**:  
   The `save_as` parameter allows exporting plots as images:  
   ```python
   if self.save_as:
       plt.savefig(self.save_as, dpi=300)
       print(f"Plot saved as '{self.save_as}'.")
   ```  

---

## **Sample Output**  

When running the sine function example, you’ll see a graph displaying the sine wave.  

### Interactive Plot  
- **Hover**: Displays `x` and `y` coordinates in the title bar.  
- **Save**: Automatically saves the plot if a file name is provided.  

Example saved output:  
![Sine Wave Example](https://via.placeholder.com/800x400)  

---

## **Contributing**  

We welcome contributions to enhance Math Plotter!  

### Steps to Contribute:  
1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Test your changes thoroughly.  
4. Submit a pull request with a detailed explanation of your modifications.  

---

## **License**  

Math Plotter is licensed under the **MIT License**, making it open for use, modification, and distribution.  

---

## **Contact**  

For questions, suggestions, or feedback, feel free to reach out:  
- **Name**: Alireza Tahriri Masuleh  
- **Email**: [alirezatahriri4@gmail.com](mailto:alirezatahriri4@gmail.com)  

Happy plotting! 🎉  