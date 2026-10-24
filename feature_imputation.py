import numpy as np
from feature_metadata import FEATURE_INFO
import csv
import os

#***** for using the data sets ******

def check_header(x_train, path):
    with open(os.path.join(path, "x_train.csv")) as f:
        reader = csv.reader(f)
        header = next(reader)

    # remove index
    header = header[1:]

    # check header list size against shape of x_trian
    if int(len(header)) == int(x_train.shape[1]): 
        print("Header okay!")
    return np.array(header)

# takes name as argument, return the data column for that name
def get_column_by_name(name, header, x_train):
    idx = header.index(name)
    column = x_train[:, idx]
    return column, idx

# **********************************

# ********* for cleaning ***********
def remove_features_threshold_mask(data, threshold=0.5):
    # calculate percentage missing data per feature
    missing_per_feature = np.isnan(data).sum(axis=0) / data.shape[0]

    mask = missing_per_feature <= threshold
    return mask

def remove_data_type_mask(header, data_type):
    mask = [FEATURE_INFO[name]["data_type"] != data_type for name in header]
    return mask
# *******************************



# ************* imputation techniques *************
def impute_mode(name, data, replace_nonresponse=False, impute_param=None):
    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    # tracking what data is missing
    missing_mask = np.isnan(data)

    # adding non response codes as missing data if asked
    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            print(f"WARNING: this feature ({name}) is empty")
            return data, 0

        # get the most common value and store it: this is going to be imputed
        values, counts = np.unique(non_missing_data, return_counts=True)
        impute_param = values[np.argmax(counts)]

    data_imputed = data.copy()
    data_imputed[missing_mask] = impute_param

    return data_imputed, impute_param


def impute_median(name, data, replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] in ["ordinal", "discrete", "continuous"]

    nonresponse_codes = [
        v
        for codes in FEATURE_INFO[name]["nonresponse_codes"].values()
        for v in codes
    ]

    # tracking what data is missing
    missing_mask = np.isnan(data)

    # adding non response codes as missing data if asked
    if replace_nonresponse:
        missing_mask |= np.isin(data, nonresponse_codes)

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            print(f"WARNING: this feature ({name}) is empty")
            return data.copy(), 0

        # get the median value of the test set
        impute_param = np.median(non_missing_data)

    data_imputed = data.copy()
    data_imputed[missing_mask] = impute_param

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

