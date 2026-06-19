# Iris Dataset Exploration and Visualization

This repository contains the complete implementation for loading, inspecting, and visualizing the classic Iris dataset using Python's standard data science toolset (`pandas`, `matplotlib`, and `seaborn`).


> Project Structure

   text
├── plots/                    # Output directory for high-resolution plots
│   ├── scatter_sepal.png     # Scatter plot of Sepal Length vs Sepal Width
│   ├── scatter_petal.png     # Scatter plot of Petal Length vs Petal Width
│   ├── histograms.png        # Value distributions for all 4 features (with KDE lines)
│   └── box_plots.png         # Box plots highlighting outliers in red
├── explore_iris.py           # Self-contained, modular Python script
├── iris_exploration.ipynb    # Interactive Jupyter Notebook
├── iris.csv                  # Cached local copy of the Iris dataset (auto-downloaded)
└── README.md                 # Project documentation and setup guide



> Setup & Usage

To run the script and notebook, ensure you have Python 3.x and the required libraries installed.

>> 1. Installation
Install the required dependencies using pip:
  bash
pip install pandas matplotlib seaborn


If you wish to use the Jupyter Notebook, install the notebook package or use the VS Code Jupyter Extension:
  bash
pip install notebook


> 2. Running the Python Script
Run the script to automatically load the dataset, print statistical summaries directly to the console, and save high-resolution plots:
  bash
python explore_iris.py


> 3. Running the Jupyter Notebook
Open the workspace in **VS Code**, open `iris_exploration.ipynb`, select your Python kernel, and run all cells to view the step-by-step documentation and plots inline.


>> Analysis & Observations

> 1. Species Separability
* Iris-setosa is completely linearly separable from versicolor and virginica using petal width and petal length. Setosa features much smaller, tightly clustered petals.
* Iris-versicolor and Iris-virginica have minor overlap but are mostly distinct, particularly in their petal dimensions.

> 2. Feature Distributions
* Petal dimensions (length and width) display a highly bimodal distribution. This is due to the small, distinct petal sizes of Iris-setosa compared to the other two species.
* Sepal dimensions display a more symmetric, unimodal (normal-like) distribution.

> 3. Outliers
* The Box Plots identify some statistical outliers:
  * Iris-setosa has minor outliers in sepal width and petal length.
  * Iris-versicolor has minor outliers in petal length.
* These outliers are automatically highlighted in red on the generated box plots for clear visual verification.


## *Author by:* 
## *Muhammad Abdullah*
## *(DHC-8675)*
