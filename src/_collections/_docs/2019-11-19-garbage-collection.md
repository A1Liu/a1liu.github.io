---
title: Garbage Collection
categories: []
tags: []
---
Garbage collection is fun and interesting. Lets talk about it.

## A Unified Theory Of Garbage Collection
This [theory of garbage collection][unifying-theory] introduces some formalism
in describing tracing and reference counting garbage collection algorithms, and
uses that formalism to create general formulas for collection runtime.

[unifying-theory]: https://www.researchgate.net/publication/221321424_A_unified_theory_of_garbage_collection

### 1 Introduction
We begin by defining basic terminology, and introducing simple formalisms for the
behavior of the garbage collector over the object graph.

#### 1.1 Basic Terminology
The *heap* is the space in memory in which objects reside. Objects can be referred
to by other objects, or by *roots*, which are references to objects whose locations
are known, e.g. global variables. The *object graph* is the set of all objects
in the heap, as well as the connections between the objects. A *mutator* is
anything that modifies the object graph, that isn't the collector itself, i.e.
the user program. A *snapshot* is the state of the entire heap at some time instant.
The *reference count* of an object *o* is the number of objects that have a reference
to *o* and are also reachable from a root.

#### 1.2 Basic Symbols
We define the following symbols:

-  $$V$$ is the universe of objects in the heap.
-  $$E$$ is multiset of edges in the object graph
-  $$R$$ is the multiset of roots
-  $$\rho(v)$$, where $$v \in V$$ is the reference count of *v*, as computed by the collector.
-  $$P(v)$$, where $$v \in V$$ is the reference count of *v*, as defined by the object graph.
-  $$G = < V,E,R >$$ is the object graph

#### 1.3 Tracing Collection
Tracing collection works by first traversing the graph, and tracing through all
objects reachable from the roots, then collecting all objects that are not marked.

#### 1.4 Reference Counting
Reference counting works by keeping a reference count of each object, and when
and object's reference count reaches zero, that object is collected. The reference
count of an object is incremented whenever its address is assigned, and decremented
when an object that refers to it reaches reference count zero or when an object
loses its reference to it.

### 2 Unifying Theory

#### 2.1 Modifications to Original Algorithms
We modify tracing to keep track of a reference count instead of simply marking each
object, and modify reference counting to do decrement operations at "collection time".

#### 2.2 Formalisms
We define a fix-point computation over a function
$$f: \mathbb{N}^{\vert V \vert} \rightarrow
\mathbb{N}^{\vert V \vert}$$, where
$$f(\rho_1, \rho_2, \dots \rho_{\vert V \vert})$$ is the computed reference
counts for the objects in the object graph, as a function of the previous
computed reference counts, for a given snapshot.

We then define:

-  $$V_F = \left\{ v \in V \vert \rho(v) = 0 \right\}$$ is the set of free objects
-  $$V_L = \left\{ v \in V \vert P(v) \gt 0 \right\}$$ is the set of live objects
-  $$V_D = \left\{ v \in V \vert P(v) = 0 \right\}$$ is the set of dead objects

Note that tracing collection calculates the least fix-point of $$f$$, minimizing
the value of $$\rho(v)$$ for all *v* in *V*, and thus for tracing collection
$$V_F = V_D$$ after each collection.

## The Train Algorithm
The Train Algorithm is a garbage collection algorithm that non-disruptively collects
garbage. The original paper that describes it can be found [here][train-algorithm].

#### Terminology
The *Mature Object Space* (MOS) is where the algorithm handles objects that have
been alive beyond some finite length of time. We refer to all references to objects
in the MOS from outside of it as *roots*; this includes pointers from the stack,
global variables, and pointers from objects that have not been alive long enough
to be in the MOS. We use the term *leader* to refer the objects that roots point
to, and *follow* to refer to objects that can be reached from any leader.

We also segment the MOS into contiguous segments which we refer to as *cars*, and
further group cars into non-contigous *trains*. Additionally, we order trains and cars
numerically in the MOS. Each car has a *remembered set*, which contains locations
of all exterior references to objects in that car, and each train has a remembered
set which is the union of the remembered sets of its cars.

[train-algorithm]: https://www.researchgate.net/publication/2683671_Incremental_Collection_of_Mature_Objects

#### The Algorithm
We go down the trains and clean them up like so:

1. Move leaders into the last train (in any car)
2. Copy-collect followers of leaders into last train
3. Move objects reachable by other cars to those cars
4. Repeat process 1-3 for all cars in current train
5. Move the now empty train to the end and go to next train in line.

```shell
hi -sa
```
