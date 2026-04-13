# CS229: Machine Learning Full Course Guide

This guide contains both a high-level summary and a detailed study guide for each chapter.

## Chapter 1: Linear Regression

### Chapter Summary
7 function h is called a hypothesis. Seen pictorially, the process is therefore like this: Training set house.) (living area of Learning algorithm h predicted y x (predicted price) of house) When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression prob- lem. When y can take on only a small number of discrete values (such as...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.

---

## Chapter 2: Classification and Logistic Regression

### Chapter Summary
19 Here, the w(i)’s are non-negative valued weights. Intuitively, if w(i) is large for a particular value of i, then in picking θ, we’ll try hard to make ( y(i) − θT x(i))2 small. If w(i) is small, then the ( y(i) − θT x(i))2 error term will be pretty much ignored in the ﬁt. A fairly standard choice for the weights is 4 w(i) = exp ( −(x(i) − x)2 2τ 2 ) Note that the weights depend on the particular point x at which we’re trying to evaluate x. Moreover, if |x(i) − x| is small, then w(i) is close ...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.

---

## Chapter 3: Generalized Linear Models

### Chapter Summary
28 Lastly, in our logistic regression setting, θ is vector-valued, so we need to generalize Newton’s method to this setting. The generalization of Newton’s method to this multidimensional setting (also called the Newton-Raphson method) is given by θ := θ − H−1∇θℓ(θ). Here, ∇θℓ(θ) is, as usual, the vector of partial derivatives of ℓ(θ) with respect to the θi’s; and H is an d-by-d matrix (actually, d+1−by−d+1, assuming that we include the intercept term) called the Hessian, whose entries are given...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.

---

## Chapter 4: Generative Learning Algorithms

### Chapter Summary
33 by µ; the third equality follows from Assumption 1 (and our earlier derivation showing that µ = η in the formulation of the Gaussian as an exponential family distribution); and the last equality follows from Assumption 3. 3.2.2 Logistic regression We now consider logistic regression. Here we are interested in binary classiﬁ- cation, so y ∈ {0, 1}. Given that y is binary-valued, it therefore seems natural to choose the Bernoulli family of distributions to model the conditional dis- tribution o...

### Study Guide & Key Points
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.

---

## Chapter 5: Kernel Methods

### Chapter Summary
47 The parameters for our new model are φy = p(y) as before, φk|y=1 = p(xj = k|y = 1) (for any j) and φk|y=0 = p(xj = k|y = 0). Note that we have assumed that p(xj|y) is the same for all values of j (i.e., that the distribution according to which a word is generated does not depend on its position j within the email). If we are given a training set {(x(i), y(i)); i = 1 , . . . , n} where x(i) = (x(i) 1 , x(i) 2 , . . . , x(i) di ) (here, di is the number of words in thei-training example), the l...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Kernels:** Using the 'Kernel Trick' to map features into high-dimensional spaces efficiently via inner products.

---

## Chapter 6: Support Vector Machines

### Chapter Summary
58 Application of kernel methods: We’ve seen the application of kernels to linear regression. In the next part, we will introduce the support vector machines to which kernels can be directly applied. dwell too much longer on it here. In fact, the idea of kernels has signiﬁcantly broader applicability than linear regression and SVMs. Speciﬁcally, if you have any learning algorithm that you can write in terms of only inner products ⟨x, z⟩ between input attribute vectors, then by replacing this wit...

### Study Guide & Key Points
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.
- **Kernels:** Using the 'Kernel Trick' to map features into high-dimensional spaces efficiently via inner products.

---

## Chapter 7: Deep Learning

### Chapter Summary
Part II Deep learning 79 Chapter 7 Deep learning We now begin our study of deep learning. In this set of notes, we give an overview of neural networks, discuss vectorization and discuss training neural networks with backpropagation. 7.1 Supervised learning with non-linear mod- els In the supervised learning setting (predicting y from the input x), suppose our model/hypothesis is hθ(x). In the past lectures, we have considered the cases when hθ(x) = θ⊤x (in linear regression) or hθ(x) = θ⊤φ(x) (w...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.
- **Neural Networks:** Multi-layer architectures using non-linear activation functions and backpropagation for training.

---

## Chapter 8: Generalization

### Chapter Summary
Part III Generalization and regularization 112 Chapter 8 Generalization This chapter discusses tools to analyze and understand the generaliza- tion of machine learning models, i.e, their performances on unseen test examples. Recall that for supervised learning problems, given a train- ing dataset {(x(i), y(i))}n i=1, we typically learn a model hθ by minimizing a loss/cost function J(θ), which encourages hθ to ﬁt the data. E.g., when the loss function is the least square loss (aka mean squared er...

### Study Guide & Key Points
- **Bias-Variance Tradeoff:** Understanding the balance between underfitting and overfitting.

---

## Chapter 9: Regularization and Model Selection

### Chapter Summary
134 x x1 2 /0 /1 /0 /1 /0 /1 x x1 2 In order words, under the deﬁnition of the VC dimension, in order to prove that VC(H) is at least D, we need to show only that there’s at least one set of size D that H can shatter. The following theorem, due to Vapnik, can then be shown. (This is, many would argue, the most important theorem in all of learning theory.)...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.
- **Kernels:** Using the 'Kernel Trick' to map features into high-dimensional spaces efficiently via inner products.
- **Neural Networks:** Multi-layer architectures using non-linear activation functions and backpropagation for training.
- **Bias-Variance Tradeoff:** Understanding the balance between underfitting and overfitting.

---

## Chapter 10: Clustering and K-means

### Chapter Summary
Part IV Unsupervised learning 144 Chapter 10 Clustering and the k-means algorithm In the clustering problem, we are given a training set {x(1), . . . , x(n)}, and want to group the data into a few cohesive “clusters.” Here, x(i) ∈ Rd as usual; but no labels y(i) are given. So, this is an unsupervised learning problem. The k-means clustering algorithm is as follows: 1. Initialize cluster centroids µ1, µ2, . . . , µk ∈ Rd randomly. 2. Repeat until convergence: { For every i, set c(i) := arg min...

### Study Guide & Key Points
- **Unsupervised Learning:** Discovering patterns in unlabeled data (e.g., K-means, PCA).

---

## Chapter 11: EM Algorithms

### Chapter Summary
147 J must monotonically decrease, and the value of J must converge. (Usu- ally, this implies that c and µ will converge too. In theory, it is possible for k-means to oscillate between a few diﬀerent clusterings—i.e., a few diﬀerent values for c and/or µ—that have exactly the same value of J, but this almost never happens in practice.) The distortion function J is a non-convex function, and so coordinate descent on J is not guaranteed to converge to the global minimum. In other words, k-means ca...

### Study Guide & Key Points
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Unsupervised Learning:** Discovering patterns in unlabeled data (e.g., K-means, PCA).

---

## Chapter 12: Principal Components Analysis

### Chapter Summary
164 With this re-parameterization, we have that Ez(i)∼Qi [ log p(x(i), z(i); θ) Qi(z(i)) ] (11.25) = Eξ(i)∼N (0,1) [ log p(x(i), q(x(i); φ) + v(x(i); ψ) ⊙ ξ(i); θ) Qi(q(x(i); φ) + v(x(i); ψ) ⊙ ξ(i)) ] It follows that ∇φEz(i)∼Qi...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.

---

## Chapter 13: Independent Components Analysis

### Chapter Summary
170 of all possible orthogonal bases u1, . . . , uk, the one that we have chosen max- imizes ∑ i ∥y(i)∥2 2. Thus, our choice of a basis preserves as much variability as possible in the original data. PCA can also be derived by picking the basis that minimizes the ap- proximation error arising from projecting the data onto the k-dimensional subspace spanned by them. (See more in homework.) PCA has many applications; we will close our discussion with a few exam- ples. First, compression—representi...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Logistic Regression:** Used for classification, employing the sigmoid (logistic) function for probability mapping.

---

## Chapter 14: Self-supervised Learning

### Chapter Summary
176 where α is the learning rate. After the algorithm converges, we then compute s(i) = W x(i) to recover the original sources. Remark. When writing down the likelihood of the data, we implicitly as- sumed that the x(i)’s were independent of each other (for diﬀerent values of i; note this issue is diﬀerent from whether the diﬀerent coordinates of x(i) are independent), so that the likelihood of the training set was given by ∏ i p(x(i); W ). This assumption is clearly incorrect for speech data an...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Neural Networks:** Multi-layer architectures using non-linear activation functions and backpropagation for training.

---

## Chapter 15: Reinforcement Learning

### Chapter Summary
188 15.1 Markov decision processes A Markov decision process is a tuple ( S, A, {Psa}, γ, R), where: • S is a set of states. (For example, in autonomous helicopter ﬂight, S might be the set of all possible positions and orientations of the heli- copter.) • A is a set of actions. (For example, the set of all possible directions in which you can push the helicopter’s control sticks.) • Psa are the state transition probabilities. For each state s ∈ S and action a ∈ A, Psa is a distribution over the...

### Study Guide & Key Points
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Reinforcement Learning:** Modeling agents in environments using MDPs, value functions, and policy gradients.

---

## Chapter 16: LQR, DDP and LQG

### Chapter Summary
205 states. In the continuous case, we can rewrite the expectation as an integral. The notation s′ ∼ Psa means that the state s′ is sampled from the distribution Psa. 2. We’ll assume that the rewards depend on both states and actions. In other words, R : S × A → R. This implies that the previous mechanism for computing the optimal action is changed into π∗(s) = argmaxa∈A R(s, a) + γEs′∼Psa [ V π∗ (s′) ] 3. Instead of considering an inﬁnite horizon MDP, we’ll assume that we have a ﬁnite horizon M...

### Study Guide & Key Points
- **Reinforcement Learning:** Modeling agents in environments using MDPs, value functions, and policy gradients.

---

## Chapter 17: Policy Gradient

### Chapter Summary
219 We aim to use gradient ascent to maximize η(θ). The main challenge we face here is to compute (or estimate) the gradient of η(θ) without the knowledge of the form of the reward function and the transition probabilities. Let Pθ(τ) denote the distribution of τ (generated by the policy πθ), and let f(τ) = ∑T−1 t=0 γtR(st, at). We can rewrite η(θ) as η(θ) = Eτ∼Pθ [f(τ)] (17.2) We face a similar situations in the variational auto-encoder (VAE) setting covered in the previous lectures, where the w...

### Study Guide & Key Points
- **Optimization:** Focuses on Gradient Descent (Batch and Stochastic) to minimize the cost function $J(\theta)$.
- **Probabilistic Interpretation:** Uses Maximum Likelihood Estimation (MLE) to derive learning algorithms.
- **Neural Networks:** Multi-layer architectures using non-linear activation functions and backpropagation for training.
- **Bias-Variance Tradeoff:** Understanding the balance between underfitting and overfitting.
- **Reinforcement Learning:** Modeling agents in environments using MDPs, value functions, and policy gradients.

---

