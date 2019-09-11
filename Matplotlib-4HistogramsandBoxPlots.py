####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

1. test_hist_of_a_sample_normal_distribution

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Set random seed to 100 using the expression np.random.seed(100).

Create a normal distribution x1 of 1000 values, with mean 25 and standard deviation 3.0. Use np.random.randn.

Draw a histogram of x1 with 30 bins. Use the hist function.

Label X-Axis as X1

Label Y-Axis as Bin Count

Set Title as Histogram of a Single Dataset.
####

####
2. test_boxplot_of_four_normal_distribution

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Set random seed to 100 using the expression np.random.seed(100).

Create a normal distribution x1 of 1000 values, with mean 25 and standard deviation 3.0. Use np.random.randn.

Create a normal distribution x2 of 1000 values, with mean 35 and standard deviation 5.0. Use np.random.randn.

Create a normal distribution x3 of 1000 values, with mean 55 and standard deviation 10.0. Use np.random.randn.

Create a normal distribution x4 of 1000 values, with mean 45 and standard deviation 3.0. Use np.random.randn.

Create a list labels with elements ['X1', 'X2', 'X3', 'X4].

Draw a Boxplot x1, x2, x3, x4 with notches and label it using the labels list. Use the boxplot function.

Choose + symbol for outlier, and fill color inside boxes by setting patch_artist argument to True.

Label X-Axis as Dataset

Label Y-Axis as Value

Set Title as Box plot of Multiple Datasets.
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Histogram'],extensions=['png'])
def test_hist_of_a_sample_normal_distribution():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1 = 25 + 3.0*np.random.randn(1000)
    ax.hist(x1, bins=30)
    plt.xlabel('X1'); plt.ylabel('Bin Count')
    plt.title('Histogram of a Single Dataset')
    plt.show()

@image_comparison(baseline_images=['Boxplot'],extensions=['png'])
def test_boxplot_of_four_normal_distribution():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1 = 25 + 3.0*np.random.randn(1000)
    x2 = 35 + 5.0*np.random.randn(1000)
    x3 = 55 + 10.0*np.random.randn(1000)
    x4 = 45 + 3.0*np.random.randn(1000)
    ax.boxplot([x1, x2, x3, x4], labels = ['X1', 'X2', 'X3', 'X4'], notch=True, patch_artist=True)
    plt.xlabel('Dataset'); plt.ylabel('Value')
    plt.title('Box plot of Multiple Datasets')
    plt.show()


####
Creating the Plot
After completing function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.
The test run will create a plot in the result_images/test_plots folder. This cannot be viewed directly.
####
Viewing the Plot
For viewing your plots after the test run, initially click on python3 ~/manage.py runserver 0.0.0.0:8000. This starts a webserver.

Now, in order to view the created plot corresponding to first defined function, access the URL :

https://2886795459-8000-host09-fresco.environments.katacoda.com/myplots/1/

Similarly, to view the plot corresponding to second defined function, access the URL :
https://2886795459-8000-host09-fresco.environments.katacoda.com/myplots/2/

To view the plot after the test run, click python3 ~/manage.py runserver 0.0.0.0:8000. This starts a web server.
To view the created plot, corresponding to the first defined function, access the URL: https://2886795459-8000-host09-fresco.environments.katacoda.com/myplots/1/
To view the plot corresponding to the second defined function, access the URL: https://2886795459-8000-host09-fresco.environments.katacoda.com/myplots/2/                                    

####
Submission
Press Ctrl+C in the terminal to stop the web server.
Ensure 2 tests are passed while testing. If any test fails, make necessary changes in the test_my_first_plot function, and redo all the steps.
Once all tests are passed, click the 'Summary' button.
Note: If unable to submit, check if the images are created as expected under the path /home/scrapbook/tutorial/result_images/test_plots/.
####
