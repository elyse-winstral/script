# Additional sources
## insert some additional information about probability theory to see how well copilot can answer questions

(Taken from Probability Essentials, Protter)

### Definition 23.4

Let $Y \in L^2(\Omega, \mathcal{A}, P)$.  
Then the conditional expectation of $Y$ given $X$ is the unique element $\hat{Y}$ in $L^2(\Omega, \sigma(X), P)$ such that

$$
E[\hat{Y}Z] = E[YZ] \quad \text{for all } Z \in L^2(\Omega, \sigma(X), P)
$$

We write $E[Y \mid X]$ for the conditional expectation of $Y$ given $X$, namely $\hat{Y}$.

---

Note that $\hat{Y}$ is simply the Hilbert space projection of $Y$ on the closed linear subspace $L^2(\Omega, \sigma(X), P)$ of $L^2(\Omega, \mathcal{A}, P)$.  
Observe that since $E[Y|X]$ is $\sigma(X)$-measurable, by Theorem 23.2 there exists a Borel function $f$ such that $E[Y|X] = f(X)$.  
Therefore the defining property is equivalent to:

$$
E[f(X)g(X)] = E[Yg(X)]
$$

for each Borel $g$ such that $g(X) \in L^2$.


