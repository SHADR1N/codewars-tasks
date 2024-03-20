
def series_sum(n):
    if n == 0:
        return "0.00"
    else:
        series_sum = sum(1 / (3 * i - 2) for i in range(1, n + 1))
        return "{:.2f}".format(series_sum)


