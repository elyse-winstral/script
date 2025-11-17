# Conditional Probability

## Introductory example

Let $A$ and $B$ be two events in $(\Omega, \mathcal{F}, \mathbb{P})$. Let's consider a population: 
- $\Omega = $ a population ($|\Omega| = n$)
- $\mathcal{F} =  2^{\Omega}$
- $\mathbb{P}(E) = \frac{|E|}{|\Omega|}$, for any event $E \in \mathcal{F}$- the Laplace model



Furthermore, let $A$ represent the event "walks on average more than 10'000 steps a day" and $B$ represent "owns a dog". If we randomly sample $n$ people from the population and count the number of times $A$ has occured within the sample $n_A$, we know $\frac{n_a}{n} \approx \mathbb{P}(A)$.

Now let's imagine we've selected all the people in $B$. Let $\mathbb{P}(A|B)$ denote the probability of $A$ occuring given $B$ has occured. In our example corresponds to asking the question "what are the chances that a dog owner walks more than 10'000 steps on average", or "given that someone owns a dog, what is the probability that they get more than 10'000 steps a day?". What should $\mathbb{P}(A|B)$ be? Here we could consider the only population of dog owners who walk 10'000+ steps $n_{A \cap B}$ and compare that number with the dog owner population $n_B$. 

$$
\frac{n_{A \cap B}}{n_B} = \frac{n_{A \cap B}/n}{n_B/n} \approx \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
$$

## Definition
<div id="def:cond-prob"> </div>

> **Conditional Probability:**
> Let $A$ and $B$ be two events in $(\Omega, \mathcal{F}, \mathbb{P})$, and $\mathbb{P}(B) > 0$. The conditional probability of $A$ given $B$ is given by 
>
>$$
>\begin{equation}
>\mathbb{P}(A|B) := \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
>\end{equation}
>\tag{1}
>$$


<div id="lemma:cond-prob-prob"> </div>

**Lemma:** For every set $B \in \mathcal{F}$ s.t. $\mathbb{P}(B) >0 $, the map $\mathbb{P}(\cdot| B): \mathcal{F} \rightarrow [0,1]$ is a probability mass.  
*Proof:*  $\mathbb{P}(\cdot|B)$ inherits non-negativity, normality and sigma-additivity from $\mathbb{P}$.


This version of conditional probability is rather static- the probability is a fixed value depending on the event we condition on (here: $B$). Additionally, we can't condition on null sets, i.e. if $Y$ is a continuous r.v., we can't condition on $B = \{Y= y\}$. However, we can condition on all events in $\sigma(Y)$. Conditioning on $\sigma$-algebras allows for variable conditional probabilities. (The conditional probability is itself random)

<div id="def:cond-prob-sig-alg"> </div>

> **Conditional Probability wrt $\sigma$-algebras:**
> The conditional probability of $A \in \mathcal{F}$ given $\mathcal{G} \subseteq \mathcal{F}$ is the almost surely unique, $\mathcal{G}$-measurable r.v. $\mathbb{P}(A|\mathcal{G})$ s.t.
> 
>$$
>\begin{equation}
>\mathbb{E}(\mathbb{P}(A|\mathcal{G})\mathbb{1}_B) = \mathbb{P}(A \cap B), \quad \forall B \in\mathcal{G}
>\end{equation}
>\tag{2}
>$$

The [conditioned event defintion](#def:cond-prob) is simply a special case of this definition where $\mathcal{G} = \{\emptyset, B, B^c, \Omega \}$. We get: 
$$
\mathbb{P}(A|\mathcal{G}) = \mathbb{P}(A|B)\mathbb{1}_B + \mathbb{P}(A|B^c) \mathbb{1}_{B^c}
$$
Equivalently stated: 
$$
\mathbb{P}(A|\mathcal{G}) = 
\begin{cases}
    \begin{aligned}
        &\mathbb{P}(A|B) \quad &&\text{if }B \text{ occurs, i.e. with probability } \mathbb{P}(B) \\
        &\mathbb{P}(A|B^c) \quad &&\text{if }B^c \text{ occurs, i.e. with probability } \mathbb{P}(B^c)
    \end{aligned}
\end{cases} \\
$$
Explicitly, the connection between (2) and (1) can be demonstrated:
$$
\mathbb{E}(\mathbb{P}(A|\mathcal{G})\mathbb{1}_B) = \int_{\Omega} \mathbb{P}(A|\mathcal{G}) \mathbb{1}_B d\mathbb{P} = \int_B \mathbb{P}(A|B)d\mathbb{P} = \mathbb{P}(A|B)\mathbb{P}(B) = \mathbb{P}(A \cap B)
$$

As mentioned above, we can condition on the $\sigma$-algebra $\sigma(Y)$ for a rv $Y:\Omega \rightarrow \Omega'$. The conditional probability $\mathbb{P}(X \in A|Y) = \mathbb{P}(X \in A|\sigma(Y))$ gives the probability of an outcome of $X$ given prior knowledge of $Y$. The value of this conditional probability depends on the outcome of $Y$, in fact $\mathbb{P}(X \in A|Y)$ is $\sigma(Y)$ measurable and can be understood as a transformation of $Y$. This probability function can be calculated from the joint and marginal probabilities:


<div id="def:cond-prob-rvs"> </div>


> For $X$, $Y$, and $(X,Y)$ **discrete random variables** with probability functions $f_X$, $f_Y$, $f_{X,Y}$ the conditional probability is given as: 
>$$
>\begin{equation}
> \mathbb{P}(X \in A | Y) = \sum_{x \in A} f_{X|Y}(x,Y) \quad \text{ where }  f_{X|Y}(x,y) := \frac{f_{X,Y}(x,y)}{f_Y(y)}
>\end{equation}
>\tag{3}
>$$
>
> For $X$, $Y$, and $(X,Y)$ **continuous random variables** with probability density functions $f_X$, $f_Y$, $f_{X,Y}$ the conditional probability is given as: 
>$$
>\begin{equation}
> \mathbb{P}(X \in A | Y) = \int_{A} f_{X|Y}(x,Y) dx \quad \text{ where }  f_{X|Y}(x,y) := \frac{f_{X,Y}(x,y)}{f_Y(y)}
>\end{equation}
>\tag{4}
>$$

To illustrate and reiterate the relationship between $Y$, $\sigma(Y)$ and the respective conditional probability consider the following example: 

&nbsp; &nbsp; Given a fair die, $X$ represents whether the outcome was an even number: 
$$
X = 
\begin{cases}
    \begin{align*}
        & E \quad &&\text{if we roll an even number}\\
        & O \quad &&\text{if we roll and odd number} \\
    \end{align*}
\end{cases}
$$
&nbsp; &nbsp; and $Y$ is given as follows $Y: \{1,2,3,4,5,6\} = \Omega \rightarrow \Omega' \supseteq A \cup B \cup C$
$$
Y = 
\begin{cases}
    \begin{align*}
        & A \quad &&\text{if we roll } 1 \\
        & B \quad &&\text{if we roll } 2 \text{ or } 3 \\
        & C \quad &&\text{for any other outcome}
    \end{align*}
\end{cases}
\\
\begin{align*}
\sigma(Y) &= \sigma\{\underbrace{\{1\}}_{Y^{-1}(A)}, \underbrace{\{2,3\}}_{Y^{-1}(B)}, \underbrace{\{4,5,6\}}_{Y^{-1}(C)}, \underbrace{\{1,2,3\} }_{Y^{-1}(A \cup B)}, \underbrace{\{1,4,5,6\} }_{Y^{-1}(A \cup C)}, \underbrace{\{2,3,4,5,6\} }_{Y^{-1}(B \cup C)}, \underbrace{\emptyset}_{Y^{-1}(\emptyset)}, \underbrace{\Omega }_{Y^{-1}(A \cup B \cup C)}\} 
\\
&= \{\{1\}, \{2,3\}, \{4,5,6\},\{1,2,3\}, \{1,4,5,6\},\{2,3,4,5,6\}, \emptyset, \Omega\}
\end{align*} 
$$
&nbsp; &nbsp; Now consider the joint probability function:
$$
f_{X,Y} = \begin{cases}
    \begin{align*}
        & 0 \quad && (x,y) = (E, A) \\
        & 1/6 \quad && (x,y) = (O, A) \\
        & 1/6 \quad && (x,y) = (E, B) \\
        & 1/6 \quad && (x,y) = (O, B) \\
        & 1/3 \quad && (x,y) = (E, C) \\
        & 1/6 \quad && (x,y) = (O, C) \\
    \end{align*}
\end{cases}
$$
&nbsp; &nbsp; This allows us to determine the conditional probability function: 
$$
f_{X|Y} = \begin{cases}
    \begin{align*}
        & 0 \quad && (x,y) = (E, A) \\
        & 1 \quad && (x,y) = (O, A) \\
        & 1/2 \quad && (x,y) = (E, B) \\
        & 1/2 \quad && (x,y) = (O, B) \\
        & 2/3 \quad && (x,y) = (E, C) \\
        & 1/3 \quad && (x,y) = (O, C) \\
    \end{align*}
\end{cases}
$$

&nbsp; &nbsp; And finally, what is the probability that $X = E$ given $Y$?
$$
\begin{align*}
\mathbb{P}(X = E | \sigma(Y)) &= f_{X|Y}(E, Y) \\
&= \overbrace{\mathbb{P}(X = E | Y = A)}^{f_{X|Y}(E,A)}\mathbb{1}_{Y = A} + \mathbb{P}(X = E | Y = B)\mathbb{1}_{Y = B} + \mathbb{P}(X = E | Y = C)\mathbb{1}_{Y = C}\\
&= 0 + 1/2 \cdot \mathbb{1}_{Y = B} + 2/3 \cdot \mathbb{1}_{Y = C}
\end{align*}
$$