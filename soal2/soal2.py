import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the exact Excel file name as requested
file_name = 'p3-s2.xlsx'

# Read the excel file dynamically 
df = pd.read_excel(file_name)
df.columns = df.columns.str.strip()

size_col = df.columns[0]  # First column: Data size
alg1_col = 'Alg.1'
alg2_col = 'Alg.2'
alg3_col = 'Alg.3'

# Part C: Calculate the mean execution time for Alg.2 (100KB to 600KB)
mean_alg2 = df[alg2_col].mean()
print(f"Average execution time for Alg.2 (100KB-600KB): {mean_alg2}")

# Helper function to generate and save the 3 requested charts
def generate_and_save_plots(data_frame, version_suffix):
    sns.set_theme(style="whitegrid")
    
    # 1. Line Plot
    plt.figure(figsize=(8, 5))
    for col in [alg1_col, alg2_col, alg3_col]:
        plt.plot(data_frame[size_col], data_frame[col], marker='o', linewidth=2, label=col)
    plt.title(f'Execution Time Trend ({version_suffix.upper()})')
    plt.xlabel('Data Size')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'line_plot_{version_suffix}.png', dpi=300)
    plt.close()

    # 2. Bar Plot
    plt.figure(figsize=(9, 5))
    x_indices = np.arange(len(data_frame))
    bar_width = 0.25
    plt.bar(x_indices - bar_width, data_frame[alg1_col], bar_width, label=alg1_col)
    plt.bar(x_indices, data_frame[alg2_col], bar_width, label=alg2_col)
    plt.bar(x_indices + bar_width, data_frame[alg3_col], bar_width, label=alg3_col)
    plt.title(f'Execution Time per Size Group ({version_suffix.upper()})')
    plt.xlabel('Data Size')
    plt.ylabel('Execution Time (ms)')
    plt.xticks(x_indices, data_frame[size_col])
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'bar_plot_{version_suffix}.png', dpi=300)
    plt.close()

    # 3. Box Plot (Warning handled)
    plt.figure(figsize=(6, 5))
    melted_df = data_frame.melt(id_vars=[size_col], value_vars=[alg1_col, alg2_col, alg3_col],
                                var_name='Algorithm', value_name='Execution Time')
    sns.boxplot(x='Algorithm', y='Execution Time', data=melted_df, hue='Algorithm', palette='Set2', legend=False)
    plt.title(f'Execution Time Distribution ({version_suffix.upper()})')
    plt.xlabel('Algorithm')
    plt.ylabel('Execution Time (ms)')
    plt.tight_layout()
    plt.savefig(f'box_plot_{version_suffix}.png', dpi=300)
    plt.close()

# Generate initial plots
generate_and_save_plots(df, 'initial')

# Part B: Append New Row Dynamically
new_row = pd.DataFrame([{
    size_col: '700KB',
    alg1_col: 80,
    alg2_col: 320,
    alg3_col: 700
}])
df_updated = pd.concat([df, new_row], ignore_index=True)

# Generate updated plots
generate_and_save_plots(df_updated, 'updated')