# Conditional Expectation

## Introduction
As seen in the [previous section](Conditional_Probability.md#definitions), the conditional probability $\mathbb{P}(A | B)$ corresponds to reducing our event space $\Omega$ to the event $B \in \Omega$, and then analyzing the probability of the event $A$ under this condition. Our goal is to extend the notion of conditional probability to conditional expectation (of a random variable $X$). In words: "What is the average of $X$ given that $B$ occurs? Or, what do we expect of $X$ given information about another random variable $Y$?". 

By the [lemma](Conditional_Probability.md#lemma) in the conditional probability section we know:

$$
\begin{align*}
\sum \mathbb{P}(X = x | A) &= 1 \\
\forall x: \mathbb{P}(X = x  | A) &\geq 0
\end{align*}
$$

These two properties ensure that $X|A$ is a random variable with probability measure $\mathbb{P}(\cdot | A)$, and $\mathbb{E}(X|A)$ exists (as long as $\sum_x x \mathbb{P} (X = x | A)$ converges). 

## Definitions

> #### Conditional Expectation - Events:
> The conditional expectation of a random variable given an event A with $\mathbb{P}(A) > 0$ is: 
>
> $$
> \mathbb{E}(X | A) = \frac{\mathbb{E}(X\mathbb{1}_A)}{\mathbb{P}(A)}
> $$
>
> This is exactly the expectation of $X$ using the probability measure $\mathbb{P}(\cdot | A)$


We can take $A$ to be any event, for example the outcome of another random variable $\mathbb{E}(X | Y = y)$. Now our goal is to extend this to random variables, denoted $\mathbb{E}(X | Y)$.


### Example (Motivation)
If $Y$ is a discrete random variable, we can view $\mathbb{E}(X | Y)$ in terms of outcomes of $Y$ i.e. 

$$ 
\mathbb{E}(X | Y) =  \begin{cases}
    \mathbb{E}(X | Y = y_1), \quad \text{given $y_1$ occurs}\\
    \mathbb{E}(X | Y = y_2), \quad \text{given $y_2$ occurs} \\
    \vdots
\end{cases} \qquad y_1, y_2, \ldots \in Y(\Omega)
$$

Note, the first case $\mathbb{E}(X | Y = y_1)$ is the value of the conditional expectation if ${Y = y_1}$ occurs, i.e. the event $\lbrace\mathbb{E}(X | Y) = \mathbb{E}(X | Y = y_1)\rbrace$ has probability $\mathbb{P}(Y = y_1)$. (Assume $\mathbb{E}(X | Y = y_k)$ is unique for each $y_k$)

The example illuminates an important property: $\mathbb{E}(X | Y)$ can be written as a function of $Y$ and thus inherits the randomness from $Y$. The conditional expectation given a random variable is thus another random variable. It should be noted the randomness from $X$ is averaged out.

$$
\begin{align*}
    g(Y) &:=  \mathbb{E}(X | Y)\\
    \mathbb{P}(g(Y) = g(y)) = \mathbb{P}(\mathbb{E}(X|Y) &= \mathbb{E}(X|Y=y))  = \sum_{k: \: \mathbb{E}(X|Y=k) = \mathbb{E}(X|Y=y)} \mathbb{P}(Y = k)
\end{align*}
$$

Recall, $g(Y)$ is $\sigma(Y)$-measurable for any measurable function $g$.

> #### Conditional Expectation - Random Variables
>For discrete random variables $X$, $Y$, $(X, Y)$ with probability functions $f_X$, $f_Y$, $f_{(X,Y)}$, the conditional expectation is 
>
>$$
>\mathbb{E}(X | Y) = \sum_x x f_{X | Y}(x, Y), \quad \text{where } \quad  f_{X | Y}(x, y) := \frac{f_{(X,Y)}(x,y)}{f_Y(y)}
>$$
>
>For continuous random variables we consider the density functions $f_X$, $f_Y$, $f_{(X,Y)}$, and analogously get
>
>$$
>\mathbb{E}(X | Y) = \int x f_{X | Y}(x, Y) dx, \quad \text{where } \quad  f_{X | Y}(x, y) := \frac{f_{(X,Y)}(x,y)}{f_Y(y)}
>$$


### Example - dice
&nbsp; &nbsp; Given a fair die, $X$ represents whether the outcome was an even number: 

$$
X = 
\begin{cases}
    \begin{align*}
        & 1 \quad &&\text{if we roll an even number}\\
        & 0 \quad &&\text{if we roll an odd number} \\
    \end{align*}
\end{cases}
$$

&nbsp; &nbsp; and $Y$ is given as follows $Y:\lbrace 1,2,3,4,5,6\rbrace = \Omega \rightarrow \Omega' \ni 10,20,30 $ 

$$
Y = 
\begin{cases}
    \begin{align*}
        & 10 \quad &&\text{if we roll } 1 \\
        & 20 \quad &&\text{if we roll } 2 \text{ or } 3 \\
        & 30 \quad &&\text{for any other outcome}
    \end{align*}
\end{cases}
$$

What is $\mathbb{E}(X | Y)$? Recall from the [example](Conditional_Probability.md#example---dice) in the conditional probability chapter: 

$$
f_{X|Y} = \begin{cases}
    \begin{align*}
        & 0 \quad && (x,y) = (1, 10) \\
        & 1 \quad && (x,y) = (0, 10) \\
        & 1/2 \quad && (x,y) = (1, 20) \\
        & 1/2 \quad && (x,y) = (0, 20) \\
        & 2/3 \quad && (x,y) = (1, 30) \\
        & 1/3 \quad && (x,y) = (0, 30) \\
    \end{align*}
\end{cases} 
$$

$$
\mathbb{E}(X|Y) = \sum_{x \in \lbrace 0, 1\rbrace} x f_{X|Y}(x,Y) = 0 f_{X|Y}(0,Y) + 1f_{X|Y}(1,Y) \\
= \begin{cases}
\begin{align*}
0 & \quad \text{if } & Y = 10 \\
1/2 & \quad \text{if } & Y = 20 \\
2/3 & \quad \text{if } & Y = 30
\end{align*}
\end{cases}
$$

This is, as mentioned earlier a random variable. So, we can also ask what is the expecatation of the conditional expectation $\mathbb{E}(\mathbb{E}(X|Y))$? The conditional expectation is a function of the conditioned variable ($\mathbb{E}(X|Y) = g(Y)$ for some measurable function $g$). 

$$
\begin{align*}
\mathbb{E}(\mathbb{E}(X|Y)) &= \mathbb{E}(g(Y)) = \sum_{y \in \lbrace 10, 20, 30 \rbrace} g(y) P(Y = y)\\ 
&= 0 P(Y=10) + 1/2 P(Y=20) + 2/3 P(Y=30) \\
&= 1/2 \cdot 1/3 + 2/3 \cdot 1/2 = 1/2
\end{align*}
$$

Interestingly, this is exactly $\mathbb{E}(X)$. This isn't a coincidence. Later, we'll look at this property in more detail.

We see there is some exchange of information happening between $X$ and $Y$. For example, if $Y = 10$, we know $X$ must be $0$. Is there a way to transform $Y$ (i.e. $g(Y)$) such that we can get the most amount of information about $X$? 

### Example - Doctor appointments and age
MAKE A MARIMO NOTEBOOK

## Conditional Expectation - $\sigma$-algebras
Analogously to conditional probability, conditonal expectation wrt. random variables are a special case of conditional expectation wrt. $\sigma$-algebras. The notation $\mathbb{E}(X|Y)$ is again another way of writing $\mathbb{E}(X|\sigma(Y))$. $X$ may not be $\sigma(Y)$ measurable. Going back to the dice example, we see exactly this situation:

$$
\lbrace X = 1 \rbrace = \lbrace 2,4,6 \rbrace \notin \sigma(Y) = \\
\lbrace\lbrace1\rbrace  ,\lbrace2,3\rbrace  ,\lbrace4,5,6\rbrace  ,\lbrace1,2,3\rbrace  ,\lbrace1,4,5,6\rbrace  ,\lbrace2,3,4,5,6\rbrace  , \emptyset, \Omega\rbrace  
$$

To formalize matters, let $(\Omega, \mathcal{F}, P)$ be a probability space, and $X : \Omega \rightarrow \mathbb{R}^n$ a random variable. 
Let's only consider variables that are square integrable: $\mathbb{E}(X^2)  < \infty$. If we identify all the rvs that are equal almost surely, we get the $L^2(\Omega, \mathcal{F}, P)$ space. By defining an inner product (or scalar product) as:

$$
\langle X, Y\rangle = \mathbb{E}(XY) 
$$

We get a Hilbert space. A Hilbert Space is a generalization of Euclidean space, and because it has an inner product, we can have orthogonality:

$$
\langle X,  Y\rangle = 0
$$

Because $\sigma(X) \subset \mathcal{F}$, $L^2(\Omega, \sigma(X), P)$ is a (closed) Hilbert subspace of  $L^2(\Omega, \mathcal{F}, P)$ (with the same inner product). 

> #### Conditional expectation 
> The conditional expectation of $X$ given $Y$ is the unique element in $L^2(\Omega, \sigma(Y), P)$ such that: 
>
> $$
> \begin{align*}
> \mathbb{E}(p(X) Z) &= \mathbb{E}(X Z) & \\
> \langle p(X), Z \rangle &= \langle X, Z \rangle    \quad &\forall Z \in L^2(\Omega, \sigma(Y), P)
> \end{align*}
> $$
>
> Where we write $p(X) = \mathbb{E}(X | Y)$. 

Hence, the conditional expectation is the **orthogonal projection** onto the subspace of $\sigma(Y)$ measurable random variables. More generally put, the conditional expectation is the orthogonal projection onto the subspace of $\mathcal{G}$ - measurable random variables. We can see the orthogonal projection fulfills the definitive property of conditional expectation. 

This notebook provides an example of what the conditional expectation can look like. [Here](https://elyse-winstral.github.io/script/conditional_expectation_sigma_algebra.html)

### Tower Property
For any event $B \in \mathcal{G}$, the conditional expectation is by definition the almost surely unique solution to: 

$$
\mathbb{E}( \mathbb{E}(X | \mathcal{G}) \mathbb{1}_B) = \mathbb{E}( X \mathbb{1}_B)
$$

### Example - trivial $\sigma$-algebra
Let $\mathcal{G} = \{\emptyset, \Omega \}$. We know: 

$$
\mathbb{E}( \mathbb{E}(X | \mathcal{G}) \mathbb{1}_B) = \mathbb{E}( X \mathbb{1}_B) \quad \forall B \in \mathcal{G}
$$

So take $\Omega \in \mathcal{G}$

$$
\mathbb{E}( \mathbb{E}(X | \mathcal{G}) \mathbb{1}_\Omega) = \mathbb{E}( X \mathbb{1}_\Omega) = \mathbb{E}(X)
$$

For $\emptyset$:  

$\mathbb{E}(X \mathbb{1}_\emptyset) = \mathbb{E}( \mathbb{E}(X) \mathbb{1}_{\emptyset})$ arbitrarily ($P(\mathbb{1}_{\emptyset} = 1) = 0$). 

Therefore, $\mathbb{E}(X | \mathcal{G}) = \mathbb{E}(X)$.

This motivates the tower properties:

$$
\mathbb{E}(\mathbb{E}(X | \mathcal{G})) = \mathbb{E}(X), \qquad \mathbb{E}(\mathbb{E}(X | \mathcal{G}) | \mathcal{G}) = \mathbb{E}(X | \mathcal{G})
$$

The second tower property in terms of projections can be thought of as: the projection of the projection is the simple projection. 

### Non-Linear Regression
Oftentimes, we want to use collected data to estimate the another dataset, for example using age to predict how often someone visits the doctor. We consider $(X,Y)$, $Y \in L^2(\Omega)$ with the goal: use $X$ to approximate $Y$. (In supervised learning, we work with the empirical distribution of a sample $(X_1, Y_1), \dots, (X_n, Y_n)$) We define an expected loss function:

$$
\mathbb{E}((Y - g(X))^2)
$$

by which we can quantify $X$-approximations of $Y$, $g(X)$. In other words, we wish to solve the following minimization problem:

$$
\underset{g \text{ meas.}}{\text{min}} \mathbb{E}((Y - g(X))^2)
$$

$g(X)$ are exactly the $\sigma(X)$ measurable random variables. The best approximation is the orthgonal projection of $Y$ onto the $\sigma(X)$ random variables, thus $g(X) = \mathbb{E}(Y|X)$:

$$
\begin{align*}
\mathbb{E}((Y - g(X))^2) &\\ 
&= \mathbb{E}((Y - \mathbb{E}(Y|X))^2) + \mathbb{E}((\mathbb{E}(Y|X) - g(X))^2) \\
& + 2\mathbb{E}(Y - \mathbb{E}(Y|X))(\mathbb{E}(Y|X) - g(X))\\
\end{align*}
$$

Using the tower property, we can show the last term is equal to zero. Then it follows directly that the minimizer $g_{\text{min}}$ is the conditional expectation $\mathbb{E}(X|Y)$.





