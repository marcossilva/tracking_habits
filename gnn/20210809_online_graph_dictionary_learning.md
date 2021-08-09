# Online Graph Dictionary Learning

https://arxiv.org/pdf/2102.06555.pdf

The excerpt below points out an interesting discussion that I could take to my thesis.

> As opposed to recent approaches focusing on
dynamically varying graphs in online or continuous learning
(Yang et al., 2018; Vlaski et al., 2018; Wang et al., 2020),
we rather suppose in this work that distinct graphs are made
progressively available (Zambon et al., 2017; Grattarola
et al., 2019). This setting is particularly challenging as
the structure, the attributes or the number of nodes of each
graph observed at a time step can differ from the previous
ones. We propose to tackle this problem by learning a linear
representation of graphs with online dictionary learning

> Dictionary Learning (DL) Dictionary Learning (Mairal
et al., 2009; Schmitz et al., 2018) is a field of unsupervised
learning that aims at estimating a linear representation of
the data, i.e. to learn a linear subspace defined by the span
of a family of vectors, called atoms, which constitute a
dictionary. These atoms are inferred from the input data by
minimizing a reconstruction error. These representations
have been notably used in statistical frameworks such as
data clustering (Ng et al., 2002), recommendation systems
(Bobadilla et al., 2013) or dimensionality reduction (Candes`
et al., 2011). (...) We
also consider the dynamic or time varying version of the
problem, where the data generating process may exhibit
non-stationarity over time, yielding a problem of subspace
change or tracking (see e.g. (Narayanamurthy & Vaswani,
2018)), where one wants to monitor changes in the subspace
best describing the data. 

But after reading the article thoroughly there's not much that can be taken directly to recommender systems tasks.