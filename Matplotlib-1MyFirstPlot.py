####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

test_my_first_plot
Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.
Create an axis, associated with figure fig, using add_subplot. Name it as ax.
Create a list t with values [5, 10, 15, 20, 25].
Create a list d with values [25, 50, 75, 100, 125].
Draw a line, by plotting t values on X-Axis and d values on Y-Axis. Use the plot function. Label the line as d = 5t.
Label X-Axis as time (seconds).
Label Y-Axis as distance (meters).
Set Title as Time vs Distance Covered.
Limit data points on X-Axis from 0 to 30.
Limit data points on Y-Axis from 0 to 130.
Add a legend.
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['My_First_plot'],extensions=['png'])
def test_my_first_plot():
    
    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    t = [5, 10, 15, 20, 25]
    d = [25, 50, 75, 100, 125]
    plt.plot(t, d,label='d = 5t')
    ax.set_xlabel("time (seconds)"); ax.set_ylabel('distance (meters)')
    ax.set_xlim([0,30]); ax.set_ylim([0,130])
    plt.legend()
    
####
Creating the Plot
After completing function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.

The test run will create a plot in the result_images/test_plots folder. This cannot be viewed directly.
####

####
Viewing the Plot
To view the plot after the test run, click python3 ~/manage.py runserver 0.0.0.0:8000. This starts a web server.

To view the created plot, click the following link:

https://2886795292-8000-host09-fresco.environments.katacoda.com/myplots/1/
####

####
Submission
Press Ctrl+C in the terminal to stop the web server.
If the plot is not as per the expectation, make necessary changes in the test_my_first_plot function, and redo all the steps.
If everything is fine, click the 'Summary' button.
Note: If unable to submit, check if the images are created as expected under the path /home/scrapbook/tutorial/result_images/test_plots/.
####

