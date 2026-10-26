import numpy as np
from feature_metadata import FEATURE_INFO
from feature_imputation import *

IMPUTE = {
    "none": impute_none,
    "mode": impute_mode,
    "median": impute_median,
    "random": impute_random,
}


def transform_binary(name, data, valid_values=None, impute_setting="none", replace_nonresponse=False, impute_param=None, standardize_param=None):
    assert FEATURE_INFO[name]["data_type"] == "binary"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = get_nonresponse_codes(name)
    
    if valid_values is None:
        unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros((data_imputed.shape[0], 2))

    if len(valid_values) == 1:
        new_values = [1]
    else:
        new_values = [-1, 1]
    
    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data_imputed, v), 0] = new_values[n]

    # missingness indicator, computed on the raw data (before imputation)
    data_transformed[:, 1] = missingness_indicator(name, data, replace_nonresponse=True)

    return data_transformed, valid_values, impute_param, standardize_param

# implemnts K encoding, needs regularization
def transform_categorical(name, data, valid_values=None, impute_setting="none", replace_nonresponse=False, impute_param=None, standardize_param=None):
    assert FEATURE_INFO[name]["data_type"] == "categorical"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = get_nonresponse_codes(name)
    
    if valid_values is None:
        unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
        valid_values = unique_values[~np.isin(unique_values, nonresponse_codes)]

    data_transformed = np.zeros((data_imputed.shape[0], len(valid_values)), dtype=np.uint8)

    for n, v in enumerate(valid_values):
        data_transformed[np.isin(data_imputed, v), n] = 1

    return data_transformed, valid_values, impute_param, standardize_param

def transform_ordinal(name, data, valid_values=None, impute_setting="none", replace_nonresponse=False, impute_param=None, standardize_param=None):
    assert FEATURE_INFO[name]["data_type"] == "ordinal"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    nonresponse_codes = get_nonresponse_codes(name)
    special_codes = FEATURE_INFO[name]["non_numeric_valid_codes"]

    if valid_values is None:
        valid_values = FEATURE_INFO[name]["ordinal_levels"]
        if valid_values is None:
            unique_values = np.unique(data_imputed[~np.isnan(data_imputed)])
            valid_values = unique_values[~np.isin(unique_values, nonresponse_codes + special_codes)]

    data_transformed = np.zeros((data_imputed.shape[0], 2 + bool(special_codes)))

    for n, v in enumerate(valid_values):
        data_transformed[data_imputed == v, 0] = 2 * n / (len(valid_values) - 1) - 1

    # missingness indicator, computed on the raw data (before imputation)
    data_transformed[:, 1] = missingness_indicator(name, data, replace_nonresponse=True)

    if special_codes:
        data_transformed[:, 2] = np.isin(data, special_codes)

    return data_transformed, valid_values, impute_param, standardize_param



def transform_discrete(name, data, valid_values=None, impute_setting="median", replace_nonresponse=False, impute_param=None, standardize_param=None):
    assert FEATURE_INFO[name]["data_type"] == "discrete"

    # replace codes that stand for a numeric answer before imputing (using the recodes dictionary)
    data = apply_value_recodes(name, data)

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    data_standardized, standardize_param = standardize_feature(data_imputed, name, standardize_param)

    # column 0: standardized values, column 1: missingness indicator (computed on the raw data)
    data_transformed = np.column_stack([data_standardized, missingness_indicator(name, data, replace_nonresponse)])

    return data_transformed, valid_values, impute_param, standardize_param


def transform_continuous(name, data, valid_values=None, impute_setting="median", replace_nonresponse=False, impute_param=None, standardize_param=None):
    assert FEATURE_INFO[name]["data_type"] == "continuous"

    data_imputed, impute_param = IMPUTE[impute_setting](name, data, replace_nonresponse, impute_param)

    data_standardized, standardize_param = standardize_feature(data_imputed, name, standardize_param)

    # column 0: standardized values, column 1: missingness indicator (computed on the raw data)
    data_transformed = np.column_stack([data_standardized, missingness_indicator(name, data, replace_nonresponse)])

    return data_transformed, valid_values, impute_param, standardize_param