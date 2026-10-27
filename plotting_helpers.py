import numpy as np
import matplotlib.pyplot as plt

def plot_feature_distribution(data, info, is_continuous=False):
    print(info)
    missing_cols = np.isnan(data).sum()
    print(f"missing data: {missing_cols} / {len(data)}")

    values, counts = np.unique(data, return_counts=True)

    print(f"possible values: {values}")

    if is_continuous:
        plt.hist(data, bins=100)
    else:
        plt.bar(values, counts)
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.title("Occurrences of each value")
    plt.show()