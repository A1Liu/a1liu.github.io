---
title: Sorting Objects into Ordered Equivalence Classes
categories: [algorithms]
tags: [fun, algorithms]
published: false
---
Problem: sort an arbitrary list of values into an ordered list of equivalence classes.
I.e. if the input is:

```
[ 1, 2, 4, 6, 3, 2, 1, 3, 4, 4, 7, 3, 4 ]
```

Then the output should be:

```
[
   [ 1, 1 ],
   [ 2, 2 ],
   [ 3, 3, 3 ],
   [ 4, 4, 4, 4 ],
   [ 6 ],
   [ 7 ],
]
```

How to do?

## Naive Algorithms

1. Sort first, then linearly scan over into classes $$O(nlog(n)) + O(n)$$
2. Scan into classes first, then sort classes: $$O(nc) + O(clog(c))$$

<!-- {% raw %} -->
<!-- {% include refc-small.html text="ref commit" commit="3cad965..." %} -->
<!-- {% include ref-commit.html text="ref commit" commit="3cad965..." %} -->
<!-- {% endraw %} -->
