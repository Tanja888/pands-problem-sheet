# Weekly Task 08 - Displays a plot of the functions:
# f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0,4] on one set of axes
# Author: Tanja Juric

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Changed the font for all the elements
# rcParams - stands for runtime configuration to apply to all plot elements
plt.rcParams['font.family'] = 'monospace' 

fig, ax = plt.subplots() #Had to put this to adjust the subplots 

x = np.array(range(0,5)) 
g = x * x
h = x ** 3

# First I did the legend but realized that the labels for each line looked nicer
plt.plot(x, x, color = 'purple')
plt.plot(x, g, color = 'green')
plt.plot(x, h, color = 'orange', linestyle = 'dashed', linewidth = 1.5)

#plt.plot(x, x, label = "x", color = "purple")
#plt.plot(x, g, label = "xsquared", color = "green")
#plt.plot(x, h, label ="xcubed", color = "orange", linestyle = "dashed", linewidth = 1.5)

plt.xlabel('X values', fontsize=8)
plt.ylabel('Results', fontsize=8)
plt.title('Functions plot', fontsize=10)
#plt.legend()

# Wanted to remove the right and top spine
ax.spines['right'].set_visible(False)    
ax.spines['top'].set_visible(False)
ax.text(x=3.24, y=54.6, s='xcubed', color='orange')
ax.text(x=3.3, y=15.8, s='xsquared', color='green')
ax.text(x=3.8, y=5.2, s='x', color='purple')

plt.subplots_adjust(left=0.1, bottom=0.2, right=None, top=None, wspace=None, hspace=None)

# Tried to change the ticks but then the x and y values were not displaying on coordinate formatter
# So, I added ax.format_coord()
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['0', '1', '2', '3', '4'], fontsize=8)
ax.set_yticks([0, 20, 40, 60])
ax.set_yticklabels(['', '20', '40', '60']) #Nicer to have only one 0 displayed and less stuff in general
ax.format_coord = lambda x, y: 'x={:g}, y={:g}'.format(x, y)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# To move 0 to the bottom of the axes
plt.xlim(xmin=0.0)
plt.ylim(ymin=0.0)

plt.show()

# Little bit on plotting:
# URL https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Wanted to remove outside borders aka spines:
# URL https://stackoverflow.com/questions/22082111/how-to-despine-a-matplotlib-and-seaborn-axes
# Was annoyed with x label not showing properly so I used subplot adjust; it got 'clipped':
# URL https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
# URL https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html
# Adding labels to the lines and changing the ticks:
# https://towardsdatascience.com/a-beginners-guide-to-plotting-fivethrityeight-like-visualizations-5b63d3f3ddd0
# On fontsize of ticks:
# URL https://stackoverflow.com/questions/6390393/matplotlib-make-tick-labels-font-size-smaller
# To move a title:
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html
# To move 0 to the start of the axes:
# URL https://stackoverflow.com/questions/44395838/how-to-make-0-0-on-matplotlib-graph-on-the-bottom-left-corner
# Coordinate formatter:
# URL https://stackoverflow.com/questions/65180000/matplotlib-mouse-cursor-coordinates-not-shown-for-empty-tick-labels
# To change the font for everything:
# URL https://www.statology.org/matplotlib-change-font/
# Officially fell into a rabbit hole with this task



