
# Project Title: Log File Analysis

## Description
This project provides tools for analyzing log files that contain measurements of system performance and behavior. It includes Python scripts for loading data, computing basic statistics, checking for missing values, and visualizing distributions through box plots, including a reference to a Ground Truth (GT) value for certain parameters.

## Features
- Load data from CSV files.
- Compute descriptive statistics for the dataset.
- Check for missing values in the dataset.
- Generate and save box plots for key metrics to visualize their distribution and identify outliers.

## Prerequisites
Before you run this project, you need to ensure that your environment has the following software installed:
- Python 3.7 or higher
- Pandas
- Matplotlib
- Seaborn
- Plotly (optional for additional types of plots)

## Installation
To set up your environment to run these scripts, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourrepository/log-analysis.git
   cd log-analysis
   ```

2. **Install the required Python libraries:**
   ```bash
   pip install pandas matplotlib seaborn plotly
   ```

3. **Prepare your data:**
   Ensure that your CSV file is formatted correctly, with headers matching those expected by the scripts (`Angle Value`, `Time total`, `Time RANSAC`, `Time ICP`, `Time of Measurement`).

## Usage
To run the analysis, follow these instructions:

1. **Modify the script to include your file path:**
   Edit `main.py` and replace `'path_to_your_file.csv'` with the path to your CSV file.

2. **Run the script:**
   Execute the main script to perform the analysis and generate plots.
   ```bash
   python main.py
   ```

3. **View the results:**
   Check the output plots in the specified output directory (`./output_plots` by default) and review the console output for statistical analysis and missing data information.

## Contributing
Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
