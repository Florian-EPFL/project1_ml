import csv
import os
import numpy as np
from feature_metadata import FEATURE_INFO, EXCLUDED_FEATURES
from feature_transformations import *

# transformation for each data type; "encoded" features are not transformed
# the dataset also contains cleaned derived versions of them
TRANSFORMS = {
    "binary": transform_binary,
    "categorical": transform_categorical,
    "ordinal": transform_ordinal,
    "discrete": transform_discrete,
    "continuous": transform_continuous,
}

def check_header(x_train, path):

    with open(os.path.join(path, "x_train.csv")) as f:
        reader = csv.reader(f)
        header = next(reader)

    # remove index
    header = header[1:]

    # check header list size against shape od x_trian
    if int(len(header)) == int(x_train.shape[1]):
        print("Header okay!")
    return header


# takes name as argument, return the data column for that name
def get_column_by_name(name, header, x_train):
    idx = header.index(name)
    column = x_train[:, idx]
    return column, idx


# gives number of NaNs in each column
def check_missing_features(x_train):
    missing_cols = np.isnan(x_train).sum(axis=0)
    return missing_cols


# gives number of NaNs in each row
def check_missing_observations(x_train):
    missing_obs = np.isnan(x_train).sum(axis=1)
    return missing_obs


def drop_high_missing_features(x_train, x_test, header, threshold=0.9):
    """Remove the columns whose fraction of NaNs in the train set exceeds threshold.
    The mask is computed on the train set and applied as is to the test set."""
    # fraction of NaNs in each column of the train set
    frac_missing_cols = check_missing_features(x_train) / x_train.shape[0]
    # keep only columns at or below the threshold
    keep_mask = frac_missing_cols <= threshold

    header_array = np.array(header)
    return x_train[:, keep_mask], x_test[:, keep_mask], list(header_array[keep_mask])



def build_feature_matrix(x_train, x_test, header):
    """Transform the raw train and test data into feature matrices.

    For each feature, the valid values are computed on the train set and reused
    on the test set, so both matrices have exactly the same columns.

    Returns X_train (N_train, D), X_test (N_test, D) and the names of the D columns.
    """
    blocks_train = []
    blocks_test = []
    names = []

    for i, name in enumerate(header):
        # skip excluded features
        if name in EXCLUDED_FEATURES:
            continue
        # skip encoded features (see TRANSFORMS)
        data_type = FEATURE_INFO[name]["data_type"]
        if data_type not in TRANSFORMS:
            continue

        # transform train (valid values, imputation and standardization parameters computed),
        # then test (the train parameters are reused)
        transformed_x_train, valid_values, impute_param, standardize_param = TRANSFORMS[data_type](
            name, x_train[:, i], replace_nonresponse=True)
        transformed_x_test, _, _, _ = TRANSFORMS[data_type](
            name, x_test[:, i], valid_values, replace_nonresponse=True,
            impute_param=impute_param, standardize_param=standardize_param)

        # binary returns a (N,) vector and categorical returns uint8 -> everything to (N, k) float
        transformed_x_train = transformed_x_train.reshape(x_train.shape[0], -1).astype(float)
        transformed_x_test = transformed_x_test.reshape(x_test.shape[0], -1).astype(float)

        blocks_train.append(transformed_x_train)
        blocks_test.append(transformed_x_test)
        names += [f"{name}_{j}" for j in range(transformed_x_train.shape[1])]

    X_train = np.hstack(blocks_train)
    X_test = np.hstack(blocks_test)
    return X_train, X_test, names


def add_bias(X):
    """Add a column of ones at the beginning of X."""
    return np.c_[np.ones(X.shape[0]), X]