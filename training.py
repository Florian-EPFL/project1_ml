import csv
import os
import numpy as np
from postprocessing import find_best_threshold

def sigmoid(z):
    """Numerically stable sigmoid: 1 / (1 + exp(-z)) = exp(-log(1 + exp(-z)))."""
    return np.exp(-np.logaddexp(0, -z))


def compute_loss(y, tx, w):
    """Logistic loss for y in {-1, 1}: mean of log(1 + exp(-y * x^T w)).
    The ridge penalty is NOT included (easier to compare models)."""
    z = y * (tx @ w)
    return np.mean(np.logaddexp(0, -z))


def compute_gradient(y, tx, w, lambda_=0):
    """Gradient of the logistic loss for y in {-1, 1}, plus the ridge term 2 * lambda_ * w.
    The bias w[0] is not penalized."""
    z = y * (tx @ w)
    grad = -tx.T @ (y * sigmoid(-z)) / y.shape[0]

    # ridge term, without the bias
    w_reg = w.copy()
    w_reg[0] = 0
    return grad + 2 * lambda_ * w_reg



def split_data(tx, y, ratio=0.8, seed=0):
    """Randomly split the data into a training part (ratio) and a validation part (1 - ratio)."""
    rng = np.random.default_rng(seed)
    idx = rng.permutation(y.shape[0])
    n_train = int(ratio * y.shape[0])
    idx_train, idx_val = idx[:n_train], idx[n_train:]
    return tx[idx_train], tx[idx_val], y[idx_train], y[idx_val]


def sgd_logistic(y, tx, lambda_, initial_w, max_epochs, gamma, batch_size=32,
                 tx_val=None, y_val=None, seed=0, verbose=True):
    """Ridge logistic regression (y in {-1, 1}) trained with mini-batch SGD.

    At each epoch, the rows are shuffled and visited by mini-batches of size batch_size.
    The train (and validation, if given) losses are recorded at the end of each epoch.

    Returns the final w and a dict with the loss history.
    """
    rng = np.random.default_rng(seed)
    w = initial_w.copy()
    N = y.shape[0]
    history = {"train_loss": [], "val_loss": []}

    for epoch in range(max_epochs):
        # shuffle the rows at each epoch
        perm = rng.permutation(N)

        # one gradient step per mini-batch
        for start in range(0, N, batch_size):
            idx = perm[start:start + batch_size]
            grad = compute_gradient(y[idx], tx[idx], w, lambda_)
            w = w - gamma * grad

        # record losses at the end of the epoch (without the ridge penalty)
        history["train_loss"].append(compute_loss(y, tx, w))
        if tx_val is not None:
            history["val_loss"].append(compute_loss(y_val, tx_val, w))

        if verbose:
            msg = f"epoch {epoch + 1:3d}/{max_epochs} | train loss: {history['train_loss'][-1]:.5f}"
            if tx_val is not None:
                msg += f" | val loss: {history['val_loss'][-1]:.5f}"
            print(msg)

    return w, history


def predict_proba(tx, w):
    """Predicted probability of being sick (y = 1) for each row."""
    return sigmoid(tx @ w)


def predict_labels(tx, w, threshold=0.5):
    """Predicted labels in {-1, 1}: 1 if the probability is >= threshold, -1 otherwise."""
    return np.where(predict_proba(tx, w) >= threshold, 1, -1)


def build_k_indices(y, k_fold, seed=0):
    """Randomly split the row indices into k_fold groups of (almost) equal size."""
    rng = np.random.default_rng(seed)
    idx = rng.permutation(y.shape[0])
    return np.array_split(idx, k_fold)


def cross_validation(y, tx, k_indices, lambda_, gamma, max_epochs, batch_size=32, seed=0):
    """k-fold cross-validation of the SGD ridge logistic regression.

    Each fold is predicted by a model trained on the other folds (out-of-fold predictions).
    The decision threshold is then chosen on all out-of-fold predictions at once.

    Returns a dict with lambda_, the mean validation loss, the best threshold and its F1 score.
    """
    k_fold = len(k_indices)
    proba_oof = np.zeros(y.shape[0])
    val_losses = []

    for k in range(k_fold):
        # fold k is the validation part, all other folds are the training part
        idx_val = k_indices[k]
        idx_tr = np.concatenate([k_indices[j] for j in range(k_fold) if j != k])

        w, _ = sgd_logistic(y[idx_tr], tx[idx_tr], lambda_, np.zeros(tx.shape[1]),
                            max_epochs, gamma, batch_size, seed=seed, verbose=False)

        # out-of-fold predictions and validation loss
        proba_oof[idx_val] = predict_proba(tx[idx_val], w)
        val_losses.append(compute_loss(y[idx_val], tx[idx_val], w))

    # one threshold for all out-of-fold predictions
    best_t, best_f1, _ = find_best_threshold(y, proba_oof)

    return {"lambda": lambda_, "val_loss": np.mean(val_losses), "threshold": best_t, "f1": best_f1}