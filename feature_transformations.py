import numpy as np
from feature_metadata import FEATURE_INFO
from feature_imputation import impute_mode, impute_median, standardize_feature

IMPUTE = {
    "mode": impute_mode,
    "median": impute_median,
}

# show why (-1, 1) is used for binary features instead of (0, 1)
def transform_binary(name, data, valid_values=None, impute_setting="mode", replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] == "binary"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    
    if valid_values is None:
        unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros(data_imputed.shape)

    if len(valid_values) == 1:
        new_values = [1]
    else:
        new_values = [-1, 1]
    
    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data_imputed, v)] = new_values[n]

    return data_transformed, valid_values, impute_param

# implemnts K encoding, needs regularization
def transform_categorical(name, data, valid_values=None, impute_setting="mode", replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] == "categorical"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    
    if valid_values is None:
        unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros((data_imputed.shape[0], len(valid_values)), dtype=np.uint8)

    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data_imputed, v), n] = 1

    return data_transformed, valid_values, impute_param

def transform_ordinal(name, data, valid_values=None, impute_setting="median", replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] == "ordinal"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]
    special_codes = FEATURE_INFO[name]["non_numeric_valid_codes"]

    if valid_values is None:
        valid_values = FEATURE_INFO[name]["ordinal_levels"]
        if valid_values is None:
            unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
            valid_values = unique_values[~np.isin(unique_values, nonresponse_codes + special_codes)]

    data_transformed = np.zeros((data_imputed.shape[0], 2 + bool(special_codes)))

    for n, v in enumerate(valid_values):
        data_transformed[data_imputed == v, 0] = 2 * n / (len(valid_values) - 1) - 1

    data_transformed[:, 1] = np.isnan(data_imputed) | np.isin(data_imputed, nonresponse_codes)

    if special_codes:
        data_transformed[:, 2] = np.isin(data_imputed, special_codes)

    return data_transformed, valid_values, impute_param



def transform_discrete(name, data, valid_values=None, impute_setting="median", replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] == "discrete"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]

    if valid_values is None:
            unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
            valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = standardize_feature(data_imputed, name)

    return data_transformed, valid_values, impute_param


def transform_continuous(name, data, valid_values=None, impute_setting="median", replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] == "continuous"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]

    if valid_values is None:
            unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
            valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = standardize_feature(data_imputed, name)

    return data_transformed, valid_values, impute_param