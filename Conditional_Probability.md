# Conditional Probability

## Introductory example

Let $A$ and $B$ be two events in $(\Omega, \mathcal{F}, \mathbb{P})$. Let's consider a population: 
- $\Omega = $ a population ($|\Omega| = n$)
- $\mathcal{F} =  2^{\Omega}$
- $\mathbb{P}(E) = \frac{|E|}{|\Omega|}$, for any event $E \in \mathcal{F}$- the Laplace model



Furthermore, let $A$ represent the event "walks on average more than 10'000 steps a day" and $B$ represents "owns a dog". If we randomly sample $n$ people from the population and count the number of times $A$ has occured within the sample $n_A$, we know $\frac{n_A}{n} \approx \mathbb{P}(A)$.

Now let's imagine we've selected all the people in $B$. Let $\mathbb{P}(A|B)$ denote the probability of $A$ occuring given $B$ has occured. In our example corresponds to asking the question "what are the chances that a dog owner walks more than 10'000 steps on average", or "given that someone owns a dog, what is the probability that they get more than 10'000 steps a day?". What should $\mathbb{P}(A|B)$ be? We could consider only the population of dog owners who walk 10'000+ steps $n_{A \cap B}$ and compare that number with the dog owner population $n_B$. 

$$
\frac{n_{A \cap B}}{n_B} = \frac{n_{A \cap B}/n}{n_B/n} \approx \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
$$

## Definitions
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

The following notebook visualizes an example of [conditional probaility](https://elyse-winstral.github.io/script/cond_prob_widget.html). 
<!--
Referencing notebook: docs/cond_prob_widget.py
Source Notebook GitHub location: https://github.com/elyse-winstral/script/blob/main/docs/cond_prob_widget.py
-->



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

The [conditioned event definition](#def:cond-prob) is simply a special case of this definition where $\mathcal{G} = \{\emptyset, B, B^c, \Omega \}$. We get: 

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
>
>$$
>\begin{equation}
> \mathbb{P}(X \in A | Y) = \int_{A} f_{X|Y}(x,Y) dx \quad \text{ where }  f_{X|Y}(x,y) := \frac{f_{X,Y}(x,y)}{f_Y(y)}
>\end{equation}
>\tag{4}
>$$

To illustrate and reiterate the relationship between $Y$, $\sigma(Y)$ and the respective conditional probability consider the following example: 

### Example - dice
&nbsp; &nbsp; Given a fair die, $X$ represents whether the outcome was an even number: 

$$
X = 
\begin{cases}
    \begin{align*}
        & E \quad &&\text{if we roll an even number}\\
        & O \quad &&\text{if we roll an odd number} \\
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
$$\

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

&nbsp; &nbsp; And finally, what is the probability that $X = E$ given $Y$:  $\mathbb{P}(X=x|Y)$?

$$
\begin{align*}
\mathbb{P}(X = E | \sigma(Y)) &= \sum_{x \in \{2,4,6\}}f_{X|Y}(x|Y) = f_{X|Y}(E, Y) \\
&= \overbrace{\mathbb{P}(X = E | Y = A)}^{f_{X|Y}(E,A)}\mathbb{1}_{Y = A} + \mathbb{P}(X = E | Y = B)\mathbb{1}_{Y = B} + \mathbb{P}(X = E | Y = C)\mathbb{1}_{Y = C}\\
&= 0 + 1/2 \cdot \mathbb{1}_{Y = B} + 2/3 \cdot \mathbb{1}_{Y = C}
\end{align*}
$$

## Properties

<div id="thm:bayes"> </div>

**Bayes Theorem:** For events $A, B \in \mathcal{F}$ with positive probability, it holds:

$$
\begin{equation*}
    P(B|A) = \frac{P(A|B)P(B)}{P(A)}, \qquad f_{Y|X}(y,x) =\frac{f_{X|Y}(x,y)f_Y(Y)}{f_X(x)} 
\end{equation*}
$$

*Proof:* Directly follows from def. of conditional probability [(1)](#def:cond-prob):

$$
P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{P(A \cap B) P(B)}{P(B)P(A)} = \frac{P(A|B)P(B)}{P(A)}
$$

<div id="prop:indep"> </div>

**Independence:** Let $A, B$ be independent events. By definition this implies: 

$$
P(A|B) = \frac{P(A \cap B)}{P(B)} = P(A)
$$

In words: $B$ has no effect on $A$. Note: disjoint events and independent events are very different. The aforementioned [notebook](https://elyse-winstral.github.io/script/cond_prob_widget.html) shows an example of independent events. 
<!--
Referencing notebook: docs/cond_prob_widget.py
Source Notebook GitHub location: https://github.com/elyse-winstral/script/blob/main/docs/cond_prob_widget.py
-->
Random variables can also be independent: $X, Y$ independent (denoted: $X \perp Y$):

$$
P(X \in A | Y) = P(X \in A), \quad \forall A \in \mathcal{F}
$$


<div id="thm:tot-prob"> </div>

**Law of total probability:** Let $B_1, B_2, \dots, B_n$ be a partition of $\Omega$ (i.e. $B_1, B_2, \dots, B_n \in \mathcal{F}$ and $B_1 \sqcup \dots \sqcup B_n = \Omega$) with $P(B_i) > 0$ for $i = 1, \dots, n$. Then for every $A \in \mathcal{F}$:

$$
P(A) = \sum_{i=1}^{n}P(A|B_i)P(B_i)
$$

*Proof:* 
$A = (A \cap B_1) \sqcup \dots \sqcup (A \cap B_n)$, so:

$$
P(A) = P(A \cap B_1) + \dots + P(A \cap B_n)
$$

Applying [(1)](#def:cond-prob), we can write:

$$
P(A) = P(A|B_1)P(B_1) + \dots + P(A|B_n)P(B_n)
$$

## Examples

### COVID 19 test
A study assessed the accuracy of COVID-19 tests. To do so, they compare test results and actual COVID-19 cases. $T$ is the event of a positive test ($T^c$ means the test was negative), and $C$ is the event of an actual COVID-19 case. Their results are given in the table:


|                              | PCR test | Antigen Test  |
|------------------------------| ---------| ------------- |
| Sensitivity $\mathbb{P}(T\|C)$        | 80%      | 41%           |
| Specificity $\mathbb{P}(T^c \| C^c)$  | 99%      | 98%           |

**Recap- events vs $\sigma$-algebras:**

Conditioning on events gives real numbers i.e. for a PCR test with events $T$ and $C$:

$$
\begin{align*}
\mathbb{P}(T|C) = 80\%, \quad \mathbb{P}(T|C^c) = 1 - \mathbb{P}(T^c | C^c) = 1 \%
\end{align*}
$$

Conditioning on $\sigma$-algebras gives random variables i.e. let $X = \mathbb{1}_T$ and $Y = \mathbb{1}_C$:

$$
\mathbb{P}(X = 1| Y) = 80 \% \cdot \mathbb{1}_{1}(Y) + 1\% \cdot \mathbb{1}_{0}(Y)
$$

Now lets imagine we conduct a PCR Test during a wave of COVID-19- $10\%$ of the population is infected ($\mathbb{P}(C) = 10\%$). If the test comes back positive, the patient is sick with a probability of: 

$$
\begin{align*}
\mathbb{P}(C|T) &= \frac{\mathbb{P}(T|C)\mathbb{P}(C)}{\mathbb{P}(T)} = \frac{\mathbb{P}(T|C)\mathbb{P}(C)}{\mathbb{P}(T|C)\mathbb{P}(C) + \mathbb{P}(T|C^c)\mathbb{P}(C^c)}&& \\
&=\frac{0.8 \cdot 0.1}{0.8 \cdot 0.1 + 0.01 \cdot 0.9} &&\approx 90\%
\end{align*}
$$

However if we were to use an antigen test, the probability would only be around $69\%$.

### Binary symmetric channel

A sender $X$ sends a message-encoded as bits- over a communication channel to a receiver $Y$. The message can't be transmitted noiselessly: there is an $\varepsilon$ chance that the bit is received incorrectly: 

<img src="images/cond-prob-channel-ex.png" alt="drawing" width="800"/>

The probability of sending a $1$ is $P(X = 1) = \pi$ and the probability of sending a $0$ is $1-\pi$. What is the probability of receiving $1$ i.e. $P(Y = 1)$?

$$
\begin{align*}
    P(Y = 1) &= P(Y = 1| X = 1)P(X = 1) + P(Y = 1| X = 0)P(X = 0)\\
    &=(1-\varepsilon)\pi + \varepsilon(1-\pi)

\end{align*}
$$

The converse problem is also considered important namely, given the probability of receiving a $1$ what is the probability that $1$ was sent? If $\varepsilon$ is relatively small, the sender and receiver can agree on what bit was sent. This is called successful communication. Information theory deals with further questions such as how long a message should be to achieve arbitrarily low error and how many different messages can be sent (channel capacity) with low error.

### Normal Random Walk
Let $X_i \sim N(0,1)$ for  $i= 1, \dots, n$, iid and $Y_i = \sum_{k=1}^{i}X_k \sim N(0, i)$. What is $P(Y_i \in [-1,1] | Y_{i-1} = y)$?

$$
\begin{align*}
P(Y_i \in [-1,1]| Y_{i-1} = y) &= P(\sum_{k=1}^i X_k \in [-1,1] | \sum _{k=1}^{i-1} X_k = y) = P(X_i + Y_{i-1} \in [-1,1] | Y_{i-1} = y) \\
&= P(X_i \in [-1-Y_{i-1}, 1-Y_{i-1}]|Y_{i-1} = y))\\
&= P(X_i \in [-1-y, 1-y]|Y_{i-1} = y)  \\
&= P(X_i \in [-1-y, 1-y]) = F_X(1-y)- F_X(-1-y) 
\end{align*}
$$

There is no gain in considering states further in the past:

$$
\begin{align*}
P(Y_i \in [-1,1]| Y_{i-1} &= y, Y_{i-2} = z) = P(Y_i \in [-1,1]| Y_{i-2}=z, X_{i-1} = y-z) \\
&= P(Y_{i-2} + X_{i-1} + X_{i} \in [-1,1] | Y_{i-2}=z, X_{i-1} = y-z) \\
&= P(X_i \in [-1 - Y_{i-2} - X_{i-1}, 1 - Y_{i-2} - X_{i-1}] | Y_{i-2}=z, X_{i-1} = y-z) \\
&= P(X_i \in [-1 - z -(y-z), 1 - z-(y-z)] | Y_{i-2}=z, X_{i-1} = y-z) \\
&= P(X_i \in [-1 - y, 1-y])
\end{align*}
$$


