
def least_squares(y, tx):
    """
    """

    A = np.dot(tx.T, tx)
    b = np.dot(tx.T, y)
    opt_w = np.linalg.solve(A, b)
    e = y - np.dot(tx, opt_w)
    mse = 0.5 * np.mean(e**2)
    return opt_w, mse


def ridge_regression(y, tx, lambda_):
    """
    """
    N = len(y)
    A = 2*N*lambda_*np.eye(tx.shape[1]) + np.dot(tx.T, tx)
    b = np.dot(tx.T, y)
    w = np.linalg.solve(A, b)
    e = y - np.dot(tx, w)
    loss = 0.5 * np.mean(e**2)
    return w, loss


def compute_gradient(y, tx, w):
    """
    """

    e = y - np.dot(tx, w)
    N = len(e)
    return -np.dot(tx.T, e)/N


def calculate_mse(e):
    """Calculate the mse for vector e."""
    return 1 / 2 * np.mean(e**2)



def mean_squared_error_gd(y, tx, initial_w, max_iters, gamma):
    """
    """

    # Define parameters to store w and loss
    ws = [initial_w]
    w = initial_w


    grad = compute_gradient(y, tx, w)
    err = y - np.dot(tx, w)
    loss = calculate_mse(err)

    losses = [loss]
    print(losses)
    for n_iter in range(max_iters):

        
        grad = compute_gradient(y, tx, ws[-1])
        w = w - gamma * grad
        ws.append(w)

        err = y - np.dot(tx, w)
        loss = calculate_mse(err)
        losses.append(loss)
  

    w = ws[-1]
    loss = losses[-1]
    

    return w, loss



def compute_stoch_gradient(y, tx, w):
    """
    """

    e = y - np.dot(tx,w)
    return -np.dot(tx.T, e)

def batch_iter(y, tx, batch_size, num_batches=1, shuffle=True):
    """
    """
    data_size = len(y)  # NUmber of data points.
    batch_size = min(data_size, batch_size)  # Limit the possible size of the batch.
    max_batches = int(
        data_size / batch_size
    )  # The maximum amount of non-overlapping batches that can be extracted from the data.
    remainder = (
        data_size - max_batches * batch_size
    )  # Points that would be excluded if no overlap is allowed.

    if shuffle:
        # Generate an array of indexes indicating the start of each batch
        idxs = np.random.randint(max_batches, size=num_batches) * batch_size
        if remainder != 0:
            # Add an random offset to the start of each batch to eventually consider the remainder points
            idxs += np.random.randint(remainder + 1, size=num_batches)
    else:
        # If no shuffle is done, the array of indexes is circular.
        idxs = np.array([i % max_batches for i in range(num_batches)]) * batch_size

    for start in idxs:
        start_index = start  # The first data point of each batch
        end_index = (
            start_index + batch_size
        )  # The first data point of the following batch
        yield y[start_index:end_index], tx[start_index:end_index]

def mean_squared_error_sgd(y, tx, initial_w, max_iters, gamma):
    """
    """

    # Define parameters to store w and loss
    ws = [initial_w]
    losses = []
    w = initial_w

    for n_iter in range(max_iters):
        
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size=1):
            grad = compute_stoch_gradient(minibatch_y, minibatch_tx, w)
            w = w - gamma*grad
        
        ws.append(w)
        loss = calculate_mse(y - np.dot(tx, w))
        losses.append(loss)
        
        #raise NotImplementedError

        print(
            "SGD iter. {bi}/{ti}: loss={l}, w0={w0}, w1={w1}".format(
                bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]
            )
        )

    w = ws[-1].flatten()
    loss = losses[-1] if losses else calculate_mse(y - np.dot(tx, w))

    return w, loss


import numpy as np

def sigmoid(t):
    return 1.0 / (1 + np.exp(-t))

def calculate_loss(y, tx, w):
    assert y.shape[0] == tx.shape[0]
    assert tx.shape[1] == w.shape[0]

    pred = sigmoid(tx.dot(w))
    loss = y.T.dot(np.log(pred)) + (1 - y).T.dot(np.log(1 - pred))
    return np.asarray(np.squeeze(-loss).item() * (1 / y.shape[0]))


def learning_by_gradient_descent(y, tx, w, gamma):
    loss = calculate_loss(y, tx, w)

    pred = sigmoid(tx.dot(w))
    grad = tx.T.dot(pred - y) * (1 / y.shape[0])
    w -= gamma * grad
    return loss, w


def logistic_regression(y, tx, initial_w, max_iters, gamma):
    """
    """

    w = initial_w.copy()

    losses = []
    ws = []

    for _ in range(max_iters):
        # get loss and update w.
        loss, w = learning_by_gradient_descent(y, tx, w, gamma)

        losses.append(loss)
        ws.append(w)


    w = ws[-1] if ws else initial_w.copy()
    loss = calculate_loss(y, tx, w)

    return w, loss

def learning_by_gradient_descent_reg(y, tx, w, gamma, lambda_):
    loss = calculate_loss(y, tx, w) + lambda_ * np.sum(w**2)

    pred = sigmoid(tx.dot(w))
    grad = tx.T.dot(pred - y) * (1 / y.shape[0])
    grad += 2 * lambda_ * w


    w -= gamma * grad
    return loss, w


def reg_logistic_regression(y, tx, lambda_, initial_w, max_iters, gamma):
    """
    """

    w = initial_w.copy()

    losses = []
    ws = []

    for _ in range(max_iters):
        # Get loss and update w.
        loss, w = learning_by_gradient_descent_reg(
            y, tx, w, gamma, lambda_
        )

        losses.append(loss)
        ws.append(w)

    w = ws[-1] if ws else initial_w.copy()
    loss = calculate_loss(y, tx, w)

    return w, loss
