import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.show()
    # Create first line of best fit
    result = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    future_years = range(2014,2051)
    future_frame = pd.DataFrame({'Year':future_years})
    df_new = pd.concat([df,future_frame])
    y_values_lin1 = df_new['Year']*result.slope+result.intercept
    plt.plot(df_new['Year'],y_values_lin1)
    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    result2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    df2 = pd.concat([df2,future_frame])
    y_values_lin2 = df2['Year']*result2.slope+result2.intercept
    plt.plot(df2['Year'],y_values_lin2)
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()