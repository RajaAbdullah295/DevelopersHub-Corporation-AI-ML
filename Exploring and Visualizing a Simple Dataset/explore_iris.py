#!/usr/bin/env python3
"""
Iris Dataset Exploration and Visualization
Loads, inspects, and visualizes the Iris dataset using pandas, matplotlib, and seaborn.
Generates statistical summaries and high-quality visualizations.
"""

import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
DATASET_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
DATASET_PATH = "iris.csv"
PLOTS_DIR = "plots"

def download_dataset():
    """Downloads the Iris dataset if it is not already present locally."""
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset '{DATASET_PATH}' not found locally. Downloading from {DATASET_URL}...")
        try:
            urllib.request.urlretrieve(DATASET_URL, DATASET_PATH)
            print("Download successful.")
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            print("Attempting Seaborn library fallback...")

def load_data():
    """Loads the Iris dataset into a pandas DataFrame."""
    try:
        df = pd.read_csv(DATASET_PATH)
        return df
    except FileNotFoundError:
        try:
            df = sns.load_dataset("iris")
            df.to_csv(DATASET_PATH, index=False)
            return df
        except Exception as e:
            print(f"Failed to load dataset: {e}")
            raise

def inspect_data(df):
    """Prints basic shape, column names, head, and summary statistics of the dataset."""
    print("\n--- Dataset Shape (rows, columns) ---")
    print(df.shape)
    
    print("\n--- Column Names ---")
    print(list(df.columns))
    
    print("\n--- First 5 Rows (df.head()) ---")
    print(df.head())
    
    print("\n--- Dataset Information (df.info()) ---")
    df.info()
    
    print("\n--- Descriptive Statistics (df.describe()) ---")
    print(df.describe())
    
    print("\n--- Species Distribution ---")
    print(df['species'].value_counts())
    print("-" * 50)

def generate_visualizations(df):
    """Generates and saves high-quality visualizations using Seaborn and Matplotlib."""
    os.makedirs(PLOTS_DIR, exist_ok=True)
    
    # Set premium plot style
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams.update({
        'figure.autolayout': True,
        'font.family': 'sans-serif',
        'axes.titleweight': 'bold',
        'axes.labelweight': 'semibold',
        'figure.titlesize': 20,
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12
    })
    
    # Custom color palette
    palette = {"setosa": "#4F46E5", "versicolor": "#10B981", "virginica": "#F59E0B"}
    
    print("Generating visualizations...")

    # 1. Scatter Plots
    # Sepal Dimensions Scatter
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.scatterplot(
        data=df, 
        x="sepal_length", 
        y="sepal_width", 
        hue="species", 
        palette=palette,
        s=80, 
        alpha=0.85, 
        edgecolor="w", 
        linewidth=0.75,
        ax=ax
    )
    ax.set_title("Sepal Dimensions: Length vs Width")
    ax.set_xlabel("Sepal Length (cm)")
    ax.set_ylabel("Sepal Width (cm)")
    ax.legend(title="Species", frameon=True, facecolor="white", edgecolor="none", shadow=True)
    plt.savefig(os.path.join(PLOTS_DIR, "scatter_sepal.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Petal Dimensions Scatter
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.scatterplot(
        data=df, 
        x="petal_length", 
        y="petal_width", 
        hue="species", 
        palette=palette,
        s=80, 
        alpha=0.85, 
        edgecolor="w", 
        linewidth=0.75,
        ax=ax
    )
    ax.set_title("Petal Dimensions: Length vs Width")
    ax.set_xlabel("Petal Length (cm)")
    ax.set_ylabel("Petal Width (cm)")
    ax.legend(title="Species", frameon=True, facecolor="white", edgecolor="none", shadow=True)
    plt.savefig(os.path.join(PLOTS_DIR, "scatter_petal.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Histograms (Value Distributions)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    feature_labels = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]
    
    for i, (feature, label) in enumerate(zip(features, feature_labels)):
        row, col = divmod(i, 2)
        ax = axes[row, col]
        sns.histplot(
            data=df,
            x=feature,
            hue="species",
            kde=True,
            multiple="layer",
            palette=palette,
            alpha=0.45,
            element="bars",
            edgecolor="w",
            linewidth=0.5,
            ax=ax,
            legend=(i == 3)
        )
        ax.set_title(f"Distribution of {label.split(' (')[0]}")
        ax.set_xlabel(label)
        ax.set_ylabel("Count")
        
        if i == 3 and ax.get_legend() is not None:
            ax.get_legend().set_title("Species")
            
    fig.suptitle("Value Distributions of Iris Features", y=0.98)
    plt.savefig(os.path.join(PLOTS_DIR, "histograms.png"), dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Box Plots (Identify Outliers)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    for i, (feature, label) in enumerate(zip(features, feature_labels)):
        row, col = divmod(i, 2)
        ax = axes[row, col]
        sns.boxplot(
            data=df,
            x="species",
            y=feature,
            palette=palette,
            hue="species",
            legend=False,
            width=0.6,
            linewidth=1.5,
            fliersize=6,
            flierprops={"markerfacecolor": "red", "markeredgecolor": "black", "marker": "o"},
            ax=ax
        )
        ax.set_title(f"{label.split(' (')[0]} by Species")
        ax.set_xlabel("Species")
        ax.set_ylabel(label)
        
    fig.suptitle("Feature Box Plots by Species (Outliers in Red)", y=0.98)
    plt.savefig(os.path.join(PLOTS_DIR, "box_plots.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Visualizations successfully saved in the '{PLOTS_DIR}' directory.")

def main():
    download_dataset()
    df = load_data()
    inspect_data(df)
    generate_visualizations(df)

if __name__ == "__main__":
    main()
