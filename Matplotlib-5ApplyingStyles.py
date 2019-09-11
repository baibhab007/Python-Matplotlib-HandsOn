####
Writing Functions
Complete the following function definitions, defined in Matsession/tests/test_plots.py, based on the instructions provided:

1. test_generate_plot_with_style1

Generate the following barplot with 'ggplot' style. Use 'with' to apply the style to the code generating the barplot.

Create a figure of size 8 inches in width, and 6 inches in height. Name it as fig.

Create an axis, associated with figure fig, using add_subplot. Name it as ax.

Define the following lists

​​​ sepal_len = [5.01, 5.94, 6.59]
​​​​​​sepal_wd = [3.42, 2.77, 2.97]
petal_len = [1.46, 4.26, 5.55]
petal_wd = [0.24, 1.33, 2.03]
species = ['setosa', 'versicolor', 'viriginica']
species_index1 = [0.7, 1.7, 2.7]
species_index2 = [0.9, 1.9, 2.9]
species_index3 = [1.1, 2.1, 3.1]
species_index4 = [1.3, 2.3, 3.3]
Draw vertical bars showing mean sepal length of a species. Set width of the bars as 0.2, and label it as Sepal Length. Use bar with species_index1 and sepal_len.

Draw vertical bars showing mean sepal length of a species. Set width of bars as 0.2 and label it as Sepal Width. Use bar with species_index2 and sepal_wd.

Draw vertical bars showing mean sepal length of a species. Set width of bars as 0.2 and label it as Petal Length. Use bar with species_index3 and petal_len.

Draw vertical bars showing mean sepal length of a species. Set width of bars as 0.2 and label it as Petal Width. Use bar with species_index4 and petal_wd.

Label X-Axis as Species.

Label Y-Axis as Iris Measurements (cm).
Set Title as Mean Measurements of Iris Species.
Limit X-Axis from 0.5 to 3.7.
Limit Y-Axis from 0 to 10.
Mark major ticks on X-Axis at 1.1, 2.1, and 3.1.
Label the major ticks on X-Axis as setosa, versicolor, and viriginica respectively.
Add a legend.
####

####
2. test_generate_plot_with_style2

Regenerate the barplot defined in 'generate_plot_with_style1' using 'seaborn-colorblind' style. Use 'with' for applying the style.
3. test_generate_plot_with_style3

Regenerate the barplot defined in 'generate_plot_with_style1' using 'grayscale' style. Use 'with' for applying the style.
####

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['Plot_with_Style1'],extensions=['png'])
def test_generate_plot_with_style1():

    # Write your functionality below
    with plt.style.context('ggplot'):
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
        ax.bar(species_index1,sepal_len, width='0.2',label='Sepal Length')
        ax.bar(species_index2,sepal_wd, width='0.2', label='Sepal Width')
        ax.bar(species_index3,petal_len, width='0.2', label='Petal Length')
        ax.bar(species_index4,petal_wd, width='0.2', label='Petal Width')
        plt.title('Mean Measurements of Iris Species')
        plt.xlabel('Species'); plt.ylabel('Iris Measurements (cm)')
        plt.xlim(0.5,3.7); plt.ylim(0,10)
        ax.set_xticks([1.1, 2.1, 3.1])
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()

@image_comparison(baseline_images=['Plot_with_Style2'],extensions=['png'])
def test_generate_plot_with_style2():

    # Write your functionality below
    with plt.style.context('seaborn-colorblind'):
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
        ax.bar(species_index1,sepal_len, width='0.2',label='Sepal Length')
        ax.bar(species_index2,sepal_wd, width='0.2', label='Sepal Width')
        ax.bar(species_index3,petal_len, width='0.2', label='Petal Length')
        ax.bar(species_index4,petal_wd, width='0.2', label='Petal Width')
        plt.title('Mean Measurements of Iris Species')
        plt.xlabel('Species'); plt.ylabel('Iris Measurements (cm)')
        plt.xlim(0.5,3.7); plt.ylim(0,10)
        ax.set_xticks([1.1, 2.1, 3.1])
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()


@image_comparison(baseline_images=['Plot_with_Style3'],extensions=['png'])
def test_generate_plot_with_style3():

    # Write your functionality below
    with plt.style.context('grayscale'):
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
        ax.bar(species_index1,sepal_len, width='0.2',label='Sepal Length')
        ax.bar(species_index2,sepal_wd, width='0.2', label='Sepal Width')
        ax.bar(species_index3,petal_len, width='0.2', label='Petal Length')
        ax.bar(species_index4,petal_wd, width='0.2', label='Petal Width')
        plt.title('Mean Measurements of Iris Species')
        plt.xlabel('Species'); plt.ylabel('Iris Measurements (cm)')
        plt.xlim(0.5,3.7); plt.ylim(0,10)
        ax.set_xticks([1.1, 2.1, 3.1])
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()

####
Creating the Plot
After completing the function definitions in test_plots.py, click cd ~/ && python3 -m pytest ~/Matsession/tests/test_plots.py.

The test run will create plots in the result_images/test_plots folder. These plots cannot be viewed directly.
####

####
Viewing the Plot
To view the plots after the test run, click python3 ~/manage.py runserver 0.0.0.0:8000. This starts a web server.
To view the created plot corresponding to the first defined function, access the URL:
https://2886795463-8000-host09-fresco.environments.katacoda.com/myplots/1/

To view the plot corresponding to the second defined function, access the URL:
https://2886795463-8000-host09-fresco.environments.katacoda.com/myplots/2/

To view the plot corresponding to the third defined function, access the URL:
https://2886795463-8000-host09-fresco.environments.katacoda.com/myplots/3/
####

####
Submission
Press Ctrl+C in the terminal to stop the web server.
Ensure 3 tests are passed while testing. If any test fails, make necessary changes in the corresponding function, and redo all the steps.
Once all 3 tests are passed, click the 'Summary' button. Note: If unable to submit, check if the images are created as expected under the path /home/scrapbook/tutorial/result_images/test_plots/.
####
