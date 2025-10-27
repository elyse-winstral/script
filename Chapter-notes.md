# Additional sources
## insert some additional information about probability theory to see how well copilot can answer questions

(Taken from Probability Essentials, Protter)

Definition 23.4. Let $Y \in L^2(\Omega, \mathcal{A}, P). Then the conditional expectation of $Y$ given $X$ is the unique element $\hat{Y}$ in $L^2(\Omega, \sigma (X), P)$ such that
$$
\begin{aligned}
    E\left{\hat{Y}Z\right} = E\left{YZ\right} \quad \text{ for all } Z \in L^2(\Omega, \sigma (X), P)
    \label{eq:cond_exp_rv}
\end{aligned}
$$
We write 
$$
E\left{Y | X\right}
$$
for the conditional expectation of $Y$ given $X$, namely $\hat{Y}$.

Note that $\hat{Y}$ is simply the Hilbert space projection of $Y$ on the closed linear subspace $L^2(\Omega, \sigma (X), P)$ of $L^2(\Omega, \mathcal{A}, P)$.
Observe that since $E\left{Y|X \right}$ is $\sigma(X)$ measurable, by Theorem 23.2 there exists a Borel measure $f$ sucht that  $E\left{Y|X\right} = f(X)$. Therefore $\eqref{eq:cond_exp_rv}$ is equivalent to:
$$
\begin{aligned}
    E\left{f(X)g(X)\right} = E\left{Yg(X)\right} 
\end{aligned}
$$
for each Borel $g$ such that $g(X) \in L^2$.
