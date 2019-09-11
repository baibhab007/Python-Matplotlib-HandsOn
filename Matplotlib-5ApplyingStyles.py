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

