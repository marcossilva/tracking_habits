# Interpretable Drug Response Prediction using a Knowledge-based Neural Network

https://dl.acm.org/doi/abs/10.1145/3447548.3467212

This approach builds a neural network where:
* Each node has meaning in its own layer
* Each known relation has its known weight
* Non-known relations exists but have learned weights and uses droupout as a strong regularization on those conections
* This built network specifically for this problem caried knowledge built-in and has shown better performance than a fully connected network
* This solution can be seen as a n-partite graph where there's meaning flowing in each partition