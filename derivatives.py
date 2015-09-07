#derivatives


deriv = lambda f, epsilon: lambda x: (f(x+epsilon) - f(x))/epsilon
nth_deriv = lambda f, n, epsilon: deriv(nth_deriv(f, n-1,epsilon),epsilon) if n > 0 else f
