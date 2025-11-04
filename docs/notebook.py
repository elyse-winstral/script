import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


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
