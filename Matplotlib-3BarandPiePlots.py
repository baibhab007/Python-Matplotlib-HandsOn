####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

1. test_barplot_of_iris_sepal_length

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Define a list species, with elements ['setosa', 'versicolor', 'viriginica'].

Define a list index, with values [0.2, 1.2, 2.2].

Define another list sepal_len with values [5.01, 5.94, 6.59]. These values represent the mean sepal length of iris flowers belonging to three species.

Draw a bar plot using the bar function, such that the height of each vertical bar displays the sepal length of a species.

Use index and sepal_len as variables. Set bar width as 0.5, color as red, and border color of the bar as black.

Label X-Axis as Species.

Label Y-Axis as Sepal Length (cm).

Set Title as Mean Sepal Length of Iris Species.

Limit X-Axis from 0 to 3.

Limit Y-Axis from 0 to 7.

Set ticks on X-Axis at 0.45, 1.45, and 2.45.

Set X-Axis tick labels to ['setosa', 'versicolor', 'viriginica']
####

####
2. test_barplot_of_iris_measurements

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.
Create an axis, associated with figure fig, using add_subplot. Name it as ax.
Define the following lists:
sepal_len = [5.01, 5.94, 6.59]
sepal_wd = [3.42, 2.77, 2.97]
petal_len = [1.46, 4.26, 5.55]
petal_wd = [0.24, 1.33, 2.03]
species = ['setosa', 'versicolor', 'viriginica']
species_index1 = [0.7, 1.7, 2.7]
species_index2 = [0.9, 1.9, 2.9]
species_index3 = [1.1, 2.1, 3.1]
species_index4 = [1.3, 2.3, 3.3]
Draw vertical bars showing the mean sepal length of a species. Set the color of the bars to c, boundary line color to black, width of bars as 0.2, and label it as Sepal Length. Use bar with species_index1 and sepal_len.
Draw vertical bars showing mean sepal length of a species. Set the color of the bars to m, boundary line color to black, width of bars as 0.2, and label it as Sepal Width. Use bar with species_index2 and sepal_wd.
Draw vertical bars showing mean sepal length of a species. Set the color of the bars to y, boundary line color to black, width of bars as 0.2, and label it as Petal Length. Use bar with species_index3 and petal_len.
Draw vertical bars showing mean sepal length of a species. Set the color of the bars to orange, boundary line color to black, width of bars as 0.2, and label it as Petal Width. Use bar with species_index4 and petal_wd.
Label X-Axis as Species.
Label Y-Axis as Iris Measurements (cm).
Set Title as Mean Measurements of Iris Species.
Limit X-Axis from 0.5 to 3.7 .
Limit Y-Axis from 0 to 10.
Mark major ticks on X-Axis at 1.1, 2.1, and 3.1.
Label the major ticks on X-Axis as setosa, versicolor and viriginica respectively.
Add a legend.
####

####
3. test_hbarplot_of_iris_petal_length

Create a figure of size 12 inches in width, and 5 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Define a list species, with elements ['setosa', 'versicolor', 'viriginica'].

Define a list index, with values [0.2, 1.2, 2.2].

Define another list petal_len with values [1.46, 4.26, 5.55]. These values represent the mean petal length of iris flowers belonging to three species.

Draw a horizontal bar plot using bar function, such that the width of each bar display the petal length of a species.

Use index and petal_len as variables. Set bar height as 0.5, color as c, and border color of the bar as black.

Label Y-Axis as Species

Label X-Axis as `Petal Length (cm).

Set Title as Mean Petal Length of Iris Species.

Mark major ticks on Y-Axis at 0.45, 1.45, and 2.45.

Label the major ticks on Y-Axis as setosa, versicolor and viriginica respectively.
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Iris_Sepal_Length_BarPlot'],extensions=['png'])
def test_barplot_of_iris_sepal_length():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    species = ['setosa', 'versicolor', 'viriginica']
    index = [0.2, 1.2, 2.2]
    sepal_len = [5.01, 5.94, 6.59]
    ax.bar(index,sepal_len, color='red', width=0.5, edgecolor = 'black')
    plt.title('Mean Sepal Length of Iris Species')
    plt.xlabel('Species'); plt.ylabel('Sepal Length (cm)')
    plt.xlim(0,3); plt.ylim(0,7)
    ax.set_xticks([0.45, 1.45, 2.45])
    ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
    plt.show()

@image_comparison(baseline_images=['Iris_Measurements_BarPlot'],extensions=['png'])
def test_barplot_of_iris_measurements():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    sepal_len = [5.01, 5.94, 6.59]
    sepal_wd = [3.42, 2.77, 2.97]
    petal_len = [1.46, 4.26, 5.55]
    petal_wd = [0.24, 1.33, 2.03]
    species = ['setosa', 'versicolor', 'viriginica']
    species_index1 = [0.7, 1.7, 2.7]
    species_index2 = [0.9, 1.9, 2.9]
    species_index3 = [1.1, 2.1, 3.1]
    species_index4 = [1.3, 2.3, 3.3]
    ax.bar(species_index1,sepal_len, color='c', width=0.2, edgecolor = 'black', label='Sepal Length')
    ax.bar(species_index2,sepal_wd, color='m', width=0.2, edgecolor = 'black', label='Sepal Width')
    ax.bar(species_index3,petal_len, color='y', width=0.2, edgecolor = 'black', label='Petal Length')
    ax.bar(species_index4,petal_wd, color='orange', width=0.2, edgecolor = 'black', label='Petal Width')
    plt.title('Mean Measurements of Iris Species')
    plt.xlabel('Species'); plt.ylabel('Iris Measurements (cm)')
    plt.xlim(0.5,3.7); plt.ylim(0,10)
    ax.set_xticks([1.1, 2.1, 3.1])
    ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
    ax.legend()
    plt.show()

@image_comparison(baseline_images=['Iris_Petal_Length_BarPlot'],extensions=['png'])
def test_hbarplot_of_iris_petal_length():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    species = ['setosa', 'versicolor', 'viriginica']
    index = [0.2, 1.2, 2.2]
    petal_len = [1.46, 4.26, 5.55]
    ax.barh(index,petal_len, color='c', height=0.5, edgecolor = 'black')
    plt.title('Mean Petal Length of Iris Species')
    plt.xlabel('Petal Length (cm)'); plt.ylabel('Species')
    ax.set_yticks([0.45, 1.45, 2.45])
    ax.set_yticklabels(['setosa', 'versicolor', 'viriginica'])
    plt.show()
    
####
Creating the Plot
After completing function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.

The test run will create plots in the result_images/test_plots folder. These plots cannot be viewed directly.
####

####
Viewing the Plot
To view the plots after the test run, click python3 ~/manage.py runserver 0.0.0.0:8000. This starts a web server.

To view the created plot corresponding to the first defined function, access the URL:

https://2886795269-8000-host09-fresco.environments.katacoda.com/myplots/1/

To view the plot corresponding to the second defined function, access the URL:
https://2886795269-8000-host09-fresco.environments.katacoda.com/myplots/2/

To view the plot corresponding to the third defined function, access the URL:
https://2886795269-8000-host09-fresco.environments.katacoda.com/myplots/3/
####

####
Submission
Press Ctrl+C in the terminal to stop the web server.

Ensure 3 tests are passed while testing. If any test fails, make necessary changes in the corresponding function, and redo all the steps.

Once all 3 tests are passed, click the 'Summary' button.

Note: If unable to submit, check if the images are created as expected under the path /home/scrapbook/tutorial/result_images/test_plots/
####
