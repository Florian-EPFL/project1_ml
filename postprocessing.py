import numpy as np

def compute_metrics(y_true, y_pred):
    """Accuracy, precision, recall and F1 score for labels in {-1, 1} (1 = positive class)."""
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == -1))
    fn = np.sum((y_pred == -1) & (y_true == 1))

    accuracy = np.mean(y_pred == y_true)
    precision = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0

    return {"accuracy": float(accuracy), "precision": float(precision), "recall": float(recall), "f1": float(f1)}


def find_best_threshold(y, proba, thresholds=np.linspace(0.05, 0.95, 91)):
    """Return the threshold that maximizes the F1 score, its F1 score, and all F1 scores."""
    f1_scores = []
    for t in thresholds:
        y_pred = np.where(proba >= t, 1, -1)
        f1_scores.append(compute_metrics(y, y_pred)["f1"])

    best = np.argmax(f1_scores)
    return thresholds[best], f1_scores[best], np.array(f1_scores)