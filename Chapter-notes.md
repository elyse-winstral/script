# Additional sources
## insert some additional information about probability theory to see how well copilot can answer questions

Definition 23.4. Let $ Y \in L^2(\Omega, \mathcal{A}, P). Then the conditional expectation of $Y$ given $X$ is the unique element $\hat{Y}$ in $L^2(\Omega, \sigma (X), P)$ such that
$$
\begin{align}
    E\{\hat{Y}Z\} = E\{YZ\} \quad \text{ for all } Z \in L^2(\Omega, \sigma (X), P)
    \label{eq:cond_exp_rv}
\end{align}
$$
We write 
$$
E\{Y | X\}
$$
for the conditional expectation of $Y$ given $X$, namely $\hat{Y}$.

Note that $\hat{Y}$ is simply the Hilbert space projection of $Y$ on the closed linear subspace $L^2(\Omega, \sigma (X), P)$ of $L^2(\Omega, \mathcal{A}, P)$.
Observe that since $E\{Y|X\}$ is $\sigma(X)$ measurable, by Theorem 23.2 there exists a Borel measure $f$ sucht that  $E\{Y|X\} = f(X)$. Therefore $\eqref{eq:cond_exp_rv}$ is equivalent to:
$$
\begin{align}
    E\{f(X)g(X)\} = E\{Yg(X)\} 
\end{align}
$$
for each Borel $g$ such that $g(X) \in L^2$.
