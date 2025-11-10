import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")

"""
Conceptual overview:
--------------------------------------
This notebook is an interactive visualization of the normal distribution. 

It demonstrates how the two parameters- mean (\mu) and standard deviation (\sigma)- change the probability density function. 

Conceptually:
- The mean (\mu) represents the expected value aka average value of the distribution. 
- The standard deviation (\sigma) is the square root of the variance (\sigma^2). It measures how spread out the values are around the mean. If random samples were generated according to this distribution, the variance describes how far these samples are from the mean \mu on average.
- Smaller std. dev. \sigma means the data is more tightly clustered around the mean
- Larger std. dev. \sigma means the data is more spread out 

The sliders demonstrate how these changes manifest in the pdf. 
"""


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Interactive Normal Distribution""")
    return


@app.cell
def _():
    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt
    return np, plt, stats


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Watch how changing the mean and standard deviation effects the pdf""")
    return


@app.cell
def _(mo):
    mu = mo.ui.slider(-5, 5, label = r"$\mu$")
    mu
    return (mu,)


@app.cell
def _(mo):
    sigma = mo.ui.slider(0.2, 10, label =r"$\sigma$")
    sigma
    return (sigma,)


@app.cell
def _(mo, mu, sigma):
    mo.md(f"""The mean $\mu$ = **{mu.value}**, std. dev. $\sigma$ = **{sigma.value}**""")
    return


@app.cell
def _(mu, np, plt, sigma, stats):
    x = np.linspace(-40, 40, 1000)
    plt.plot(x, stats.norm.pdf(x, mu.value, sigma.value))
    return


if __name__ == "__main__":
    app.run()
