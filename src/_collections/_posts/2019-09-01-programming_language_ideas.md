---
title: Ideas to Include in a New Programming Language
categories: [programming]
tags: [fun]
published: false
---
<!-- {% raw %} -->
<!-- {% include refc-small.html text="ref commit" commit="3cad965..." %} -->
<!-- {% include ref-commit.html text="ref commit" commit="3cad965..." %} -->
<!-- {% endraw %} -->

### Idea: DAG of Programming Language Features

##### Application: Disabling Language Features

### Idea: Auto-Destructure Structs

##### Application: RAII without the Overhead

### Idea: Scopes as Anonymous Structs

##### Application: Immediately-Invoked Lambdas without the Abstraction Cost

### Idea: Contracts Over Types and Data Fields

##### Application: Fine-Grained Safety Checks

### Idea: Associative Scopes

##### Application: Coarse-Grained (i.e. Declarative) Control Flow

### Idea: Loop Invariant Declaration

##### Application: Fine-Grained Safety Checks

##### Application: Easier Optimization

### Idea: Orthogonal Pointer Annotations

##### Application: Customizable Safety Checks

### Idea: Compile-Time Source Edits

##### Application: Cannonicalization Work Can be Saved to Source

### Idea: Language Support for Allocators

##### Application: Intrusive Allocators

### Idea: Flexible Namespace Captures
Restrict access to a name in the surrounding namespace, or to all but a subsection
of names.

##### Application: Debugging Invariants
Let's say I have a global that, for some reason, doesn't take on the value I
expect it to. With namespace captures, I can simultaneously debug it while also
making my code easier to read. By putting namespace capture restrictions on scopes
in question, I can check, at compile time, which scopes are using the global.
Additionally, I can check exactly which scopes *modify* the global, which is much
harder to do with something simple like text search.

### Idea: Module Permissions
Programmatically prevent modules from doing certain kinds of tasks. For example,
prevent a module from doing anything but computation, as a feature of the language.

##### Application: Secure Black Boxes
If I import a module, I expect it to do what it says on the tin; if it doesn't,
that could be a security vulnerability. I'd like to be able to, at compile time,
check that the module I'm importing doesn't copy my entire file system, compress it,
and post it in a public repo on GitHub.

