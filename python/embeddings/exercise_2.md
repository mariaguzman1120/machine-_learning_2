What do you think is the best distance criterion to estimate how far two embeddings(vectors)are from each other? Why?
-

The best way to choose a distance criterion for a particular application is to experiment with different metrics and see which one performs best. However, the following general guidelines may be helpful:

If the embeddings are dense and the relationships between the different dimensions are relatively simple, then Euclidean distance is often a good choice.
If the embeddings are sparse or the relationships between the different dimensions are more complex, then Manhattan distance may be a better choice.
If the embeddings are normalized and the relationships between the different dimensions are directional, then cosine distance may be a better choice.
The nature of the data: Some distance criteria are better suited for certain types of data than others. For example, cosine distance is often a good choice for text data, while Euclidean distance is often a good choice for image data.
The task at hand: The distance criterion should be chosen in a way that is appropriate for the task at hand. For example, if the goal is to cluster embeddings, then a distance criterion that is sensitive to the spatial relationships between the embeddings may be preferred.
Computational efficiency: Some distance criteria are more computationally efficient than others. This is important to consider if the distance criterion will be used in a large-scale application.


