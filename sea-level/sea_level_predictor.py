from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    print(df.head())
    # Create scatter plot

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_plot_1= np.arange(x[0],2050)
    plt.plot(x_plot_1, res.intercept + res.slope*x_plot_1,label='Normal')
    
    # Create second line of best fit
    dfaux = df[df['Year'] >= 2000]
    xaux = dfaux['Year']
    yaux = dfaux['CSIRO Adjusted Sea Level']
    res2 = linregress(xaux, yaux)
    x_plot_2 = np.arange(2000,2050)
    plt.plot(x_plot_2, res2.intercept + res2.slope*x_plot_2,label='Since 2000')
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend()
    
    # To load the display window
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()