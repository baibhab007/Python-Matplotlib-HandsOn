####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

1 test_sine_wave_plot

Create a figure of size 12 inches in width, and 3 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Create a numpy array t with 200 values between 0.0 and 2.0. Use the 'linspace' method to generate 200 values.

Create a numpy array v, such that v = np.sin(2.5*np.pi*t).

Pass t and v as variables to plot function and draw a red line passing through the selected 200 points. Label the line as sin(t).

Label X-Axis as Time (seconds).

Label Y-Axis as Voltage (mV).

Set Title as Sine Wave.

Limit data on X-Axis from 0 to 2.

Limit data on Y-Axis from -1 to 1.

Mark major ticks on X-Axis at 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, and 2.0.

Mark major ticks on Y-Axis at -1, 0, and 1.

Add a grid, whose linestyle is '--'.

Add a legend.

####



####
2 test_multi_curve_plot

Create a figure of size 12 inches in width, and 3 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Create a numpy array x with 20 values between 0.0 and 5.0. Use the 'linspace' method to generate 20 values.

Create three numpy arrays y1, y2 and y3, using the expressions y1 = x, y2 = x**2 and y3 = x**3 respectively.

Draw a red colored line passing through x and y1, using the plot function. Mark the 20 data points on the line as circles. Label the line as y = x.

Draw a green colored line passing through x and y2, using the plot function. Mark the 20 data points on the line as squares. Label the line as y = x**2.

Draw a blue colored line passing through x and y3, using the plot function. Mark the 20 data points on the line as upward pointed triangles.

Label the line as y = x**3.

Label X-Axis as X.

Label Y-Axis as f(X).

Set Title as Linear, Quadratic, & Cubic Equations.

Add a legend.
####


####
3 test_scatter_plot

Create a figure of size 12 inches in width, and 3 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Consider the list s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]. It represents the number of cars sold by a Company 'X' in each month of 2017, starting from Jan, 2017.

Create a list months containing numbers from 1 to 12.

Draw a scatter plot with variables months and s as arguments. Mark the data points in red color. Use the scatter function for plotting.

Limit data on X-Axis from 0 to 13.

Limit data on Y-Axis from 20 to 100.

Mark ticks on X-Axis at 1, 3, 5, 7, 9, and 11.

Label the X-Axis ticks as Jan, Mar, May, Jul, Sep, and Nov respectively.

Label X-Axis as Months

Label Y-Axis as No. of Cars Sold

Set Title as "Cars Sold by Company 'X' in 2017".
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Sine_Wave_Plot'],extensions=['png'])
def test_sine_wave_plot():

    # Write your functionality below
    fig = plt.figure(figsize=(12,3))
    ax = fig.add_subplot(111)
    t = np.linspace(0.0,2.0,200)
    v = np.sin(2.5*np.pi*t)
    plt.plot(t,v,label='sin(t)', color='red')
    plt.title('Sine Wave')
    plt.xlabel('Time (seconds)'); plt.ylabel('Voltage (mV)')
    plt.xlim(0,2); plt.ylim(-1,1)
    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    plt.yticks([-1, 0, 1])
    ax.grid(linestyle='--')
    ax.legend()
    

@image_comparison(baseline_images=['Multi_Curve_Plot'],extensions=['png'])
def test_multi_curve_plot():

    # Write your functionality below
    fig = plt.figure(figsize=(12,3))
    ax = fig.add_subplot(111)
    x = np.linspace(0.0,5.0,20)
    y1 = x
    y2 = x**2
    y3 = x**3
    plt.plot(x,y1,label='y = x', color='red',marker='o')
    plt.plot(x,y2,label='y = x**2', color='green',marker='s')
    plt.plot(x,y3,label='y = x**3', color='blue',marker='^')
    plt.title('Linear, Quadratic, & Cubic Equations')
    plt.xlabel('X'); plt.ylabel('f(X)')
    ax.legend()


@image_comparison(baseline_images=['Scatter_Plot'],extensions=['png'])
def test_scatter_plot():

    # Write your functionality below
    fig = plt.figure(figsize=(12,3))
    ax = fig.add_subplot(111)
    s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    plt.scatter(s,months,color='red')
    plt.xlabel('Months'); plt.ylabel('No. of Cars Sold')
    plt.xlim(0,13); plt.ylim(20,100)
    ax.set_xticks([1, 3, 5, 7, 9, 11])
    ax.set_xticklabels(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'])
    plt.title("Cars Sold by Company 'X' in 2017")



####
Creating the Plot
After completing function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.

The test run will create plots in the result_images/test_plots folder. These plots cannot be viewed directly.
####

####
Viewing the Plot
To view the plots after the test run, click python3 ~/manage.py runserver 0.0.0.0:8000. This starts a web server.

To view the created plot corresponding to the first defined function, access the URL:

https://2886795289-8000-host09-fresco.environments.katacoda.com/myplots/1/

To view the plot corresponding to the second defined function, access the URL:
https://2886795289-8000-host09-fresco.environments.katacoda.com/myplots/2/

To view the plot corresponding to the third defined function, access the URL:
https://2886795289-8000-host09-fresco.environments.katacoda.com/myplots/3/
####

####
Submission
Press Ctrl+C in the terminal to stop the web server.

Ensure that 3 tests are passed while testing. If any test fails, make necessary changes in the corresponding function, and redo all the steps.

Once all 3 tests are passed, click the 'Summary' button.

Note: If unable to submit, check if the images are created as expected under the path /home/scrapbook/tutorial/result_images/test_plots/.
####
