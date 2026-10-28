# Project 1 - Machine Learning
### by Naji Amrani, Maja Kubik and Florian Lepoutre

Course CS-433 Machine Learning, EPFL (Fall 2026).
Prediction of heart attack risk (coronary heart disease) from the BRFSS 2015 health survey (more than 300'000 individuals, 321 raw features), using only **NumPy** (plus matplotlib for plots).

The method, the experiments and the results are described in the report: **`report.pdf`**.

---

## Dataset (important)

The dataset is **not** included in this repository. Before running anything, download it from the
[AIcrowd competition page](https://www.aicrowd.com/challenges/epfl-machine-learning-project-1) and place the three files **in `./data/dataset`** (relative to the root of the repository), keeping their original names:

```
data/
└── dataset/
    ├── x_train.csv
    ├── y_train.csv
    └── x_test.csv
```

The code reads the data from `./data/dataset` (see `data_path` in `run.ipynb`), so all scripts and notebooks must be run **from the root of the repository**. The `data/` folder is not versioned.

---

## Requirements

- Python 3.9 or newer
- `numpy`
- `matplotlib` (visualization only)
- `jupyter` (to open the notebooks)

```bash
pip install numpy matplotlib jupyter
```

No other external library is used (no pandas, scikit-learn, etc.), as required by the project rules.

---

## Reproducing our submission

1. Put the dataset in `./data/dataset` (see above).
2. From the root of the repository, open and run **all cells** of `run.ipynb`:
   ```bash
   jupyter notebook run.ipynb
   ```
3. The last cells train the final model and write the predictions to **`submission_test.csv`** (columns `Id`, `Prediction`, with values in {-1, 1}), which is the file we submitted to AIcrowd.

All random choices (cross-validation folds, train/validation split, SGD shuffling, random imputation) use fixed seeds, so the run is deterministic.

What `run.ipynb` does, in order:

1. **Loading** of the data with `load_csv_data`.
2. **Hyperparameter selection by 5-fold cross-validation**, with the features rebuilt inside each fold to avoid any leakage from the validation fold:
   - the imputation strategy for each feature type (none / mode / median / random),
   - the missingness threshold above which a feature is dropped.
3. **Feature matrix construction** on the train set, the same encoding being then applied to the test set, plus a bias column.
4. **Sanity checks** of the loss and of the gradient (comparison with a numerical gradient).
5. **Choice of the SGD settings** (step size, number of epochs) on an 80/20 split, with the training curves.
6. **Evaluation against a baseline** (always predicting "not sick") and **selection of the decision threshold** that maximizes the F1 score.
7. **Selection of the regularization parameter lambda** by 5-fold cross-validation (F1 score and validation loss).
8. **Final training** on the full training set with the selected lambda, **prediction on the test set** with the selected threshold, and **writing of the submission file**.

---

## Method in short

- **Model**: ridge logistic regression (labels in {-1, 1}), trained by mini-batch SGD (batch size 32). The bias is not penalized.
- **Preprocessing**: every feature is handled according to its type (binary, categorical, ordinal, discrete, continuous), defined from the BRFSS codebook. Non-response codes ("don't know", "refused") are treated as missing values, special codes that stand for a numerical answer are recoded (e.g. 88 -> 0 days), identifiers, survey-design variables, sampling weights and interview dates are excluded. A missingness indicator is added for most features.
- **Class imbalance**: only about 9% of the individuals are positive, so the decision threshold is tuned on the F1 score instead of using 0.5.
- **Validation**: k-fold cross-validation with out-of-fold predictions; the threshold is chosen on all out-of-fold predictions at once.

See `report.pdf` for the justification of each choice and the results.

---

## Repository structure

| File | Description |
|---|---|
| `report.pdf` | The 2-page report describing our approach and findings. |
| `run.ipynb` | Main notebook: reproduces the whole pipeline and generates `submission_test.csv`. |
| `feature_analysis.ipynb` | Exploratory data analysis (missing values, feature types, correlations with the target, ...). Not needed to reproduce the submission. |
| `implementations.py` | The six basic methods required by the project (least squares GD / SGD, normal equations, ridge regression, (regularized) logistic regression). |
| `helpers.py` | Provided helpers: `load_csv_data` and `create_csv_submission`. |
| `preprocessing.py` | Feature matrix construction (`build_feature_matrix`), dropping of features with too many missing values, bias column. |
| `feature_metadata.py` | Description of the 321 features from the BRFSS codebook: groups, types, non-response codes, special-value recodes, excluded features. Builds the `FEATURE_INFO` dictionary. |
| `feature_transformations.py` | One transformation per feature type (binary, categorical, ordinal, discrete, continuous). |
| `feature_imputation.py` | Imputation strategies (none, mode, median, random), missingness indicator and standardization. |
| `training.py` | Ridge logistic regression with mini-batch SGD, loss and gradient, train/validation split, k-fold cross-validation (also with features built inside each fold). |
| `postprocessing.py` | Metrics (accuracy, precision, recall, F1) and search of the best decision threshold. |
| `codebook15_llcp.pdf` | BRFSS 2015 codebook, used to build the feature metadata. |
| `project1_description.pdf` | Project description given by the course. |
| `submission_test.csv` | Predictions for the test set generated by `run.ipynb`. |
| `data/dataset/` | **Not versioned.** Must contain `x_train.csv`, `y_train.csv` and `x_test.csv`. |

---

## Notes

- Run everything from the root of the repository, otherwise the relative paths (`./data/dataset`) and the local imports will fail.
- The training on the full dataset and the cross-validations can take a few minutes.
