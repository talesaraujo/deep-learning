def cost_function(X, Y, m, W):
    return (1/(2*m)) * ((X @ W) - y).T @ ((X @ W) - y)


def gradient_descent(X, Y, m, n, n_iterations=1000, learning_rate=0.001, verbose=False):
    #W = np.random.rand(n)
    W = np.zeros(n)

    for iteration in range(n_iterations):
        W = W - (learning_rate/m) * (X.T @ ((X @ W.T) - Y))

        J = cost_function(X, Y, m, W)

        if (verbose):
            print("Iteration: {} | Cost: {} | Theta: {}".format(iteration+1, J, W))

    return (W, J)
