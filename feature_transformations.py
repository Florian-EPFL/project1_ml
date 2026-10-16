import numpy as np
from project1_ml.feature_metadata import FEATURE_INFO

# show why (-1, 1) is used for binary features instead of (0, 1)
def transform_binary(name, data, valid_values=None):
    assert FEATURE_INFO[name]["data_type"] == "binary"

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    
    if valid_values is None:
        unique_values = np.unique(data[~np.isnan(data)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros(data.shape)

    if len(valid_values) == 1:
        new_values = [1]
    else:
        new_values = [-1, 1]
    
    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data, v)] = new_values[n]

    return data_transformed, valid_values

# implemnts K encoding, needs regularization
def transform_categorical(name, data, valid_values=None):
    assert FEATURE_INFO[name]["data_type"] == "categorical"

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    
    if valid_values is None:
        unique_values = np.unique(data[~np.isnan(data)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros((data.shape[0], len(valid_values)), dtype=np.uint8)

    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data, v), n] = 1

    return data_transformed, valid_values

def transform_ordinal(name, data, valid_values=None):
    assert FEATURE_INFO[name]["data_type"] == "ordinal"

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    special_codes = FEATURE_INFO[name]["non_numeric_valid_codes"]

    if valid_values is None:
        valid_values = FEATURE_INFO[name]["ordinal_levels"]
        if valid_values is None:
            unique_values = np.unique(data[~np.isnan(data)])
            valid_values = unique_values[~np.isin(unique_values, nonresponse_codes + special_codes)]

    data_transformed = np.zeros((data.shape[0], 2 + bool(special_codes)))

    for n, v in enumerate(valid_values):
        data_transformed[data == v, 0] = 2 * n / (len(valid_values) - 1) - 1

    data_transformed[:, 1] = np.isnan(data) | np.isin(data, nonresponse_codes)

    if special_codes:
        data_transformed[:, 2] = np.isin(data, special_codes)

    return data_transformed, valid_values


