# CS229 Detailed Study Guide

## Chapter 1: Linear Regression
### Core Concepts
- **Overview:** 7 function h is called a hypothesis. Seen pictorially, the process is therefore like this: Training set house.) (living area of Learning algorithm h predicted y x...
### Key Technical Points
- **Gradient Descent:** Optimization algorithm for minimizing the cost function.

---

## Chapter 2: Classification and Logistic Regression
### Core Concepts
- **Overview:** 19 Here, the w(i)’s are non-negative valued weights. Intuitively, if w(i) is large for a particular value of i, then in picking θ, we’ll try hard to make ( y(i) − θT x(i))2 small. If w(i) is small, then the ( y(i) − θT x(i))2 error term will be pretty much ignored in the ﬁt. A fairly standard choice...
### Key Technical Points
- **Maximum Likelihood Estimation:** Method for estimating model parameters.

---

## Chapter 3: Generalized Linear Models
### Core Concepts
- **Overview:** 28 Lastly, in our logistic regression setting, θ is vector-valued, so we need to generalize Newton’s method to this setting. The generalization of Newton’s method to this multidimensional setting (also called the Newton-Raphson method) is given by θ := θ − H−1∇θℓ(θ). Here, ∇θℓ(θ) is, as usual, the v...
### Key Technical Points
- **Gradient Descent:** Optimization algorithm for minimizing the cost function.
- **Maximum Likelihood Estimation:** Method for estimating model parameters.

---

## Chapter 4: Generative Learning Algorithms
### Core Concepts
- **Overview:** 33 by µ; the third equality follows from Assumption 1 (and our earlier derivation showing that µ = η in the formulation of the Gaussian as an exponential family distribution); and the last equality follows from Assumption 3. 3.2.2 Logistic regression We now consider logistic regression. Here we are ...
### Key Technical Points

---

## Chapter 5: Kernel Methods
### Core Concepts
- **Overview:** 47 The parameters for our new model are φy = p(y) as before, φk|y=1 = p(xj = k|y = 1) (for any j) and φk|y=0 = p(xj = k|y = 0). Note that we have assumed that p(xj|y) is the same for all values of j (i.e., that the distribution according to which a word is generated does not depend on its position j...
### Key Technical Points
- **Gradient Descent:** Optimization algorithm for minimizing the cost function.
- **Maximum Likelihood Estimation:** Method for estimating model parameters.
- **The Kernel Trick:** Efficient computation in high-dimensional feature spaces.

---

## Chapter 6: Support Vector Machines
### Core Concepts
- **Overview:** 58 Application of kernel methods: We’ve seen the application of kernels to linear regression. In the next part, we will introduce the support vector machines to which kernels can be directly applied. dwell too much longer on it here. In fact, the idea of kernels has signiﬁcantly broader applicabilit...
### Key Technical Points
- **The Kernel Trick:** Efficient computation in high-dimensional feature spaces.

---

## Chapter 7: Deep Learning
### Core Concepts
- **Overview:** Part II Deep learning 79 Chapter 7 Deep learning We now begin our study of deep learning. In this set of notes, we give an overview of neural networks, discuss vectorization and discuss training neural networks with backpropagation. 7.1 Supervised learning with non-linear mod- els...
### Key Technical Points
- **Gradient Descent:** Optimization algorithm for minimizing the cost function.
- **Maximum Likelihood Estimation:** Method for estimating model parameters.
- **Backpropagation:** Algorithm for calculating gradients in neural networks.

---

## Chapter 8: Generalization
### Core Concepts
- **Overview:** Part III Generalization and regularization 112 Chapter 8 Generalization This chapter discusses tools to analyze and understand the generaliza- tion of machine learning models, i.e, their performances on unseen test examples. Recall that for supervised learning problems, given a train- ing dataset {(...
### Key Technical Points

---

## Chapter 9: Regularization and Model Selection
### Core Concepts
- **Overview:** 134 x x1 2 /0 /1 /0 /1 /0 /1 x x1 2...
### Key Technical Points
- **Gradient Descent:** Optimization algorithm for minimizing the cost function.
- **The Kernel Trick:** Efficient computation in high-dimensional feature spaces.

---

## Chapter 10: Clustering and K-means
### Core Concepts
- **Overview:** Part IV Unsupervised learning 144 Chapter 10 Clustering and the k-means algorithm In the clustering problem, we are given a training set {x(1), . . . , x(n)}, and want to group the data into a few cohesive “clusters.” Here, x(i) ∈ Rd as usual; but no labels y(i) are given. So, this is an unsupervise...
### Key Technical Points

---

## Chapter 11: EM Algorithms
### Core Concepts
- **Overview:** 147 J must monotonically decrease, and the value of J must converge. (Usu- ally, this implies that c and µ will converge too. In theory, it is possible for k-means to oscillate between a few diﬀerent clusterings—i.e., a few diﬀerent values for c and/or µ—that have exactly the same value of J, but th...
### Key Technical Points
- **Maximum Likelihood Estimation:** Method for estimating model parameters.

---

## Chapter 12: Principal Components Analysis
### Core Concepts
- **Overview:** 164 With this re-parameterization, we have that Ez(i)∼Qi [ log p(x(i), z(i); θ) Qi(z(i)) ] (11.25) = Eξ(i)∼N (0,1) [...
### Key Technical Points

---

## Chapter 13: Independent Components Analysis
### Core Concepts
- **Overview:** 170 of all possible orthogonal bases u1, . . . , uk, the one that we have chosen max- imizes ∑ i ∥y(i)∥2 2. Thus, our choice of a basis preserves as much variability as possible in the original data. PCA can also be derived by picking the basis that minimizes the ap- proximation error arising from p...
### Key Technical Points

---

## Chapter 14: Self-supervised Learning
### Core Concepts
- **Overview:** 176 where α is the learning rate. After the algorithm converges, we then compute s(i) = W x(i) to recover the original sources. Remark. When writing down the likelihood of the data, we implicitly as- sumed that the x(i)’s were independent of each other (for diﬀerent values of i; note this issue is d...
### Key Technical Points
- **Maximum Likelihood Estimation:** Method for estimating model parameters.

---

## Chapter 15: Reinforcement Learning
### Core Concepts
- **Overview:** 188 15.1 Markov decision processes A Markov decision process is a tuple ( S, A, {Psa}, γ, R), where: • S is a set of states. (For example, in autonomous helicopter ﬂight, S might be the set of all possible positions and orientations of the heli- copter.) • A is a set of actions. (For example, the se...
### Key Technical Points
- **Markov Decision Process (MDP):** Formal framework for modeling decision making in RL.

---

## Chapter 16: LQR, DDP and LQG
### Core Concepts
- **Overview:** 205 states. In the continuous case, we can rewrite the expectation as an integral. The notation s′ ∼ Psa means that the state s′ is sampled from the distribution Psa. 2. We’ll assume that the rewards depend on both states and actions. In other words, R : S × A → R. This implies that the previous mec...
### Key Technical Points
- **Markov Decision Process (MDP):** Formal framework for modeling decision making in RL.

---

## Chapter 17: Policy Gradient
### Core Concepts
- **Overview:** 219 We aim to use gradient ascent to maximize η(θ). The main challenge we face here is to compute (or estimate) the gradient of η(θ) without the knowledge of the form of the reward function and the transition probabilities. Let Pθ(τ) denote the distribution of τ (generated by the policy πθ), and let...
### Key Technical Points
- **Maximum Likelihood Estimation:** Method for estimating model parameters.

---

