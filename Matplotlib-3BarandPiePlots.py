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

