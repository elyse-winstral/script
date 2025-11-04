import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Monte Carlo Methods
    Originating from statistical physics and finance, Monte Carlo methods are numerical algorithms for computing stochastic expectations via random sampling. They rely on the law of large numbers, which guarantees convergence to the true expectation, and the central limit theorem, which guarantees a convergence rate of order $1/\sqrt{n}$, $n$ where is the number of samples.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    return norm, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Computing Pi""")
    return


@app.cell
def _(np, plt):
    x, y = np.random.uniform(-1, 1, size=(2, 1000))
    plt.scatter(x, y, s=1)
    plt.gca().add_artist(plt.Circle((0, 0), 1, color='red', alpha=0.3))
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', 'box')
    plt.show()
    return


@app.cell
def _(np, plt):
    errors = []
    N = np.logspace(1, 6, num=20, dtype=int)
    for n in N:
        x2, y2 = np.random.uniform(-1, 1, size=(2, n))
        pi_estimate = 4 * np.sum(x2**2 + y2**2 <= 1) / n
        errors.append(abs(np.pi - pi_estimate))
    plt.figure(figsize=(10, 6))
    plt.loglog(N, errors, label='Approximation Error of π')
    plt.xlabel("Number of samples")
    plt.ylabel("Error")
    plt.title(r"Approximation Error of $\pi$")
    plt.legend()
    plt.show()
    return N, errors


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Computing Option Prices
    The following stock price model by Black, Merton, and Scholes was awarded the 1997 Nobel Prize in Economics.
    """
    )
    return


@app.cell
def _(np, plt):
    S0, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    brownian_motion = np.cumsum(np.random.normal(0, np.sqrt(T) / np.sqrt(252), (252, 50)), axis=0)
    prices = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * brownian_motion)
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(1, 253) / 252 * T, prices)
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.title('Evolution of Black-Scholes Stock Prices')
    plt.show()
    return K, S0, T, prices, r, sigma


@app.cell
def _(K, N, S0, T, errors, norm, np, plt, prices, r, sigma):
    option_price = S0 * norm.cdf((np.log(S0/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))) - K * np.exp(-r * T) * norm.cdf((np.log(S0/K) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T)))
    N2 = np.logspace(1, 6, num=20, dtype=int)
    errors2 = []
    for n2 in N:
        prices2 = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * np.random.randn(n2))
        option_estimate = np.exp(-r * T) * np.mean(np.maximum(prices - K, 0))
        errors2.append(abs(option_price - option_estimate))
    plt.figure(figsize=(10, 6))
    plt.loglog(N, errors)
    plt.xlabel("Number of samples")
    plt.ylabel("Error")
    plt.title("Approximation Error of Black-Scholes Option Prices")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
