import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ["date"], index_col = "date")

# Clean data
f25 = df['value'] <= df['value'].quantile(0.025)
f75 = df['value'] >= df['value'].quantile(0.975)
df = df.drop(index=df[(f25 | f75)].index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots() 
    fig.set_figheight(6)
    fig.set_figwidth(14)

    plt.plot(df['value'],color='red',linewidth=1, linestyle="solid")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views') 

   # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    list_month= ['January','February','March','April','May','June','July','August','September','October','November','December']

    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month

    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    sns.set_style("whitegrid")

    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    plt.title('')
    plt.xlabel('Years', fontsize = '13')
    plt.ylabel('Average Page Views', fontsize = '13')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = list_month)
    title = lg.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()

    df_box['Year'] = pd.DatetimeIndex(df_box.index).year
    df_box['Month'] = pd.DatetimeIndex(df_box.index).month

    list_month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axes = plt.subplots(1, 2, figsize=(18, 18))
    sns.set_style("whitegrid")

    sns.boxplot(ax=axes[0], data=df_box, x='Year', y='value')
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize = '15')
    axes[0].set_xlabel('Year', fontsize = '15')
    axes[0].set_ylabel('Page Views', fontsize = '15')


    sns.boxplot(ax=axes[1], data=df_box, x='Month', y='value')
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize = '15')
    axes[1].set_xlabel('Month', fontsize = '15')
    axes[1].set_ylabel('Page Views', fontsize = '15')
    axes[1].set_xticklabels(list_month)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig