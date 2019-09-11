####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

1. test_generate_figure1

Define a numpy array 't' with expression 'np.arange(0.0, 5.0, 0.01)'.

Define another numpy array 's1' with expression 'np.sin(2np.pit)'

Define one more numpy array 's2' with expression 'np.sin(4np.pit)'.

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axes, using plt.subplot function. Name it as axes1. The subplot must point to the first virtual grid created by 2 rows and 1 column. Set 'title' argument to 'Sin(2pix)'.

Draw a line plot of 't' and 's1' using the 'plot' function on 'axes1`.

Create another axes, using the plt.subplot function. Name it as axes2. The subplot must point to the second virtual grid created by 2 rows and 1 column. Set 'title' argument to 'Sin(4pix)'. Set 'sharex' argument to 'axes1' and 'sharey' argument to 'axes1'.

Draw a line plot of 't' and 's2' using the 'plot' function on 'axes2`.
####

####
2. test_generate_figure2

Set random seed to 1000 using the expression 'np.random.seed(1000)'.

Define a numpy array 'x' with expression 'np.random.rand(10)'.

Define another numpy array 'y' with expression 'np.random.rand(10)'.

Define one more numpy array 'z' with expression 'np.sqrt(x2 + y2)'.

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axes, using plt.subplot function. Name it as axes1. The subplot must point to the first virtual grid created by 2 rows and 2 columns. Set 'title' argument to 'Scatter plot with Upper Traingle Markers'.

Draw a scatter plot of 'x' and 'y' using 'scatter' function on 'axes1`. Set argument 's' to 80, 'c' to z and 'marker' to '^'.

Add ticks on X-Axis at 0.0, 0.4, 0.8, 1.2 and ticks on Y-Axis at -0.2, 0.2, 0.6, 1.0 respectively

Create an axes, using plt.subplot function. Name it as axes2. The subplot must point to the Second virtual grid created by 2 rows and 2 columns. Set 'title' argument to 'Scatter plot with Plus Markers'.

Draw a scatter plot of 'x' and 'y' using 'scatter' function on 'axes2`. Set argument 's' to 80, 'c' to 'z' and 'marker' to '+'.

CONTINcontinued...

Add ticks on X-Axis at 0.0, 0.4, 0.8, 1.2 and ticks on Y-Axis at -0.2, 0.2, 0.6, 1.0 respectively.

Create an axes, using plt.subplot function. Name it as axes3. The subplot must point to the Third virtual grid created by 2 rows and 2 columns. Set 'title' argument to 'Scatter plot with Circle Markers'.

Draw a scatter plot of 'x' and 'y' using 'scatter' function on 'axes3`. Set argument 's' to 80, 'c' to 'z' and 'marker' to 'o'.

Add ticks on X-Axis at 0.0, 0.4, 0.8, 1.2 and ticks on Y-Axis at -0.2, 0.2, 0.6, 1.0 respectively.

Create an axes, using plt.subplot function. Name it as axes4. The subplot must point to the Fourth virtual grid created by 2 rows and 2 columns. Set 'title' argument to 'Scatter plot with Diamond Markers'.

Draw a scatter plot of 'x' and 'y' using 'scatter' function on 'axes4`. Set argument 's' to 80, 'c' to 'z' and 'marker' to 'd'.

Add ticks on X-Axis at 0.0, 0.4, 0.8, 1.2 and ticks on Y-Axis at -0.2, 0.2, 0.6, 1.0 respectively

Adjust the entire layout with expression 'plt.tight_layout()'.
####

####
3. test_generate_figure3

Define a numpy array 'x' with expression 'np.arange(1, 101)'.

Define another numpy array 'y1' with expression 'y1 = x'.

Define another numpy array 'y2' with expression 'y1 = x**2'.

Define another numpy array 'y3' with expression 'y1 = x**3'.

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Define a grid 'g' of 2 rows and 2 columns, using 'GridSpec' function. Ensure that 'matplotlib.gridspec' is imported, before defining the grid.

Create an axes, using plt.subplot function. Name it as axes1. The subplot must span the 1st row and 1st column of the defined grid 'g'. Set 'title' argument to 'y = x'.

Draw a line plot of 'x' and 'y1' using 'plot' function on 'axes1`.

Create an axes, using plt.subplot function. Name it as axes2. The subplot must span 2nd row and 1st column of defined grid 'g'. Set 'title' argument to 'y = x**2'.

Draw a line plot of 'x' and 'y2' using 'plot' function on 'axes2`.

Create an axes, using plt.subplot function. Name it as axes3. The subplot must span all rows of 2nd column of defined grid 'g'. Set 'title' argument to 'y = x**3'.

Draw a line plot of 'x' and 'y3' using 'plot' function on 'axes3`.

Adjust the entire layout with the expression 'plt.tight_layout()'.
####

####
Creating the Plot
After completing function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.
The test run will create plots in the result_images/test_plots folder. These plots cannot be viewed directly.
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Multiple_Plots_Figure1'],extensions=['png'])
def test_generate_figure1():

    # Write your functionality below
    t = np.arange(0.0, 5.0, 0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)
    fig = plt.figure(figsize=(8,6))
    axes1 = plt.subplot(2,1,1, title='Sin(2pix)')
    axes1.plot(t,s1)
    axes2 = plt.subplot(2,1,2, title='Sin(4pix)', sharex=axes1, sharey=axes1)
    axes2.plot(t,s2)
    plt.show()


@image_comparison(baseline_images=['Multiple_Plots_Figure2'],extensions=['png'])
def test_generate_figure2():

    # Write your functionality below
    np.random.seed(1000)
    x = np.random.rand(10)
    y = np.random.rand(10)
    z = np.sqrt(x*2 + y*2)
    fig = plt.figure(figsize=(8,6))
    axes1 = plt.subplot(2,2,1, title = 'Scatter plot with Upper Traingle Markers')
    axes1.scatter(x,y, s = 80, c = z , marker = '^')
    axes1.set_xticks([0.0, 0.4, 0.8, 1.2])
    axes1.set_yticks([-0.2, 0.2, 0.6, 1.0])
    axes2 = plt.subplot(2,2,2, title = 'Scatter plot with Plus Markers')
    axes2.scatter(x,y, s = 80, c = z , marker = '+')
    axes2.set_xticks([0.0, 0.4, 0.8, 1.2])
    axes2.set_yticks([-0.2, 0.2, 0.6, 1.0])
    axes3 = plt.subplot(2,2,3, title = 'Scatter plot with Circle Markers')
    axes3.scatter(x,y, s = 80, c = z , marker = 'o')
    axes3.set_xticks([0.0, 0.4, 0.8, 1.2])
    axes3.set_yticks([-0.2, 0.2, 0.6, 1.0])
    axes3 = plt.subplot(2,2,3, title = 'Scatter plot with Diamond Markers')
    axes3.scatter(x,y, s = 80, c = z , marker = 'd')
    axes3.set_xticks([0.0, 0.4, 0.8, 1.2])
    axes3.set_yticks([-0.2, 0.2, 0.6, 1.0])
    plt.tight_layout()
    plt.show()

@image_comparison(baseline_images=['Multiple_Plots_Figure3'],extensions=['png'])
def test_generate_figure3():

    # Write your functionality below
    x = np.arange(1,101)
    y1 = x
    y2 = x**2
    y3 = x**3
    fig = plt.figure(figsize=(8,6))
    g = gridspec.GridSpec(2,2)
    axes1 = plt.subplot(g[1,1], title = 'y = x')
    axes1.plot(x, y1)
    axes2 = plt.subplot(g[2,1], title = 'y = x**2')
    axes2.plot(x, y2)
    axes3 = plt.subplot(g[:2], title = 'y = x**3')
    axes3.plot(x, y3)
    plt.tight_layout()
    plt.show()
