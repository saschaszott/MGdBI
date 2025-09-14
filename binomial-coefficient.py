def binomial_coefficient(n, k):
    """
    Calculates the binomial coefficient n choose k (nCk)
    which is the number of ways to choose k elements from a set of n elements.
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry nCk == nC(n-k) to reduce computations
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

n = 49
k = 6
result = binomial_coefficient(n, k)
print(f"{n}C{k} = {result}")