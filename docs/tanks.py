import marimo

'''
Conceptual Overview:

The German tank problem is a popular estimation example in statistics. It consists of estimating the maximum of a discrete unfiform distribution by sampling without replacement. The example highlights the contrast between Frequentist and Bayesian inference. In frequentist statistics, it is assumed that the parameter of interest (the value we wish to estimate) is fixed. The underlying truth i.e. the maximum amount of tanks produced is a non-random value. In Bayesian statistics, it is assumed the maximum $N$ is random - it can take on different values and has a distribution. 

The Frequentist approach estimates a single value for $\hat{N}$ - the estimation of $N$. This is given by $\hat{N} = m + \frac{m-k}{k}$. This can be seen as using the most likely estimator: the largest observed number $m$ added to the negative bias. (The bias is the expected difference between m and N- because m is a random sample the expectation can be taken w.r.t. to this distribution). 

The Bayesian approach models $N$ as a random variable with a so called prior distribution, denoted $\pi(N)$. A key element of Bayesian statistics lies in determining this prior. Here we use $\pi(N) \propto N ^ {-\alpha}$. Notice if \alpha = 0, we assume $N$ has a flat distribution- any outcome is equally likely. By changing $\alpha$ > 0, we can model certain beliefs or assumptions about the distribution of $N$ (i.e. whether it is concentrated around a certain value). By taking the expectation of $N | M = m, K = k$ we can estimate the amount of produced tanks given our observations.

For $\alpha = 1$ we get approximately the Frequentist formula. 

'''

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    # importing marimo is only necessary for the Marimo notebook (not necessary otherwise)
    import marimo as mo

    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    During World War II, production of German tanks such as the Panther was accurately estimated by Allied intelligence using statistical methods.

    The serial number gave information about how many tanks were produced, i.e. a tank with serial number $n$ was the $n$-th tank produced. Meaning, if the Allies found a tank serial number, this number was uniformally distributed between 1 and $N$. The question is: how can $N$ be estimated from a sequence of $k$ observed serial numbers $\{n_1, n_2, \dots, n_k \}$?

    Let $m$ be the maximum observed serial number. We consider the following variables: $M$ the observed maximum, $K$ the length of the observation, $N$ the true maximum.
    """)
    return


@app.function
def estimate_total_tanks(max_serial: int, num_observed: int, alpha: float = 1.5) -> float:
    return ((alpha + num_observed) / (alpha + num_observed - 1)) * max_serial


@app.cell
def _(mo):
    mo.md(r"""
    How can $N$ be estimated?

    The MLE of $N$ would simply be $M$, however this will be slightly lower than $N$ on average. To compensate for this, we can take the average gap between observations and add this to $M$:

    $$ \hat{N} = m + \frac{m - k}{k}  = m + \frac{m}{k} - 1 \approx \frac{1 + k}{k} m$$

    However, if we imagine $N$ to be random as well, we can model $P(N = n | M = m, K = k)$. From here we could find the expectation $n$ given our observations.
    """)
    return


@app.cell
def _(np):
    num_observed = 38
    monthly_production = 245
    n_simulations = 1000
    rng = np.random.RandomState(43)
    estimates = []

    for _ in range(n_simulations):
        observed_serials = rng.choice(range(1, monthly_production + 1), num_observed, replace=False)
        max_serial = max(observed_serials)
        estimates.append(estimate_total_tanks(max_serial, num_observed))

    return estimates, monthly_production


@app.cell
def _(estimates, monthly_production, plt):
    plt.figure(figsize=(10, 6))
    plt.hist(estimates, bins=30, alpha=0.7, color='b', edgecolor='black', density=True)
    plt.axvline(x=monthly_production, color='r', linestyle='dashed', linewidth=2, label=f'True Value ({monthly_production})')
    plt.xlabel('Estimated Total Tanks')
    plt.ylabel('Density')
    plt.title('Histogram of Estimated Total Tanks')
    plt.legend()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
