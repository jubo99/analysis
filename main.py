import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns

def create_box_plot(df, value_col):
    """
    Create a box plot for the specified column.
    Args:
    df: pd.DataFrame - The DataFrame containing the data.
    value_col: str - The name of the column to plot.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[value_col])
    plt.title('Box Plot of ' + value_col)
    plt.ylabel(value_col)
    plt.grid(True)
    plt.show()

def create_multiple_box_plots(df, columns):
    """
    Create box plots for multiple specified columns in a DataFrame.
    Args:
    df: pd.DataFrame - The DataFrame containing the data.
    columns: list - List of column names to plot.
    """
    plt.figure(figsize=(12, 8))
    df[columns].plot(kind='box', subplots=True, layout=(1, len(columns)), figsize=(12, 6))
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def create_box_plot_and_save(df, column, gt_value=None):
    """
    Create a box plot for a specific column and save it as a .png file.
    Optionally include a ground truth (GT) value as a reference line.
    Args:
    df: pd.DataFrame - The DataFrame containing the data.
    column: str - The name of the column to plot.
    gt_value: float - Optional GT value to display as a reference line.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[column])
    if gt_value is not None:
        plt.axhline(gt_value, color='r', linestyle='--', label=f'GT Value = {gt_value}')
        plt.legend()
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)
    plt.grid(True)
    plt.savefig(f"BoxPlot_{column}.png")
    plt.close()

# Example function calls commented out



def load_and_process_csv(filepath):
    """
    Load the CSV file and process it.
    Args:
    filepath: str - The path to the CSV file.
    
    Returns:
    pd.DataFrame - Processed DataFrame.
    """
    df = pd.read_csv(filepath)
    df['Time of Measurement'] = pd.to_datetime(df['Time of Measurement'], format='%d.%m.%Y %H:%M:%S')
    return df

def analyze_data(df):
    """
    Perform basic statistical analysis on the DataFrame.
    Args:
    df: pd.DataFrame - The DataFrame to analyze.
    
    Returns:
    pd.DataFrame - Descriptive statistics.
    """
    return df.describe()

def check_missing_data(df):
    """
    Check for missing data in the DataFrame.
    Args:
    df: pd.DataFrame - The DataFrame to check.
    
    Returns:
    pd.Series - Missing data counts for each column.
    """
    return df.isnull().sum()

def create_candlestick_chart(df, date_col, value_col):
    """
    Create a candlestick chart for the specified column.
    Args:
    df: pd.DataFrame - The DataFrame containing the data.
    date_col: str - The name of the column with date values.
    value_col: str - The name of the column with values to plot.
    """
    df_daily = df.resample('D', on=date_col).agg({
        value_col: ['first', 'max', 'min', 'last']
    })
    df_daily.columns = ['Open', 'High', 'Low', 'Close']  # Renaming for clarity

    fig = go.Figure(data=[go.Candlestick(x=df_daily.index,
                                         open=df_daily['Open'],
                                         high=df_daily['High'],
                                         low=df_daily['Low'],
                                         close=df_daily['Close'])])
    fig.update_layout(title='Candlestick chart for ' + value_col,
                      xaxis_title='Date',
                      yaxis_title=value_col,
                      xaxis_rangeslider_visible=False)
    fig.show()

# Example usage (commented out):
filepath = '/Users/julianbogenberger/PycharmProjects/Analysis_adapt/SampleLogFile_Varying4Degrees.csv'
df = load_and_process_csv(filepath)
print(analyze_data(df))
print(check_missing_data(df))
# create_box_plot(df, 'Angle Value')
# create_multiple_box_plots(df, ['Angle Value', 'Time ICP', 'Time RANSAC'])
# create_candlestick_chart(df, 'Time of Measurement', 'Angle Value')
create_box_plot_and_save(df, 'Angle Value', gt_value=2.5)
create_box_plot_and_save(df, 'Time ICP')
create_box_plot_and_save(df, 'Time RANSAC')
