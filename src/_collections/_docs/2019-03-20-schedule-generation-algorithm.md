---
title: Schedule Generation Algorithm
categories: [bugs-nyu, yacs]
tags: [ideas, algorithms]
---
Right now at YACS I'm working on getting a system in place for prerequisites, and
also trying to build a course schedule resolver, i.e. a program that can tell me
which classes don't conflict with my schedule. While probably not entirely relevant,
there's a much harder problem, that of generating potential combinations of classes
from an arbitrary list. This problem is a lot harder, and a lot more interesting to
me. I'm going to be documenting my process as I try to design an algorithm to solve
it.

### Setup
First, some terminology. Let $$S$$ denote a set of $$n$$ schedules,
$$\left\{ s_1, s_2, \ldots s_n \right\}$$, where each schedule is a set of ordered
pairs $$(b, f)$$, with $$b,f \in \mathbb{N}$$. For all $$s \in S$$, each pair $$(b, f) \in s$$
represents a single *event* in the schedule. We call a schedule $$s$$ **invalid** if either
of the following are true:

1. there exists some event $$(b, f) \in s$$ such that $$b > f$$
2. there exists some pair of events $$(b_1, f_1), (b_2, f_2) \in S$$ such that $$b_1 \leq f_2$$
and $$b_2 \leq f_1$$, i.e. the events overlap.

A schedule is valid if it is not invalid.

Our question is *how can we find all possible valid schedules that are unions of
schedules in $$S$$?*

### Runtime of Schedule Validation
We can naively check the validity of some schedule $$s$$ with size $$m$$ by first making
sure $$b \leq f$$ for all $$(b, f) \in s$$, and then comparing each event in $$s$$
to all other events in $$s$$, i.e. $$\dfrac{m(m+1)}{2}$$ comparisons. This naive
implementation runs in $$O(m^2)$$ time.

We can lower that to $$O(m\log m)$$ by sorting the events by their begin times (the $$b$$).
Then for the $$i^{th}$$ event in the sorted sequence of events, $$e_i = (b_i, f_i)$$,
we do a binary search through the start times of events $$e_{i}, e_{i+1}, \ldots e_{m}$$
for the time that is less than or equal to $$f_i$$ with the greatest possible index.
If we find something besides $$e_i$$, or don't find anything, then schedule $$s$$ is invalid.

Since we do a binary search $$m$$ times, this runs in $$O(m\log m)$$ time.


