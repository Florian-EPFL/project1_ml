import numpy as np
from feature_metadata import FEATURE_INFO
import matplotlib.pyplot as plt


#************** testing functions **************
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


# ************* imputation techniques *************
def impute_none(name, data, replace_nonresponse=False, impute_param=None):
    return data.copy(), impute_param

def impute_mode(name, data, replace_nonresponse=False, impute_param=None):
    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    # tracking what data is missing
    missing_mask = np.isnan(data)
    data_imputed = data.copy()

    # adding non response codes as missing data if asked
    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            print(f"WARNING: this feature ({name}) is empty")
            return data_imputed, 0

        # get the most common value and store it: this is going to be imputed
        values, counts = np.unique(non_missing_data, return_counts=True)
        impute_param = values[np.argmax(counts)]

    data_imputed[missing_mask] = impute_param

    return data_imputed, impute_param


def impute_median(name, data, replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] in ["ordinal", "discrete", "continuous"]

    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    # tracking what data is missing and copyigng data
    missing_mask = np.isnan(data)
    data_imputed = data.copy()

    # adding non response codes as missing data if asked
    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            print(f"WARNING: this feature ({name}) is empty")
            return data_imputed, None

        # get the median value of the test set
        impute_param = np.median(non_missing_data)
    
    data_imputed[missing_mask] = impute_param

    return data_imputed, impute_param


def impute_random(name, data, replace_nonresponse=False, impute_param=None, seed=67):
    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    missing_mask = np.isnan(data)
    data_imputed = data.copy()

    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    if impute_param is None:
        non_missing_data = data[~missing_mask]
        rng = np.random.default_rng(seed)

        impute_param = {"distribution": non_missing_data, "rng": rng}

        if len(non_missing_data) == 0:
            print(f"WARNING: this feature ({name}) is empty")
            return data_imputed, impute_param
        
    n_missing = np.sum(missing_mask)

    data_imputed[missing_mask] = impute_param["rng"].choice(
        impute_param["distribution"],
        size=n_missing,
        replace=True
    )

    return data_imputed, impute_param



# we can add extra features that record the imputed value, could hold extra information
def missingness_indicator(name, data, replace_nonresponse=False, replace_nan=True):
    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    if replace_nan:
        missing_mask = np.isnan(data)

    # adding non response codes for imputation if asked
    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    return missing_mask.astype(int)






# ******** standrdaize ************
def standardize_feature(feature, name):
    """Standardize a continuous or discrete numerical feature."""

    if FEATURE_INFO[name]["data_type"] in ("continuous", "discrete"):
        feature = feature.astype(float, copy=True)

        mean = np.nanmean(feature)
        std = np.nanstd(feature)

        if std > 0:
            feature = (feature - mean) / std

    return feature

