# Best Model Identification: A Rested Bandit Formulation

http://proceedings.mlr.press/v139/cella21a/cella21a.pdf

>Multi-armed bandits are a mathematical framework of sequential decision problems that have played a fundamental
role in machine learning and statistics

Maybe this framework could be used to model the problems of suggested assests I've come up with?

>  This framework consists of a sequence of T interactions (or rounds)
between a learning agent and an unknown environment.
During each round the learner picks an action from a set of
options K, usually referred to as arms, and the environment
consequently generates a feedback (e.g., in the form of a
loss value) associated with the chosen action/pulled arm.

Maybe it could be modelled with the actions buy and do nothing and the feedback the earned money? It comes to my mind some possible approaches:

* Take each combination of recommended asset and recommendator as a separate possibility. The problem here is that the options chnge over time
* A simpler approach would be having the whole portifolio asset suggestion as an option to take or leave in each take. This way the percentage of money spent would be adjusted on the better performing asset portifolios over time
* Its possible to set different stop gain and stop losses on each portifolio as means to multiply the available inputs.

In the end reading the article inspired me but I didn't understand it largely.
