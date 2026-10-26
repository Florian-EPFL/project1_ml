import numpy as np
from feature_metadata import FEATURE_INFO

# ******** helpers ************

# gets all non-response codes (don't know, refused, etc.) of a feature, as a flat list
def get_nonresponse_codes(name):
    return [v for codes in FEATURE_INFO[name]["nonresponse_codes"].values() for v in codes]

# true where a value is missing, so NaN, and also non-response codes if replace_nonresponse
def get_missing_mask(name, data, replace_nonresponse=False):
    missing_mask = np.isnan(data)
    if replace_nonresponse:
        missing_mask |= np.isin(data, get_nonresponse_codes(name))
    return missing_mask

# replace codes that stand for a numeric answer by that value, must be applied before imputation
def apply_value_recodes(name, data):
    data_recoded = data.copy()
    for code, value in FEATURE_INFO[name]["value_recode"].items():
        data_recoded[data == code] = value
    return data_recoded

# ******** imputations techniques ************

def impute_none(name, data, replace_nonresponse=False, impute_param=None):
    return data.copy(), impute_param

def impute_mode(name, data, replace_nonresponse=False, impute_param=None):
    # tracking what data is missing (NaN, and non-response codes if replace_nonresponse = True)
    missing_mask = get_missing_mask(name, data, replace_nonresponse)
    data_imputed = data.copy()

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            raise ValueError(f"Feature {name} has no observed values to impute from.")

        # get the most common value and store it: this is going to be imputed
        values, counts = np.unique(non_missing_data, return_counts=True)
        impute_param = values[np.argmax(counts)]

    data_imputed[missing_mask] = impute_param

    return data_imputed, impute_param


def impute_median(name, data, replace_nonresponse=False, impute_param=None):
    assert FEATURE_INFO[name]["data_type"] in ["ordinal", "discrete", "continuous"]

    # tracking what data is missing (NaN, and non-response codes if replace_nonresponse = True)
    missing_mask = get_missing_mask(name, data, replace_nonresponse)
    data_imputed = data.copy()

    # if we dont specify the setting parameter it is implied we are imputing in the training set
    if impute_param is None:
        non_missing_data = data[~missing_mask]

        if len(non_missing_data) == 0:
            raise ValueError(f"Feature {name} has no observed values to impute from.")

        # get the median value of the training set
        impute_param = np.median(non_missing_data)
    
    data_imputed[missing_mask] = impute_param

    return data_imputed, impute_param


def impute_random(name, data, replace_nonresponse=False, impute_param=None, seed=67):
    # tracking what data is missing (NaN, and non-response codes if replace_nonresponse = True)
    missing_mask = get_missing_mask(name, data, replace_nonresponse)
    data_imputed = data.copy()

    if impute_param is None:
        non_missing_data = data[~missing_mask]
        rng = np.random.default_rng(seed)

        impute_param = {"distribution": non_missing_data, "rng": rng}

        if len(non_missing_data) == 0:
            raise ValueError(f"Feature {name} has no observed values to impute from.")
        
    n_missing = np.sum(missing_mask)

    data_imputed[missing_mask] = impute_param["rng"].choice(
        impute_param["distribution"],
        size=n_missing,
        replace=True
    )

    return data_imputed, impute_param

# we can add an extra column that indicates the observation was imputed, could hold extra information
def missingness_indicator(name, data, replace_nonresponse=False, replace_nan=True):
    missing_mask = np.zeros(data.shape, dtype=bool)

    if replace_nan:
        missing_mask |= np.isnan(data)

    if replace_nonresponse:
        missing_mask |= np.isin(data, get_nonresponse_codes(name))

    return missing_mask.astype(int)

# ******** standrdaize ************

# standardize a continuous or discrete numerical feature using training mean and std
def standardize_feature(feature, name, standardize_param = None):
    if FEATURE_INFO[name]["data_type"] in ("continuous", "discrete"):
        feature = feature.astype(float, copy=True)

        # for training set compute mean and std
        if standardize_param is None:
            standardize_param = (np.nanmean(feature), np.nanstd(feature))

        # for test set reuse the ones passed in
        mean, std = standardize_param

        if std > 0:
            feature = (feature - mean) / std

    return feature, standardize_param